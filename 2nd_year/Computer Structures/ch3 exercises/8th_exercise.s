.data
    str: .string "Hello"    
.text
            main:	la a0, str
					jal ra Vowels
                    li a7, 1
                    ecall
                    li a7, 10
                    ecall
                    
          Vowels:	mv t0, a0
                    li t1, 0
                    li t3, 'a'

            loop1:	lb t2, 0(t0)
                    beq t2, zero, end
                    bne t2, t3, not_a
                    addi t1, t1, 1
            not_a:  addi t0, t0, 1
                    j loop1

              end:	bne t0, a0, skip_zero_case
                    li t1, -1
          	
    skip_zero_case:	mv a0 t1
    				jr ra