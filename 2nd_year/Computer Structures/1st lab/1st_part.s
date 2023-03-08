.data
	A: .string "Te1"
    B: .string "Te1"

.text
main:
    #string_compare(A, B)    
    la a0 A					#Argument A
    la a1 B 				#Argument B
    jal ra string_compare 	#Invoke
    li a7, 10				#End Program (with syscall 10)
    ecall

string_compare:
    beq a0, zero, error				#If a string is empty go to error
    beq a1, zero, error
    
loop:
    #Load strings in Temporary Int Registers
    lb t0, 0(a0)
    lb t1, 0(a1)
        
    #Pass to the next char
    addi a0, a0, 1
    addi a1, a1, 1
        
    #Check if the current chars are different
    bne t0, t1, not_equal
        
    #If the current chars are equal and are the zero (the end)
    bne t0, zero, loop
    li a0, 1						#If it's equal to 0 result = 1
    j end

error:								#If a string is empty, return -1
	li a0, -1
    j end

not_equal:
    li a0, 0						#If it's not equal result = 0
    
end:
    jr ra							#Return to Main (exit fuction/subroutine)