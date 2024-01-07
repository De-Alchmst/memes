(module

  ;;;;;;;
  ;; ! ;;
  ;;;;;;;

  (export "factorial" (func $factorial))
  (func $factorial (param $n i64) (result i64)

     (local $outcome i64)

     ;; default value
     (local.set $outcome (i64.const 1))

     ;; if more than one
     (i64.ge_s (local.get $n) (i64.const 1))
     (if
       (then
         (local.set $outcome (local.get $n))
         (loop $L
           ;; way more obvious than n--
           (local.set $n (i64.sub (local.get $n) (i64.const 1)))

           ;; end once (local.get $n) is equal to the number
           ;; of bitches avarage python developer gets
           (i64.ne (local.get $n) (i64.const 0))
           (if
             (then
               (local.set $outcome (i64.mul (local.get $outcome) (local.get $n)))
               (br $L))))))
       

  ;; return the outcome
  (local.get $outcome))

  ;;;;;;;;;;;;;;;;
  ;; SPIRAL GUY ;;
  ;;;;;;;;;;;;;;;;
(; ⠀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢂⣂⡢⠢⠦⠦⠒⠒⠒⠒⠒⠢⠦⠦⣂⣂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⠀⠉⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⢄⠀⠀⠀⠀⠀⠀⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⠀⢄⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀ ;)
(; ⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄ ;)
(; ⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣ ;)
(; ⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ ;)
(; ⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⢀⡤⠤⠤⢄⡀⠄⠀⠠⠀⠀⠄⠀⠠⠀⠀⠄⠀⢸ ;)
(; ⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⡔⠁⠀⠀⠅⠀⠱⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ ;)
(; ⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡚⠀⠀⠀⠀⣏⣃⡰⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇ ;)
(; ⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣪⠀⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀ ;)
(; ⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⢆⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⠀⠀ ;)
(; ⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠈⠢⡀⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⣀⠴⠉⠀⠀⠀⠀ ;)
(; ⠀⠇⠀⢀⠀⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠀⡂⠀⡀⠈⡑⠢⠤⢄⠆⠤⠤⠔⢒⠉⡀⢀⠀⡀⢀⠀⡀ ;)
  (export "fibonacci" (func $fibonacci))
  (func $fibonacci (param $n i64) (result i64)
     (local $first i64)
     (local $second i64)

     (local.set $first (i64.const 0))
     (local.set $second (i64.const 1))

     (loop $L ;; imagine needing for loop
       (i64.gt_s (local.get $n) (i64.const 1))
       (if
         (then
           ;; imagine having to make temporary variable for this
           (local.get $first)
           (local.set $first (local.get $second))
           (local.set $second (i64.add (local.get $second)))

           (local.set $n (i64.sub (local.get $n) (i64.const 1)))
           (br $L))))

     ;; if you have to write return, your algorythm is bad
     ;; if you must write return, your language is bad
     (local.get $first))


  ;;;;;;;;;;;;;;;;;;
  ;; round things ;;
  ;;;;;;;;;;;;;;;;;;

  ;; value of pi, not that hard to come by ↓
  (global $pi f32 (f32.const 3.141592653589793))

  ;; rare case of english word pronounced without any vowels
  (export "circumference" (func $circumference))
  (func $circumference (param $r f32) (result f32)
     (f32.mul (f32.mul (global.get $pi) (local.get $r)) (f32.const 2)))

  (export "circleSurface" (func $circlesurface))
  (func $circlesurface (param $r f32) (result f32)
     ;; first I say I multiply a lot
     (f32.mul (f32.mul
        ;; then I say what I multiply a lot
        (local.get $r) (local.get $r)) (global.get $pi)))

  (export "sphereVolume" (func $sphereV))
  (func $sphereV (param $r f32) (result f32)
  ;; V = 4/3*π*r³
     (f32.mul
       (f32.mul
         (f32.div (f32.const 4) (f32.const 3))
         (global.get $pi))
       
       (call $f32pow (local.get $r) (i32.const 3))))

  ;; power is builtin only for ints
  ;; but I don't mind writing extra six lines of code
  (func $f32pow (param $x f32) (param $y i32) (result f32)
     (local $res f32) (local.set $res (f32.const 1))
     (loop $L (local.get $y) (if (then
         (local.set $res (f32.mul (local.get $res) (local.get $x)))
         (local.set $y (i32.sub (local.get $y) (i32.const 1)))
         (br $L)))) (local.get $res))
  ;; definitly six lines of code ↑, no bullshit here

)
