.data
	A: .string "Te1"
    B: .string "Te"

.text
main:
    #string_compare(A, B)    
    la a0 A					#Argument A
    la a1 B 				#Argument B
    jal ra string_compare 	#Invoke        

string_compare:
    #------------Question------------------- dentro de string compare
    #Do the solution of the problem of the exercise (-1 result) has to be inside
    #of the subroutine or can it be tested before entering the subroutine

    #Load strings in Temporary Int Registers
    lb t0, 0(a0)
    lb t1, 0(a1)
        
    #Pass to the next char
    addi a0, a0, 1
    addi a1, a1, 1
        
    #Check if the current chars are different
    bne t0, t1, not_equal
        
    #If the current chars are equal and are the zero (the end)
    bne t0, zero, string_compare
    li a0, 1						#If it's equal to 0 result = 1
    j end
    

not_equal:
    li a0, 0						#If it's not equal result = 0
    
end:
    #Why can't I use need t break the loop using syscall 10 (exit)
    jr ra #-------------here-------------

    #Print result
    #li  a7, 1
    #ecall