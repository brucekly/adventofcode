(require "asdf")
(ql:quickload "cl-ppcre")
(ql:quickload "split-sequence")

(defparameter *input* (uiop:read-file-lines "input/day04.txt"))

(defparameter *winning-configurations*
  (loop for n below 5
	collect (mapcar (lambda (x) (+ x (* 5 n)))
			(loop for x below 5 collect x))
	collect (mapcar (lambda (x) (+ x n))
			(loop for x below 5 collect (* 5 x)))))

(defun str-to-ints (str)
  (mapcar #'parse-integer (cl-ppcre:all-matches-as-strings "\\d+" str)))

(defun parse-board (board)
  (str-to-ints (format nil "~{~A ~}" board)))

(defun winning? (matches)
  (loop for configuration in *winning-configurations*
	do (if (subsetp configuration matches) (return t))))

(defun board-score (board numbers n)
  (* (apply #'+ (set-difference board (subseq numbers 0 n)))
     (nth (1- n) numbers)))

(defun evaluate-board (board numbers)
  (loop for n from 0
	for number in numbers
	for matches = (list (position number board))
	  then (append matches (list (position number board)))
        if (winning? matches) do
	  (return (cons n (board-score board numbers (1+ n))))))

(defun find-score (evaluations fn)
  (cdr (assoc (apply fn (mapcar #'car evaluations)) evaluations)))

(let* ((paragraphs (split-sequence:split-sequence "" *input* :test #'equal))
       (boards (mapcar #'parse-board (cdr paragraphs)))
       (numbers (str-to-ints (caar paragraphs)))
       (evaluations (mapcar (lambda (b) (evaluate-board b numbers)) boards)))
  (print (find-score evaluations #'min))
  (print (find-score evaluations #'max)))
