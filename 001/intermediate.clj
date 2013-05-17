;; create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.
;; (note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)
;; 
;; Create a menu driven program
;; Using the menu drive program allow a user to add/delete items
;; The menu should be based on an events calender where users enter the events by hour
;; No events should be hard-coded.
(def menu "Main menu, enter # of option to perform action:")
(def options ( vector 
	"1. add event"
	"2. del event"
	"3. view events"
	"4. exit"
	))
	
(defn print-menu []
	(println menu)
	(doseq [x options] (println x)))

(defn get-input [prompt]
  (println prompt)
  (read-line))

(defn main []
	(print-menu)
	(loop [input (get-input "hi?")]
	(if (= input "4")
		(println input)
		(recur (get-input "That is not valid.\nWhat is your decision?")))))
		
(main)