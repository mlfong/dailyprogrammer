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