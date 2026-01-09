@0
D=A
@index
M=D
@sum
M=D

(LOOP)
@index
D=M+1
M=D
@sum
M=M+D
@R0
D=M-D
@LOOP
D;JGT
