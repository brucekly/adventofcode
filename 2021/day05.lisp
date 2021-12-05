(require "asdf")
(ql:quickload "cl-ppcre")

(defparameter *input* (uiop:read-file-lines "input/day05.txt"))

(defun str-to-ints (str)
  (mapcar #'parse-integer (cl-ppcre:all-matches-as-strings "\\d+" str)))

(defun str-to-line (l)
  (destructuring-bind (x1 y1 x2 y2) l
    (let ((dx (signum (- x2 x1)))
	  (dy (signum (- y2 y1))))
      (loop for (x y) = (list x1 y1)
	      then (list (+ x dx) (+ y dy))
	    collect (list x y)
	    until (and (= x x2) (= y y2))))))

(defun count-overlaps (lines &optional (table (make-hash-table :test #'equal)))
  (dolist (l lines)
    (destructuring-bind (x1 y1 x2 y2) l
      (let ((dx (signum (- x2 x1)))
	    (dy (signum (- y2 y1))))
	(loop for (x y) = (list x1 y1)
		then (list (+ x dx) (+ y dy))
              do (incf (gethash (list x y) table 0))
	      until (and (= x x2) (= y y2))))))
  (loop for v being the hash-values of table count (>= v 2)))

(defun not-straight? (line)
  (destructuring-bind (x1 y1 x2 y2) line
    (and (not (= x1 x2)) (not (= y1 y2)))))

(let ((lines (mapcar #'str-to-ints *input*)))
  (print (count-overlaps (remove-if #'not-straight? lines)))
  (print (count-overlaps lines)))
