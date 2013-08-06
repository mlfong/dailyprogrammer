(defn n-div-digits [N M]
	(let [x (- (Math/pow 10 N) 1)]
		(- x (mod x M))))
		
(prn (n-div-digits 3 2))
(prn (n-div-digits 7 4241275))