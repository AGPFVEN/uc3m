.text
    main:
    li a0, 4            #Argument 1
    jal ra factorial    #"Call" function

    li a7, 10           #End program
    ecall

    e: #Until 6
    li t0, 1            #E counter
    li t1, 1            #E j
    li t2, 0            #E result 
    
    fcvt.s.w f0, a0     #Convert to float32
    fcvt.s.w f1, a1

    fdiv.s f2, f0, f1

    e_loop:
    
    
    factorial:          #Recives (a0) Uses (t01) Return (a0)
    li t0, 0            #Factorial Counter
    li t1, 1            #Factorial Result

    factorial_loop:
    beq t0 a0 end_factorial
    addi t0, t0, 1
    mul t1, t0, t1
    j factorial_loop

    end_factorial:
    mv a0, t1
    jr ra