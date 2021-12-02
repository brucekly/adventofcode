(require 'uiop)

(defparameter *input* (uiop:read-file-forms "input/day01.txt"))

(defun increases (list win)
  (count t (mapcar #'< list (nthcdr win list))))

(print (increases *input* 1))
(print (increases *input* 3))
