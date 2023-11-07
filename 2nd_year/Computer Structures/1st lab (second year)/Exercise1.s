  tg:
  #Copy value in stack
  addi sp, sp, -8
  sw ra, 0(sp)
  fsw fa0, 4(sp)

  jal ra sin

  fmv.s fa1, fa0
  flw fa0, 4(sp)
  fsw fa1, 4(sp)

  jal ra cos

  fmv.s fa1, fa0
  flw fa0, 4(sp)
  
  fdiv.s fa0, fa0, fa1
  lw ra, 0(sp)
  addi sp, sp, 8

  jr ra


  sin:
  li s1, 13    #Limit
  fcvt.s.w fs0, zero
  li s0, 0

  #Store argument and ra to stack
  addi sp, sp, -8
  sw ra, 0(sp)
  fsw fa0, 4(sp)

  loop_sin:

  #Calculate sign #fs1 sign
  mv a0, s0
  jal ra exponent_sign
  fcvt.s.w fs1, a0

  #Exponent
  li s3, 2
  flw fa0, 4(sp)
  mul a0, s0, s3
  addi a0, a0, 1
  jal ra power_of
  fmul.s fs1, fs1, fa0

  #factorial
  mul a0, s0, s3
  addi a0, a0, 1
  jal ra factorial_float
  fmv.s fs2, fa0
  fdiv.s fs1, fs1, fs2

  #Sum of
  fadd.s fs0, fs0, fs1
  addi s0, s0, 1
  bne s0, s1, loop_sin

  #End function
  fmv.s fa0, fs0
  lw ra, 0(sp)
  addi sp, sp, 8
  jr ra

  cos:
  li s0, 1    #Counter, I need to add 1 at the end
  fcvt.s.w fs0, s0
  li s1, 12    #Limit

  #Store argument and ra to stack
  addi sp, sp, -8
  sw ra, 0(sp)
  fsw fa0, 4(sp)

  loop_cos:

  #Calculate sign #fs1 sign
  mv a0, s0
  jal ra exponent_sign
  fcvt.s.w fs1, a0

  #Exponent
  li s3, 2
  flw fa0, 4(sp)
  mul a0, s0, s3
  jal ra power_of
  fmul.s fs1, fs1, fa0

  #factorial
  mul a0, s0, s3
  jal ra factorial_float
  fmv.s fs2, fa0
  fdiv.s fs1, fs1, fs2

  #Sum of
  fadd.s fs0, fs0, fs1
  addi s0, s0, 1
  bne s0, s1, loop_cos

  #End function
  fmv.s fa0, fs0
  lw ra, 0(sp)
  addi sp, sp, 8
  jr ra

  factorial_float:#Recives (a0) Uses (t01) Return (a0)
  li t0, 0            #Factorial Counter
  li t1, 1            
  fcvt.s.w ft0, t1	#Factorial Result

  factorial_loop_float:
  beq t0 a0 end_factorial_float
  addi t0, t0, 1
  fcvt.s.w ft1, t0
  fmul.s ft0, ft0, ft1
  j factorial_loop_float

  end_factorial_float:
  fmv.s fa0, ft0
  jr ra

  exponent_sign:#a0 (exponent, integer)
  li t0, 2
  rem a0, a0, t0          #Calculate n % 2
  bne a0, zero, negative  #If even a0 = -1, else a0 = 1
  li a0, 1
  j End
  negative:
  li a0, -1
  End:
  jr ra

  power_of:#fa0 (base), a0 (exponent)
  li t0, 1                #Counter
  fmv.s ft0, fa0          #Base

  power_loop:
  beq t0, a0, End
  fmul.s fa0, fa0, ft0
  addi t0, t0, 1
  j power_loop

  E:#Until 6
  #Put 1 into a float register
  li s0, 1
  fcvt.s.w fs0, s0
  fmv.s fs3, fs0

  #Declare starting values
  li s0, 0            #E counter
  li s1, 6            #Limit
  li s2, 1            #Result

  addi sp, sp, 4      #Store ra in Stack
  sw ra 0(sp)
  
  e_loop:
  addi s0, s0, 1

  mv a0, s0
  jal ra factorial_float

  #Float operations (Division and adition)
  fdiv.s fs2, fs0, fa0
  fadd.s fs3, fs3, fs2

  bne s0, s1, e_loop
  lw ra 0(sp)
  addi sp, sp, -4
  fmv.s fa0, fs3
  jr ra
