(require 'uiop)

(defparameter *input*
  (mapcar (lambda (x)
	    `(,(intern (string-upcase (first x)))
	      ,(parse-integer (second x))))
	  (mapcar #'uiop:split-string (uiop:read-file-lines "input/day02.txt"))))

(defun part1-move (state course)
  (let ((hor (first state)) (dep (second state))
	(dir (first course)) (mag (second course)))
    (case dir
      (down (list hor (+ dep mag)))
      (up (list hor (- dep mag)))
      (forward (list (+ hor mag) dep))
      (t (list hor dep)))))

(defun part2-move (state course)
  (let ((hor (first state)) (dep (second state)) (aim (third state))
	(dir (first course)) (mag (second course)))
    (case dir
      (down (list hor dep (+ aim mag)))
      (up (list hor dep (- aim mag)))
      (forward (list (+ hor mag) (+ dep (* aim mag)) aim))
      (t (list hor mag dep)))))

(print (apply #'*
	      (reduce #'part1-move *input*
		      :initial-value '(0 0))))

(print (apply #'* (subseq
		   (reduce #'part2-move *input*
			   :initial-value '(0 0 0))
		   0 2)))
