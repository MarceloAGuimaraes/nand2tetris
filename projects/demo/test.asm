// D: Data register
// A: Address / data register
// M: The currently selected memory register, M = RAM[A]
// D = 10
// Set the memory
// @10
// D=A
//D++
// D=D + 1
//D=RAM[17]
// @17
// D=M
// RAM[17]=D
// @17
// M=D
// Computes: RAM[2] = RAM[0] + RAM[1]
// Usage: put values in RAM[0], RAM[1]
// @0
// D=M
// @1
// D=D+M
// @2
// M=D
// Add up two numbers
// RAM[2] = RAM[0] + RAM[1]
@R0
D=M
@R1
D=M+D
@R2
M=D
@15
D=A
@THIS
M=D
// ADD R1, R2, R3

