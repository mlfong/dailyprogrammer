;; create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
;; your name is (blank), you are (blank) years old, and your username is (blank)
;; for extra credit, have the program log this information in a file to be accessed later.


(defn easy-1 [] 
	(println "What is your name?")
	(let [name (read-line)]
		(println "How old are you?")
		(let [age (read-line)]
			(println "What is your username?")
			(let [sn (read-line)]
				(println (str "your name is " name ", you are " age " years old, and your username is " sn))
			))
		)
	)
	
	
(easy-1)