(defn easy-147 []
  (prn (if (some #{(read-line)} '("1" "2" "4" "5"))
    "Invalid score"
    "Valid score")))
(easy-147)