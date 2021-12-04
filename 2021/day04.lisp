(require "asdf")

(defparameter *input* (uiop:read-file-lines "input/day04.txt"))

(defparameter *winning-configurations*
  (loop for n below 5
	collect (mapcar (lambda (x) (+ x (* 5 n))) (loop for x below 5 collect x))
	collect (mapcar (lambda (x) (+ x n)) (loop for x below 5 collect (* 5 x)))))

(defun split-paragraphs (input)
  (loop with paragraph
	for e in input
	if (equal e "")
	  collect (nreverse paragraph) into paragraphs and do (setf paragraph nil)
	else
	  do (push e paragraph)
	finally
	   (return (concatenate 'list paragraphs (list (nreverse paragraph))))))

(defun get-board (board)
  (with-input-from-string (in (format nil "~{~A ~}" board))
    (loop for x = (read in nil nil) while x collect x)))

(let ((paragraphs (split-paragraphs *input*)))
  (defparameter *boards*
    (mapcar #'get-board (cdr paragraphs)))
  (defparameter *numbers*
    (mapcar #'parse-integer
	    (uiop:split-string (caar paragraphs) :separator ","))))

(defun get-matches (board nums)
  (loop for num in nums
	collect (position num board)))

(defun winning? (matches)
  (loop for configuration in *winning-configurations*
	do (if (subsetp configuration matches)
	       (return t))))

(defun board-win-number (board numbers)
    (loop for n below (length numbers)
       do (let ((nums (subseq numbers 0 n)))
	    (if (winning? (get-matches board nums))
		(return n)))))

(defun board-score (board numbers)
  (let ((win-number (board-win-number board numbers)))
    (* (apply #'+
	      (set-difference
	       board
	       (subseq numbers 0 win-number)))
       (nth (1- win-number) numbers))))

(defun choose-board (boards numbers f)
  (let ((win-numbers (loop for board in boards
			   collect (board-win-number board numbers))))
    (nth (position (apply f win-numbers) win-numbers) boards)))

(print (board-score (choose-board *boards* *numbers* #'min) *numbers*))
(print (board-score (choose-board *boards* *numbers* #'max) *numbers*))
