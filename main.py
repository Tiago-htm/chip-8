import sys
import pygame


def renderDisplay(screen, display, drawingTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    for y in range(32):
        for x in range(64):
            if display[x + y * 64] == 1:
                pygame.draw.rect(
                    screen,
                    (0, 0, 200),
                    (x * 5, y * 5, 5, 5),
                )

    pygame.display.flip()

    drawingTime.tick(1)


def main():
    memory = bytearray(4096)
    registers = bytearray(16)
    PC = 0x200
    display = bytearray(64 * 32)
    stack = []
    I = 0

    pygame.init()
    screen = pygame.display.set_mode((320, 160))
    pygame.display.set_caption("chip-8")
    drawingTime = pygame.time.Clock()

    try:
        with open("logo.ch8", "rb") as rom:
            romData = rom.read()
            for i in range(len(romData)):
                memory[0x200 + i] = romData[i]
    except FileNotFoundError:
        print("Arquivo de ROM não encontrado.")
        sys.exit(1)

    while True:
        opcode = (memory[PC] << 8) | memory[PC + 1]
        PC += 2
        nnn = opcode & 0x0FFF
        nn = opcode & 0x00FF
        n = opcode & 0x000F
        vx = (opcode & 0x0F00) >> 8
        vy = (opcode & 0x00F0) >> 4
        vf = (opcode & 0xF000) >> 12
        posX = registers[vx] % 64
        posY = registers[vy] % 32

        match vf:
            case 0x0:
                match nn:
                    case 0xE0:
                        for i in range(len(display)):
                            display[i] = 0
                    case 0xEE:
                        PC = stack.pop()
                    case _:
                        print(f"token não implementado: {vf:#04x}")

            case 0x1:
                PC = nnn
            case 0x2:
                stack.append(PC)
                PC = nnn
            case 0x6:
                vx = (opcode & 0xF00) >> 8
                registers[vx] = nn
            case 0x7:
                registers[vx] = registers[vx] + nn
            case 0xA:
                I = nnn

            case 0xD:
                for row in range(n):
                    byte = memory[I + row]
                    if (posY + row) >= 32:
                        break
                    for bit in range(8):
                        if (posX + bit) >= 64:
                            break
                        posDisplay = (posX + bit) + (posY + row) * 64
                        if byte & (0x80 >> bit):
                            if display[posDisplay] == 1:
                                registers[0xF] = 1
                                display[posDisplay] = 0
                            else:
                                display[posDisplay] = 1
            case _:
                print(f"token não implementado: {vf:#04x}")

        renderDisplay(screen, display, drawingTime)


if __name__ == "__main__":
    main()
