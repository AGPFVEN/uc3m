.data
    a: .word 5
    b: .word 7
    c: .word 9

.text
    func:   #Integer function (I only gonna sum all)
            mv t0 a0
            add t0 t0 a1
            add t0 t0 a2

            mv a0 t0
            jr ra 

    #Load adresses to registers (arguments of function)
    main:   la t0 a
            lw a0 0(t0)

            la t0 b
            lw a1 0(t0)

            la t0 c
            lw a2 0(t0)

            #Call function
            jal ra func

            #Print result
            li a7 1
            ecall

            #End program
            li a7 10
            ecall