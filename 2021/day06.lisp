(require "asdf")
(ql:quickload "cl-ppcre")

(defparameter *input* (uiop:read-file-line "input/day06.txt"))

(defun str-to-ints (str)
  (mapcar #'parse-integer (cl-ppcre:all-matches-as-strings "\\d+" str)))

(defun ints-to-count (ints)
  (let ((fish (make-hash-table)))
    (loop for n in ints
	  do (incf (gethash n fish 0))
	  finally (return fish))))

(defun advance-fishes (fishes)
  (let ((new-fish (make-hash-table)))
    (loop for k being the hash-keys in fishes using (hash-value v)
	  if (zerop k) do
	    (incf (gethash 6 new-fish 0) v)
	    (incf (gethash 8 new-fish 0) v)
	  else do
	    (incf (gethash (1- k) new-fish 0) v)
	  finally (return new-fish))))

(defun simulate-fishes (times input)
  (loop for n from 0 to times
	for fish = input
	  then (advance-fishes fish)
	finally (return fish)))

(defun count-fishes (fishes)
  (loop for v being the hash-values in fishes
	sum v))

(let ((initial-fishes (ints-to-count (str-to-ints *input*))))
  (print (count-fishes (simulate-fishes 80 initial-fishes)))
  (print (count-fishes (simulate-fishes 256 initial-fishes))))
