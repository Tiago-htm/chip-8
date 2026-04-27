def main():
    memoria = bytearray(4096)
    registradores = bytearray(16)
    posicaoMemoria = 0
    PC = 0x200
    display = bytearray(64 * 32)
    pilha = []
    I = 0

    while True:
        opcode = (memoria[PC] << 8) | memoria[PC + 1]
        PC += 2
        nnn = opcode & 0x0FFF
        nn = opcode & 0x00FF
        n = opcode & 0x000F
        vx = (opcode & 0x0F00) >> 8
        vy = (opcode & 0x00F0) >> 4
        vf = 0

        if opcode == 0x00E0:
            for i in range(len(display)):
                display[i] = 0

        if opcode & 0xF000 == 0x1000:
            PC = nnn

        if opcode == 0x00EE:
            PC = pilha.pop()

        if opcode & 0xF000 == 0x2000:
            pilha.append(PC)
            PC = nnn

        if opcode & 0xF000 == 0x6000:
            vx = (opcode & 0xF00) >> 8
            registradores[vx] = nn

        if opcode & 0xF000 == 0x7000:
            registradores[vx] = registradores[vx] + nn

        if opcode & 0xF000 == 0xA000:
            I = nnn

        posX = registradores[vx] % 64
        posY = registradores[vy] % 32

        if opcode & 0xF000 == 0xD000:
            for linha in range(n):
                byte = memoria[I + linha]
                if (posY + linha) >= 32:
                    break
                for bit in range(8):
                    if (posX + bit) >= 64:
                        break
                    posDisplay = (posX + bit) + (posY + linha) * 64
                    if byte & (0x80 >> bit):
                        if display[posDisplay] == 1:
                            registradores[0xF] = 1
                            display[posDisplay] = 0
                        else:
                            display[posDisplay] = 1
