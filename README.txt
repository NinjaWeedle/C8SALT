C8SALT - A CHIP-8 interpreter written in TI-BASIC for the TI-83+ & TI-84+.
By Oxiti8

Installation:
1. Send C8SALT.8xp and C8CPU.8xp to your calculator.
2. There's no rom loader yet, so just run C8SALT.

WARNING: IF YOU HAVE XLib OR CELTIC III INSTALLED, YOU MUST DISABLE THEM TO RUN C8SALT!
This is because C8SALT uses the Real( command, which XLib uses.

P = PC
I = i
C = op1
D = op2
G = Dummy 1
H = Dummy 2
E = Dummy 3
F = Dummy 4
Q = Delay Timer
R = Return
S = Sound timer 

Opcodes currently implemented:

00E0: Clear Display
00EE: Return from Subroutine Call
00FD: Stop emulation and exit the emulator
1NNN: Jump to 
2NNN: Call Subroutine (Same as 1NNN but you put the current PC in the stack
3XNN: Skip if VX = NN
4XNN: Skip if VX != NN
5XY0: Skip if VX = VY.
CXKK: VX = rand AND kk
DXYN: Draw Sprite at VX, VY

Programmed by Oxiti8 2021.