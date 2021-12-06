(require "asdf")

(defparameter *input* (uiop:read-file-line "input/day06.txt"))

(defun str-to-ints (str)
  (mapcar #'parse-integer (uiop:split-string str :separator ",")))

(defun counts (ints)
  (loop for n from 0 to 8
	collect (count n ints)))

(defun advance (fishes)
  (let ((next (append (cdr fishes) (list (car fishes)))))
    (incf (nth 6 next) (nth 8 next))
    next))

(defun simulate-fishes (times input)
  (loop repeat (1+ times)
	for fish = input then (advance fish)
	finally (return fish)))

(let ((initial (counts (str-to-ints *input*))))
  (print (apply #'+ (simulate-fishes 80 initial)))
  (print (apply #'+ (simulate-fishes 256 initial))))
