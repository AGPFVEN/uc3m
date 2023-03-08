.data
  a: .word 5
  b: .word 7
  c: .word 9

.text
	main:	la t0, a
    		lw a0, 0(t0)
            la t0, b
            lw a1, 0(t0)
			la t0, c
            lw a2, 0(t0)
            jal ra func
            li a7, 1
            ecall
            li a7, 10
            ecall
            
#This is not part of the excirse but i did it mostly for compilation acceptance
    func:	li t0, 0
    		add t0, a0, a1
            add t0, t0, a2
            mv a0, t0
            jr ra
            