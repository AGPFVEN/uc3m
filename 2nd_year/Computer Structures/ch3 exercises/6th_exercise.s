.data
	msg1: .string "Amount of numbers to read:"
    msg2: .string "Introduce number:"

.text
	main:	la a0, msg1 	#Show first message
    		li a7, 4
            ecall
            
            li a7, 5		#Read int
            ecall
            
            mv t0, a0		#Set up counter
            li t1, 0		#Set up result
            
    loop1:  la a0, msg2		#Show second message
            li a7, 4
            ecall
            
            li a7, 5		#Read int
            ecall
            
            mul a0, a0, a0	#Calculate square
            add t1, t1, a0	#Add square to result
            addi t0, t0, -1	#Counter control
            
            bge t0, zero, loop1
            
            mv a0, t1		#Show result
            li a7, 1
            ecall
            
            li a7, 10
            ecall