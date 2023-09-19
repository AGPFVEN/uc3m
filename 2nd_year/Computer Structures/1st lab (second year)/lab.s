.text
    main:
    li a0, 4            #Argument 1
    jal ra factorial    #"Call" function

    li a7, 10           #End program
    ecall

    factorial:
    li t0, 0            #Counter
    li t1, 1            #Result

    factorial_loop:
    beq t0 a0 end_factorial
    addi t0, t0, 1
    mul t1, t0, t1
    j factorial_loop

    end_factorial:
    mv a0, t1
    jr ra