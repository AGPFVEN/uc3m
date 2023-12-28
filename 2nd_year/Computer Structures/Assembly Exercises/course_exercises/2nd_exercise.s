.data
	v: .word 7, 8, 3, 4, 5, 6

.text
	main:			addi sp, sp, 4
    				sw ra 0(sp)
                    
					#Parameters
					la a0 v
					li a1 6
					li a2 5
 
					#Execute function
					jal ra AddValue

					#End
					li a7, 10
					ecall

	AddValue:		li t0, 0 	#Temporal value to loop through integer array 
					mv t1, a0	#This is done in order to not modify original arguments

	loop1:			bgt t0 a1 endFunction	#If t0 > a1 go to endFunction
    				lw t2, 0(t1)			#Load value in array in t2
                    add t2, t2, a2			#Add t2 + a2 and store it in t2
                    sw t2, 0(t1)			#Store t2 into t1
                    addi t0, t0, 1			
                    addi t1, t1, 4
                    j loop1
    
    endFunction:	jr ra