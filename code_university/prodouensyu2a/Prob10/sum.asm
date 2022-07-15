        addi x2,x0,0x10
        add x3,x0,x0
loop:   lw x4,x3,0
        addi x3,x3,4
        addi x4,x4,1
        sw x4,x3,-4
        bne x3,x2,loop
        ecall x0,x0,x0