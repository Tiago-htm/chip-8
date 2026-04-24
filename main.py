
def main:
    memoria = bytearray(4096)
    registradores = bytearray(16)
    posicaoMemoria  = 0
    PC = 0x200
    display = bytearray(64 * 32)
    pilha = []




    while True:

       
        opcode = (memoria[PC] << 8) | memoria[PC + 1]
        PC += 2
       
        if opcode == 0x00E0:
            for i in range(len(display)):
                display[i] = 0


        if opcode & 0xF000 == 0x1000:
            nnn = opcode & 0X0FFF
            PC  = nnn

        if opcode == 0x00EE:
            PC = pilha.pop()
        
        if opcode & 0xF000 == 0x2000:
            nnn = opcode & 0x0FFF
            pilha.append(PC)
            PC = nnn

        if opcode &  0xF000 == 0x6000:
            vx = (opcode & 0xF00) >> 8
            nnn = opcode & 0x0FF
            registradores[vx] = nnn

        if opcode & 0xF000 == 0x7000:
             vx = (opcode & 0xF00) >> 8
             nnn = opcode & 0x0FF
             registradores[vx] = registradores[vx] + nnn

        if opcode & 0xF000 == 0xA000:
             nnn = opcode & 0x0FFF
             I = nnn

                


        
 
        
