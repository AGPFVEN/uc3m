.data
    A1: .word 5, 8, 7, 9, 2, 4, 5, 9
    A2: .word 1, 4, 3, -8, 5, 6, 5, 9
    .align 2
    A3: .zero 32

.text
    #Load adresses into registers
    merge:  mv t0 a0
            mv t1 a1
            mv t2 a2
            mv t3 a3
            li t6 1

        #Load integers into registers
        Loop1:  lw t4 0(t1)
                lw t5 0(t2)

                #Compare
                beq t0 t6 end_merge
                bge t4 t5 Loop2
                mv t4 t5 

        #Store integer in 3rd array
        Loop2:  sw t3 0(t4)

                #Pass next integers
                addi t1 t1 4
                addi t2 t2 4
                addi t3 t3 4
                addi t6 t6 1

                bne t4 x0 Loop1
        
        #End function
        end_merge: jr ra 

    #Load adresses (arguments)
    main:   li a0 9
            la a1 A1
            la a2 A2
            la a3 A3

            #Call function
            jal ra merge