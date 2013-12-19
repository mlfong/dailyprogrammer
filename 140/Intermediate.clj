; abbreviating functions
(require '[clojure.string :as str])
(def rs read-string)

; makes a vector of n 0s
(defn make-row [n] (into [] (for [x (range n)] (str 0)) ))

(defn intermediate-140 []
  ; setup
  (def matrix {})
  (def settings (str/split (read-line) #" "))
  (def N (rs (first settings)))
  (def M (rs (last settings)))
  ; create matrix
  (doseq [x (range N)]
    (def matrix 
      (assoc matrix x (make-row N))))
  ; populate adjlist
  (doseq [x (range M)]
    (def line (str/split (read-line) #" "))
    (def nodes (split-at (.indexOf line "->") line))
    (doseq [l (first nodes)]
      (doseq [r (rest (last nodes))]
        (def matrix 
          (assoc matrix (rs l) 
            (assoc (matrix (rs l)) (rs r) "1"))))))
  ; printing
  (doseq [x (range N)]
    (prn (str/join (matrix x)))))

(intermediate-140)