(module

  ;;;;;;;
  ;; ! ;;
  ;;;;;;;

  (export "factorial" (func $factorial))
  (func $factorial (param $n i32) (result i32)

     (local $outcome i32)

     ;; default value
     (local.set $outcome (i32.const 1))

     ;; if more than one
     (i32.ge_s (local.get $n) (i32.const 1))
     (if
       (then
         (local.set $outcome (local.get $n))
         (loop $L
           ;; way more obvious than n--
           (local.set $n (i32.sub (local.get $n) (i32.const 1)))

           ;; end once i32.eqz (local.get $n)
           (i32.ne (local.get $n) (i32.const 0))
           (if
             (then
               (local.set $outcome (i32.mul (local.get $outcome) (local.get $n)))
               (br $L))))))
       

  ;; return the outcome
  (local.get $outcome))

  ;;;;;;;;;;;;;;;;
  ;; SPIRAL GUY ;;
  ;;;;;;;;;;;;;;;;

  (export "fibonacci" (func $fibonacci))
  (func $fibonacci (param $n i32) (result i32)
     (local $first i32)
     (local $second i32)

     (local.set $first (i32.const 0))
     (local.set $second (i32.const 1))

     (loop $L ;; imagine needing for loop
       (i32.gt_s (local.get $n) (i32.const 1))
       (if
         (then
           ;; imagine having to make temporary variable for this
           (local.get $first)
           (local.set $first (local.get $second))
           (local.set $second (i32.add (local.get $second)))

           (local.set $n (i32.sub (local.get $n) (i32.const 1)))
           (br $L))))

     ;; if you have to write return, your algorythm is bad
     ;; if you must write return, your language is bad
     (local.get $first))
)
