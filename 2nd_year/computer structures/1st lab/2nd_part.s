.data
 	password: .string "buenosdias"
    alphabet: .string "abcdefghijklmnopqrstuvwxyz"

.text 
	main:		
    		la a1 password
            
            li a2 'a'
            li a6 'z'
            
    		jal ra study_energy		#Invoke
            li a7 10				#End Program (with syscall 10)
            ecall
            
    study_energy:	
    		#Store the string on memory
    		#addi sp, sp, - 4 # space is left to store a string.
          	#sb t0, 0(sp)
          	#sb zero, 1(sp)
            
            rdcycle t1				#The cycles executed up to now are obtained
			#mv a2 sp				#Prepare the argument for string compare
            jal ra string_compare	#Call string_compare (password, possible_key)
            rdcycle t2				#Get cycles executed so far
            sub t1 t2 t1 			#t1: number of cycles consumed
            
            #Print the number of cycles executed
            mv a0 t1
            li a7 1
            ecall
            
            bne a2 a6 conditional
			j end_ener
                
    conditional:
    		#Change to the next character
            addi a2 a2 1
            la a1 password
            #Change stack pointer to rewrite the previous letter
            j study_energy

	string_compare:	
    		beq a1, zero, error				#If a string is empty go to error
            beq a2, zero, error

	loop:	#Load strings in Temporary Int Registers
            lb t4, 0(a1)
            mv t0 a2

            #Pass to the next char
            addi a1, a1, 1
            #addi a2, a2, 1

            #Check if the current chars are different
            bne t0, t4, not_equal

            #If the current chars are equal and are the zero (the end)
            bne t0, zero, loop
            li a1, 1						#If it's equal to 0 result = 1
            j end

	error:								#If a string is empty, return -1
            li a0, -1
            j end

    not_equal:
            li a0, 0						#If it's not equal result = 0

    end:
            jr ra							#Return to Main (exit fuction/subroutine)a'
            
    end_ener:
            li a7 10				#End Program (with syscall 10)
            ecall