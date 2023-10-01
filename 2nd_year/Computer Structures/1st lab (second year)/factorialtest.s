.text
    main:
        li a0, 4            #Argument 1
        fcvt.s.w f0, a0

        jal ra factorial    #"Call" function
        factorial:
        addi t0, t0, 1
        mul t1, t0, t1
        j factorial_loop

    end_factorial:
        mv a0, t1
        jr ra