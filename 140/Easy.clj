
(require '[clojure.string :as str])

(defn variable-notation []
	(let [convention (read-line)]
		(let [input (read-line)]
			(if (= convention "2")
				(prn (str/upper-case (str/replace input #" " "_" )))
			(if (= convention "1")
				(prn (str/replace input #" " "_"))
			(if (= convention "0")
				(prn (str (first (str/split input #" ")) (str/join "" (map str/capitalize (rest (str/split input #" "))))))))))))

(variable-notation)