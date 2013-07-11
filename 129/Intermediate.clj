(defn euclid-dist [vect]
	(Math/sqrt (reduce + (map * vect vect) )))
	
(defn unit-vector [vect]
	(let [eud (euclid-dist vect)]
		(for [x vect] (/ x eud))))
		
(defn dot-product [vect1 vect2]
	(reduce + (map * vect1 vect2)))

(euclid-dist [1,2,3])
(println (euclid-dist [84.82,121.00,467.05,142.14,592.55,971.79,795.33])); 1479.26
(println (unit-vector [0,1,0,1])); 0 0.707107 0 0.707107
(println (dot-product [1,1] [1.2,3.4]))

(let [N (read-string (read-line))]
 (let [vectors (repeatedly N read-line)]
	(println vectors)
		(println (type vectors))
		(let [M (read-string (read-line))]
			(let [commands (repeatedly N read-line)]
				(println commands)))))
