(defn unit-test [testcase]
  (let [[num word1 word2] (map read-string (clojure.string/split testcase #" "))]
    (if 
      (or
        (and (= num 0) (= (str word2) (clojure.string/reverse (str word1))))
          (and (= num 1) (= (str word2) (clojure.string/upper-case (str word1)))))
            "Good test data" "Mismatch! Bad test data")))