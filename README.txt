C8SALT - A CHIP-8 interpreter written in TI-BASIC for the TI-83+, TI-84+, TI-84+ C Silver Edition, and TI-84+ CE.
By Oxiti8

Installation:
1. Send C8SALT.8xp and C8CPU.8xp to your calculator.
2. Select an option from the menu:
	1 - NONE: This launches C8SALT with no ROM. Useless.
	2 - CORAX89: This launches Corax89's test ROM.
	3 - LOAD FROM LROM: Loads the rom data stored in ROM. For info on converting CHIP-8 software for use with C8SALT, see the instructions at the bottom of this README.

WARNING: IF YOU HAVE XLib OR CELTIC III INSTALLED, YOU MUST DISABLE THEM TO RUN C8SALT!
This is because C8SALT uses the Real( command, which XLib uses.

You can find already converted ROM.8xl files to send to your calculator in the "Programs" folder,
or if you want to import your own:

ROM CONVERSION INSTRUCTIONS:

1. Put your CHIP-8 program in the "Programs" folder.
2. Name your chip-8 program "program.ch8"
3. Run convert.py. it should create a file named "ROM.txt"

For the following steps, you have two options based on the tool you want to use:

For TI-CONNECT USERS (Recommended):
4. Open TI-Connect, and open "TI DataEditor".
5. Go to File > Import... and import your "ROM.txt" file.
6. Click File -> Save As... and save the list as "ROM.8xl".
7. Send the ROM.8xl file to your calculator.

FOR SOURCECODER 3 USERS:
4. Convert the out.txt file to the comma delimted .csv format. This can be done thru Microsoft Excel or whatever spreadsheet editor you have availiable.
5. Go to https://www.cemetech.net/sc/ and open your ROM.csv file. It should show up in SourceCoder 3 as "|LROM".
6. Rename the file from "|LROM" to "ROM".
7. Click "Export File". It should export as "ROM.8xl".
8. Send ROM.8xl to your calculator.

Now you can run C8SALT, and you should now be able to play your game!


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
L = Screen height
W = Screen width

All 30 ops from the original CHIP-8 spec are planned to be supported,
as well as some limited SuperCHIP support.

 - On the limited SuperCHIP support:

You can use 00FD (EXIT), 00FE (LORES), and eventually FX75/FX85 just fine.
Hires mode (00FF) can also be used, but you're limited to a 96x64 resolution when using it rather than the full 128x64.

DXY0, 00Cn(SCD n), 00FB (SCR), 00FC (SCL), FX75, and FX85 are not supported at this time.
    
Programmed by Oxiti8 (C)2021.
Rom importer created by A-KouZ1.