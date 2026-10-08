// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(INICIO)
	@KBD
	D=A
	@index
	M=D-1
	@KBD
	D=M
	@APAGAR
	D;JEQ
	@DESENHAR
	D;JNE
(APAGAR)
	@index
	A=M
	M=0
	@index
	D=M-1
	M=D
	@SCREEN
	D=D-A
	@APAGAR
	D;JGE
	@INICIO
	D;JLT
(DESENHAR)
	@index
	A=M
	M=-1
	@index
	D=M-1
	M=D
	@SCREEN
	D=D-A
	@DESENHAR
	D;JGE
	@INICIO
	D;JLT


