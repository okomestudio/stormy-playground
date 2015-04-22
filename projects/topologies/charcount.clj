(ns charcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn charcount [options]
   [
    ;; spout configuration
    {"char-spout" (python-spout-spec
          options
          "spouts.chars.CharSpout"
          ["char"]
          )
    }
    ;; bolt configuration
    {"count-bolt" (python-bolt-spec
          options
          {"char-spout" :shuffle}
          "bolts.charcount.CharCounter"
          ["char" "count"]
          :p 2
          )
    }
  ]
)
