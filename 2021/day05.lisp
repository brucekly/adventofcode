(require "asdf")

(defparameter *input* (uiop:read-file-lines "input/day05.txt"))

(defun str-to-coords (str)
  (apply #'cons
	 (mapcar #'parse-integer
		 (uiop:split-string str :separator ","))))

(defun str-to-points (str)
  (mapcar #'str-to-coords
	  (remove-if (lambda (s) (string= s ""))
		     (uiop:split-string str :separator " ->"))))

(defun normalise (int)
  (if (= 0 int)
      0
      (/ int (abs int))))

(defun direction (a b)
  (cons (normalise (- (car b) (car a)))
	(normalise (- (cdr b) (cdr a)))))

(defun coord+ (a b)
  (cons (+ (car a) (car b))
	(+ (cdr a) (cdr b))))

(defun str-to-line (str)
  (destructuring-bind
      (a b) (str-to-points str)
    (let ((dir (direction a b)))
      (loop for point = a
	      then
	      (coord+ point dir)
	    collect point
	    until (equal point b)))))

(defun count-overlapping-points (input)
  (let ((table (make-hash-table :test #'equal)))
    (loop for str in input
	  do (loop for point in (str-to-line str)
		   do (incf (gethash point table 0))))
    (loop for v being the hash-values in table
          if (>= v 2)
            sum 1 into count
	  finally (return count))))

(defun remove-diagonals (input)
  (remove-if
   (lambda (x)
     (let ((dir (apply #'direction (str-to-points x))))
       (= (abs (car dir))
	  (abs (cdr dir)))))
   input))

(print (count-overlapping-points (remove-diagonals *input*)))
(print (count-overlapping-points *input*))
