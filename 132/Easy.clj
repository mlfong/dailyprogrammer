(defn gcd [one two]
    (loop [a one b two]
      (if (= a b)
        a
        (if (> a b) 
          (recur (- a b) b)
          (recur a (- b a))))))

(println (gcd 32 12))
(println (gcd 142341 512345))
(println (gcd 65535 4294967295))