.text
    main:   li a7, 5    #Get number of numbers to sum
            ecall

            mv t0, a0   #Registers to loop through
            li t1, 1
            li t2, 0    #Register to sum all values

    loop1:  bgt t1, t0, end
            ecall
            add t2, t2, a0
            addi t1, t1, 1
            j loop1

    end:    li a7, 1
            mv a0 t2
            ecall

/* Professor solution
.data
    msg01: .asciiz "Amount of numbers to read: "
    msg02: .asciiz "introduce number: "
    msg03: .asciiz "The result is: "
 .text
    main:
        # print message "Amount of numbers to read: "...
        la a0 msg01
        li a7 4
        ecall

        # read the amount of numbers to read
        li a7 5
        ecall
        mv t0 a0

        # if quantity of numbers to read is zero, finish.
        beq x0, t0 f01

        # loop (t1: counter of numbers, t2: partial result)
        li t1 0
        li t2 0

    b01:
        # print "introduce number: "
        la a0 msg02
        li a7 4
        ecall

        # read the number
        li a7 5
        ecall

        # Calculation of the square and partial addition
        mul v0 a0 a0
        add t2 t2 v0

        # loop
        addi t1 t1 1
        blt t1 t0 b01

        # print "The result is: "...
        la a0 msg03
        li a7 4
        ecall

        # print the result
        mv a0 t2
        li a7 1
        ecall

    f01: li a7 10
    ecall