(require '[clojure.string :as str])
(def phone {\2 "abc" \3 "def" \4 "ghi" \5 "jkl" \6 "mno" \7 "pqrs" \8 "tuv" \9 "wxyz"})

(defn intermediate [line] 
	(def value
		(apply str (for [x (str/split line #" ")] 
			(get (get phone (first x)) (- (count x) 1 )))))
			
	(doseq [x (line-seq (clojure.java.io/reader "./brit-a-z.txt"))]
		(if (.startsWith x value)
			(prn x))))

(intermediate (read-line))