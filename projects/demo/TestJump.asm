@R0
D=M
@ZEROED
D;JEQ // if D == 0 goto (ZEROED)

@R1
M=M+D
@FINAL
0;JMP


(ZEROED)
@R15
D=M
@30
D=D+A
@R1
M=D
(FINAL)
// Computes: If R[0] == 0 R[1] = R[15] + 30 else R[1] = R[1] + R[0]
