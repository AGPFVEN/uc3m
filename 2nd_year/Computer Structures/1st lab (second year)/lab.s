.text
    main:
    li a0, 4            #Argument 1
    jal ra factorial    #"Call" function

    li a7, 10           #End program
    ecall

    e: #Until 6
    li t0, 0            #E counter
    li t1, 0            #E result
    
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