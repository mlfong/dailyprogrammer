(require '[clojure.string :as str])
(defn easy-146 []
  (let [n-r (map read-string (str/split (read-line) #" "))]
    (let [n (first n-r)]
      (let [r (last n-r)]
        (prn (format "%.3f"
          (* 2 n r (Math/sin (/ Math/PI n)))))))))

(easy-146)
