.data
    m1: .word 2, 3
        .word 8, 4, 5
        .word 0, 9, 7

    m2: .word 3, 2
        .word 6, 3
        .word 1, 5
        .word 7, 9

.text
    main:
    #Read Inputs
    la a0, m1
    la a1, m2

    #Call Matrix_mul
    addi sp, sp, -4
    sw ra, 0(sp)
    j Matrix_mul

    Matrix_mul:
    #Copy matrix addresses
    mv s0, a0   #s0 = m1
    mv s1, a1   #s1 = m2

    #Check matrix dimensions (Check if multiplication is possible)
    sw s2, 0(s0)    #s2 -> dimensions of m1 (Rows)
    sw s3, 4(s1)    #s3 -> dimensions of m2 (Columns)----
    bne s2, s3, end_mul
    sw s4, 4(s0)    #s4 -> dimensions of m1 (Columns)
    sw s5, 0(s1)    #s5 -> dimensions of m2 (Rows)

    #Auxiliar data
    mul s2, s2, s3  #s2 -> number of elements in result





    mul s6, s2, s4  #s6 -> counter of m1 (numbers in matrix)
    addi s7, s5, -1
    mul s8, s8, s7
    addi s8, s8, -1 #s8 -> Column switcher
    mul s7, s3, s5  #s7 -> counter of m2 (numbers in matrix)

    #Move auxiliar to optimize space (s3 is already placed)
    mv s2, s6       #s2 -> counter of m1 (numbers in matrix)
    mv s4, s7       #s7 -> counter of m2 (numbers in matrix)
    mv s5, s8       #s8 -> Column switcher of m2

    #First loop 



    #End multiplication function
    end_mul:
    lw ra 0(sp)
    addi sp, sp, 4
    jal ra