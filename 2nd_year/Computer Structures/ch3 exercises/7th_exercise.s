.data
	str:    .string "alfonso has only 1 a but this phrase has 5"
    vowel:  .string "a"

.text
	Vowels: mv t0 a0
            mv t1 a1
            lb t4 0(t1)
            li t2 0
        
        #Check if string is empty
        loop1:  lb t3 0(t0)
                beq x0 t3 end2
                bne t4 t3 end1
                addi t2 t2 1

        #Next character
        end1:   addi t0 t0 1
                j loop1

        #Finish function
        end2:   mv a0 t2
                jr ra
    
    main:	la a0 str
            la a1 vowel
            jal ra Vowels

            #Print result of function
            li a7 1
            ecall

            #Exit
            li a7 10
            ecall