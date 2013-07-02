(defn unit-test [testcase]
  (let [[num word1 word2] (clojure.string/split testcase #" ")]
    (if (or (and (= num "0")
                 (= word2 (clojure.string/reverse word1)))
            (and (= num "1")
                 (= word2 (clojure.string/upper-case word1))))
        "Good test data"
        "Mismatch! Bad test data")))

(println(unit-test "0 Car raC"))
(println(unit-test "0 Alpha AhplA"))
(println(unit-test "0 Discuss noissucsiD"))
(println(unit-test "1 Batman BATMAN"))
(println(unit-test "1 Graph GRAPH"))
(println(unit-test "1 One one"))