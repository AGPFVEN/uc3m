.data
	v: .word 7, 8, 3, 4, 5, 6 #Given in the exercise

.text
	main:
    	addi sp, sp, 4
        sw ra, 0(sp)	#no entiendo por que hay un 4 y no un -4
        
        la 	a0, v		#Load word in a0
        li 	a1, 6		#load number of ints in v in a1
        li 	a2, 5		#load 5 in a2 (5 is given in the exercise)
        jal ra, AddValue#Execute AddValue
        
        li t0, 0		#Reset counter
        mv t1, a0		#Work with t1 instead of a0
	
    loop2:
    	bgt	t0, a1, end2
        lw 	a0, 0(t1)
        li 	a7, 1
        ecall
        
        addi t0, t0, 1
        addi t1, t1, 4
        j 	 loop2
    
    end2:
    	lw 	 ra, 0(sp)
        addi sp, sp, 4
        
        li   a7, 10
        ecall
        jr ra
    
    AddValue:
    	li t0, 0			#Counter
        mv t1, a0			#Work with t1 instead of a0
        
    loop:
    	bge  t0, a1, end	#If t0 > a1 go to end (> because there's always a 0 in the end of the word
        lw   t2, 0(t1)		#Load first value of t1 in t2
        add t2, t2, a2		#t2 = t2 + a2
        sw 	 t2, 0(t1)		#Save t2 in first space of t1
        addi t0, t0, 1		#Add 1 to counter
        addi t1, t1, 4		#Add 4 to t1 (adress) to change the number
        j 	 loop			#Go to loop
    
    end:
    	jr ra