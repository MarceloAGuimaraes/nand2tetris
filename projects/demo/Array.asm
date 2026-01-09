@KBD
D=M
(LOOP)
	// if (i==n) goto END
	@i
	// Pegue o valor que tenho no registro de memória @i e coloque em D
	D=M
	@n
	// Pegue o valor que tenho no registro de memória @n e coloque D=@i - @n
	D=D-M
	@END
	// Pule para o bloco END se D==0
	D;JEQ
	
	// RAM[arr+i] == -1

	@arr
	// Pegue o valor que tenho no registro de memória @arr e coloque em D
	D=M
	@i
	// O registro de memória será o valor que tenho em @arr somado com o valor que está no registro de memório @i
	// seria a mesma coisa que dizer: @D+M (acesse o registro de memória D+M)
	A=D+M
	// Set o registro de memória para -1
	M=-1

	//i++
	@i
	M=M+1
	
	@LOOP
	0;JMP
	
(END)
	@END
	0;JMP
