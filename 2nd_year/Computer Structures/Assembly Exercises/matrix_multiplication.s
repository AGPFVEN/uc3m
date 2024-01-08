.data
    m1: .word 3, 3
        .word 8, 4, 5
        .word 0, 9, 7
        .word 4, 4, 1

    m2: .word 3, 3
        .word 6, 3, 2
        .word 1, 5, 8
        .word 7, 9, 4

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
    sw s3, 4(s1)    #s3 -> dimensions of m2 (Columns)
    bne s2, s3, end_mul
    sw s2, 4(s0)
    sw s3, 0(s1)
    bne s2, s3, end_mul

    #Set up matrix counters
    sw s3, 4(s0)    #s3 -> Dimensions of m1 (Columns)
    mul s2, s2, s3  #s2 -> Counter (Limit)
    li s3, 0        #s3 -> Counter (Actual position)
    li s4, 0        #s4 -> Counter of m2 (Actual position)

    #End multiplication function
    end_mul:
    lw ra 0(sp)
    addi sp, sp, 4
    jal ra