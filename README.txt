Oxiti8's                 _
CCC  8 8  SSS  AAA      T T 
C    888   S   AAA  LLL TTT
CCC  8 8  SSS  A        T_T

C8SALT - A CHIP-8 emulator written in TI-BASIC for the TI-83+, TI-84+, TI-84+ C Silver Edition, and TI-84+ CE.
By Oxiti8

VERSION V1.1

C8SALT is the first ever TI-BASIC CHIP-8 emulator. Play all your favorite CHIP-8 games (as well as some SCHIP games) at a blistering 0.2 FPS!
9 programs are included with C8SALT, along with a ROM converter written in Python 3 allowing you to use your own CHIP-8 games with C8SALT.
You can even import your own custom fonts! V1.1 makes optimizations and fixes a bug with VIP style Load/Save.

*TABLE OF CONTENTS*

 I. INSTALLATION
 II. ROM CONVERSION INSTRUCTIONS
 III. CONTROLS
 IV. TECHNICAL DETAILS
 V. VARIABLE GUIDE
 VI. CREDITS
 VII. LICENSE

I. INSTALLATION:
 1. Send C8SALT.8xp, FONT.8xl, and C8CPU.8xp to your calculator.
 2. Select an option from the menu:
	1 - RESUME: If you pressed ON to stop C8SALT mid-execution and you haven't cleared the graph screen, you can select this option to pick up where you left off.
	2 - LOAD FROM LROM: Loads the rom data stored in ROM. For info on converting CHIP-8 software for use with C8SALT, see ROM CONVERSION INSTRUCTIONS.
	3 - SETTINGS: From here, you can enable and disable HLE Text Rendering (0 = on, 1 = off) as well as decide the behavior of FX55/65 (0 = Do not increment I (SCHIP style), 1 = Increment I (VIP/Octo style)), and set the shift quirk for 8XY6/8XYE (0 = SCHIP style (default), 1 = VIP/Octo style).
	4 - CLEAR RPL DATA: Selecting this option clears the RPL flags that FX75/FX85 use.
	5 - EXIT: Exits C8SALT.

 WARNING: IF YOU HAVE XLib OR CELTIC III INSTALLED, YOU MUST DISABLE THEM TO RUN C8SALT!
 This is because C8SALT uses the Real( command as part of its memory decompression routine, a command which XLib uses for its functions. 

 You can find preconverted ROM.8xl files to send to your calculator in the "Programs" folder, or if you want to import your own, refer to Section II.


II. ROM CONVERSION INSTRUCTIONS:

 1. Open the "Programs" folder.
 2. Drag and drop your CHIP-8 program binary(Generally a .ch8 or .sc8 file) onto convert.py. It should output a file named "ROM.txt".

 For the following steps, you have two options based on the tool you want to use:

 FOR TI-CONNECT USERS (Recommended):
  3. Open TI-Connect, and open "TI DataEditor".
  4. Go to File > Import... and import your "ROM.txt" file.
  5. Click File -> Save As... and save the list as "ROM.8xl".
  6. Send the ROM.8xl file to your calculator.

 FOR SOURCECODER 3 USERS:
  3. Convert the ROM.txt file to the comma delimited .csv format. This can be done thru Microsoft Excel or whatever spreadsheet editor you have available.
  4. Go to https://www.cemetech.net/sc/ and open your ROM.csv file. It should show up in SourceCoder 3 as "|LROM".
  5. Rename the file from "|LROM" to "ROM".
  6. Click "Export File". It should export as "ROM.8xl".
  7. Send ROM.8xl to your calculator.

 Now you can run C8SALT, and you should now be able to play your game!

 (You can also create custom fonts this way by saving the hex data for them in a .ch8 file, then following the program conversion process- just rename the resulting "ROM.8xl" file to "FONT.8xl" when finished)


III. CONTROLS (Note- Due to emulation speed you may need to mash the keys for them to register.):

 MODE - Quit C8SALT, clean up lists used during emulation, and display debug info.

 The controls for the keypad are the same as Vinegar:

 Chip-8
 1	2	3	C
 4	5	6	D
 7	8	9	E
 A	0	B	F

 TI-83+
 7	8	9	×
 4	5	6	-
 1	2	3	+
 0	.	(-)	Enter
 
 You can also use the arrow keys in place of 2, 4, 5, and 6.


IV. TECHNICAL INFO

 All 30 ops from the original CHIP-8 spec are supported, as well as select SuperCHIP ops.
 Obviously, there's no audio support.

 - On the limited SuperCHIP support:

 You can use 00FD (EXIT), 00FE (LORES), Fx30 (BIGFONT VX), Fx75 (LD R, Vx), and Fx85 (LD Vx, R) just fine.
 SuperCHIP 128x64 mode (00FF) can also be used, but on the monochrome calculators you're limited to a 92x62 resolution when using it rather than the full 128x64 and as such errors can and will occur.
 - On the CSE and CE though, you can use the full 128x64 resolution.

 DXY0, 00Cn(SCD n), 00FB (SCR), and 00FC (SCL) are not supported.

 C8SALT uses the list "RPL" for Fx75 and Fx85, and this list is not deleted/cleared upon exiting or starting C8SALT.
 - This means that one can use the "RPL flags" as a form of persistent data storage like on the HP48.
 - Fx75 and Fx85 also support up to 16 entries as outlined in the XO-CHIP 1.1 spec instead of just the original 8.

 Rom data is stored in a list, with 4 bytes being stored per list entry:
  0.001002003004
 C8SALT loads this ROM into list RAM, which itself stores 8 bytes per list entry:
  .001002003004+i.005006007008


V. VARIABLE GUIDE

A = temp
B = temp
P = Program Counter (PC)
I = instruction pointer (i)
C = op1 (Byte 1 of the opcode) 
D = op2 (Byte 2 of the opcode)
G = Dummy 1 (Sometimes used as a temp for Vx)
H = Dummy 2 (Sometimes used as a temp for Vy)
E = Dummy 3
F = Dummy 4
J = Increment I during FX55/65 flag
K = getkey
L = Screen height
M = Shift Quirk Flag
N = Temp
Q = Delay Timer
R = Return value
S = Sound timer 
W = Screen width
Z = Temp
Theta = HLE Font Toggle
Recursive n = temp var.

VI. CREDITS

Programmed by Oxiti8.
Rom importer created by A-KouZ1, modified by Oxiti8.

Special thanks to Mr Womp Womp, kg583, and calc84maniac, LogicalJoe, and fghsgh for help with memory compression and optimization. C8SALT wouldn't exist without them.

VII. LICENSE

Copyright 2021-2022 Oxiti8

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.