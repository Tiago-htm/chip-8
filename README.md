# chip-8

Um emulador CHIP-8 escrito em Python com pygame.

---

## Como funciona o chip-8:

O CHIP-8 funciona como um autômato — ele lê uma sequência de instruções (tokens) e as consome uma a uma.

Imagine que ele aceita a linguagem `(a + b)*`. Se recebe `aaabbb`, ele processa token a token sem problema. Se recebe `aaabccc`, no caso o token 'c', ele não é reconhecido por esta máquina por esse motivo não é uma cadeia reconhecida.

Aqui é a mesma coisa: a ROM é a cadeia de entrada, e o emulador consome instrução por instrução até acabar.

---

### Como rodar
pip install pygame
python main.py

### Configuração do chip-8

memory    = bytearray(4096)   # 4KB de memória
registers = bytearray(16)     # 16 registradores de uso geral (V0–VF)
display   = bytearray(64*32)  # Tela de 64x32 pixels (1 bit por pixel)

### Instruções implementadas:

00E0 → limpa a tela
00EE → retorna da sub-rotina
1NNN → faz um salto para NNN
2NNN → chama sub-rotina em NNN
6XNN → carrega NN em VX
7XNN → soma NN a VX
ANNN → carrega NNN em I
DXYN → desenha sprite


#### Referencias:
https://tobiasvl.github.io/blog/write-a-chip-8-emulator/#instructions

