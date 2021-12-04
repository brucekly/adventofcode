(require "asdf")

(defparameter *input* (uiop:read-file-lines "input/day03.txt"))

(defun str-to-bits (str)
  (map 'list #'digit-char-p str))

(defun bits-to-decimal (bits)
  (parse-integer (format nil "~{~A~}" bits) :radix 2))

(defun most-common-bit (lst)
  (let ((table (make-hash-table)))
    (loop for e in lst
          do (incf (gethash e table 0)))
    (if (< (gethash 1 table 0) (gethash 0 table 0)) 0 1)))

(defun most-common-bits (input)
  (let ((bits (mapcar #'str-to-bits input)))
    (loop for n below (length (car input))
	  collect
	  (most-common-bit
	   (mapcar (lambda (x) (nth n x)) bits)))))

(defun filter-consecutive-bits (input pred)
  (loop for oxygen = (mapcar #'str-to-bits input)
	  then
	  (let ((bits (mapcar (lambda (x) (nth n x)) oxygen)))
            (remove-if-not
	     (lambda (x) (= (nth n x) (funcall pred bits)))
	     oxygen))
	for n to (length (car input))
        do (if (= (length oxygen) 1)
	       (return (car oxygen)))))

(let* ((epsilon (most-common-bits *input*))
       (gamma (mapcar (lambda (x) (if (= x 1) 0 1)) epsilon)))
  (print (* (bits-to-decimal epsilon) (bits-to-decimal gamma))))

(let ((oxygen-generator-rating
	(filter-consecutive-bits
	 *input*
	 #'most-common-bit))
      (co2-scrubber-rating
	(filter-consecutive-bits
	 *input*
	 (lambda (x) (if (= (most-common-bit x) 1) 0 1)))))
  (print (* (bits-to-decimal oxygen-generator-rating)
	    (bits-to-decimal co2-scrubber-rating))))
