Oxiti8's                 _
CCC  8 8  SSS  AAA      T T 
C    888   S   AAA  LLL TTT
CCC  8 8  SSS  A        T_T

C8SALT - A CHIP-8 emulator written in TI-BASIC for the TI-83+, TI-84+, TI-84+ C Silver Edition, and TI-84+ CE.
By Oxiti8

ALPHA VERSION V0.8

C8SALT is the first ever TI-BASIC CHIP-8 emulator. Play all your favorite CHIP-8 games at a blistering 0.1 FPS!
5 games are included with C8SALT, along with a ROM converter written in Python 3 allowing you to play any CHIP-8 game with C8SALT.
You can even import your own custom fonts!

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
	3 - SETTINGS: From here, you can enable and disable HLE Text Rendering (0 = on, 1 = off). It is recommended that CSE/CE users leave HLE text rendering disabled.
	4 - EXIT: Exits C8SALT.

WARNING: IF YOU HAVE XLib OR CELTIC III INSTALLED, YOU MUST DISABLE THEM TO RUN C8SALT!
This is because C8SALT uses the Real( command as part of its memory decompression routine, a command which XLib uses for its functions. 

You can find already converted ROM.8xl files to send to your calculator in the "Programs" folder, or if you want to import your own, refer to Section II.


II. ROM CONVERSION INSTRUCTIONS:

 1. Put your CHIP-8 program in the "Programs" folder, or in the same place as convert.py.
 2. Rename your CHIP-8 program "program.ch8"
 3. Run convert.py. It should create a file named "ROM.txt".

 For the following steps, you have two options based on the tool you want to use:

 FOR TI-CONNECT USERS (Recommended):
  4. Open TI-Connect, and open "TI DataEditor".
  5. Go to File > Import... and import your "ROM.txt" file.
  6. Click File -> Save As... and save the list as "ROM.8xl".
  7. Send the ROM.8xl file to your calculator.

 FOR SOURCECODER 3 USERS:
  4. Convert the ROM.txt file to the comma delimited .csv format. This can be done thru Microsoft Excel or whatever spreadsheet editor you have available.
  5. Go to https://www.cemetech.net/sc/ and open your ROM.csv file. It should show up in SourceCoder 3 as "|LROM".
  6. Rename the file from "|LROM" to "ROM".
  7. Click "Export File". It should export as "ROM.8xl".
  8. Send ROM.8xl to your calculator.

 Now you can run C8SALT, and you should now be able to play your game!

 (You can also create custom fonts this way by saving the hex data for them in a .ch8 file, then following the program conversion process- just rename the "ROM.8xl" to "FONT.8xl" when finished)


III. CONTROLS (Note- Due to emulation speed you may need to mash the keys for them to register.):

 MODE - Quit C8SALT, clean up lists used during emulation, and display debug info.
 
Controls are unique in that the keys used are the GetKey value modulo 16.

IV. TECHNICAL INFO

 All 30 ops from the original CHIP-8 spec are planned to be supported, as well as select SuperCHIP ops.
 Obviously, there's no audio support.

 - On the limited SuperCHIP support:

 You can use 00FD (EXIT), 00FE (LORES), and Fx30 (BIGFONT VX) just fine.
 SuperCHIP Hires mode (00FF) can also be used, but you're limited to a 94x62 resolution when using it rather than the full 128x64.

 DXY0, 00Cn(SCD n), 00FB (SCR), 00FC (SCL), FX75, and FX85 are not supported.


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
Q = Delay Timer
R = Return value
S = Sound timer 
L = Screen height
W = Screen width
Theta = HLE Font Toggle
Recursive n = temp var.


VI. CREDITS

Programmed by Oxiti8.
Rom importer created by A-KouZ1.

Special thanks to Mr Womp Womp, kg583, and calc84maniac, and fghsgh for help with memory compression and optimization. C8SALT wouldn't exist without them.

VII. LICENSE

Copyright 2021-2022 Oxiti8

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.