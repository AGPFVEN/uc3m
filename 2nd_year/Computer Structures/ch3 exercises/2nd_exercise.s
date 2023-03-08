.data
	v: .word 7, 8, 3, 4, 5, 6
.text
        main:	la a0, v
                li a1, 6
                li a2, 5

                jal ra AddValue
                
                li t0, 0
                mv t1 a0
                
        loop2:	lw a0, 0(t1)
                li a7, 1
                ecall
                
                bgt t0, a2, end2
                addi t0, t0, 1
                addi t1, t1, 4
                j loop2
                
          end2:	li a7, 10
                ecall
        
  	AddValue:	li t0, 0
    			mv t1 a0
                
    	loop:	lw t2, 0(t1)
            	add t2, t2, a2
                sw t2, 0(t1)
                addi t0, t0, 1
                bgt t0, a2, end
                addi t1, t1, 4
                j loop
            
          end: 	jr ra
