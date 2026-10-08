from symbol_table import SymbolTable


class Code:
    A_INSTRUCTION_OPCODE = "0"
    C_INSTRUCTION_OPCODE = "1"

    DEST_LOOKUPS = {
        None: "000",  # the value is not stored
        "": "000",  # the value is not stored
        "M": "001",  # RAM[A]
        "D": "010",  # D register
        "DM": "011",  # D register and RAM[A]
        "MD": "011",  # D register and RAM[A]
        "A": "100",  # A register
        "AM": "101",  # A register and RAM[A]
        "AD": "110",  # A register and D register
        "ADM": "111",  # A register, D register, and RAM[A]
        "AMD": "111",  # A register, D register, and RAM[A]
    }

    JUMP_LOOKUPS = {
        None: "000",  # no jump
        "": "000",  # no jump
        "JGT": "001",  # if comp > 0 jump
        "JEQ": "010",  # if comp = 0 jump
        "JGE": "011",  # if comp ≥ 0 jump
        "JLT": "100",  # if comp < 0 jump
        "JNE": "101",  # if comp ≠ 0 jump
        "JLE": "110",  # if comp ≤ 0 jump
        "JMP": "111",  # Unconditional jump
    }

    COMP_LOOKUPS = {
        "0": {"op_code": "0", "comp": "101010"},
        "1": {"op_code": "0", "comp": "111111"},
        "-1": {"op_code": "0", "comp": "111010"},
        "D": {"op_code": "0", "comp": "001100"},
        "A": {"op_code": "0", "comp": "110000"},
        "M": {"op_code": "1", "comp": "110000"},
        "!D": {"op_code": "0", "comp": "001101"},
        "!A": {"op_code": "0", "comp": "110001"},
        "!M": {"op_code": "1", "comp": "110001"},
        "-D": {"op_code": "0", "comp": "001111"},
        "-A": {"op_code": "0", "comp": "110011"},
        "-M": {"op_code": "1", "comp": "110011"},
        "D+1": {"op_code": "0", "comp": "011111"},
        "A+1": {"op_code": "0", "comp": "110111"},
        "M+1": {"op_code": "1", "comp": "110111"},
        "D-1": {"op_code": "0", "comp": "001110"},
        "A-1": {"op_code": "0", "comp": "110010"},
        "M-1": {"op_code": "1", "comp": "110010"},
        "D+A": {"op_code": "0", "comp": "000010"},
        "D+M": {"op_code": "1", "comp": "000010"},
        "D-A": {"op_code": "0", "comp": "010011"},
        "D-M": {"op_code": "1", "comp": "010011"},
        "A-D": {"op_code": "0", "comp": "000111"},
        "M-D": {"op_code": "1", "comp": "000111"},
        "D&A": {"op_code": "0", "comp": "000000"},
        "D&M": {"op_code": "1", "comp": "000000"},
        "D|A": {"op_code": "0", "comp": "010101"},
        "D|M": {"op_code": "1", "comp": "010101"},
    }

    def __init__(self):
        self.symbol_table = SymbolTable()

    def dest(self, instruction):
        dest_index = instruction.find("=")
        if dest_index != -1:
            return instruction[:dest_index]
        else:
            return None

    def jump(self, instruction):
        jump_index = instruction.find(";")
        if jump_index != -1:
            return instruction[(jump_index + 1) :]
        else:
            return None

    def comp(self, instruction):
        comp = instruction
        dest = self.dest(instruction)
        if dest is not None:
            comp = comp.removeprefix(("%s=" % dest))
        jump = self.jump(instruction)
        if jump is not None:
            comp = comp.removesuffix((";%s" % jump))
        return comp

    def translate_a_instruction(self, allocated_at):
        if not allocated_at.isnumeric():
            self.symbol_table.add_entry(allocated_at)
            allocated_at = self.symbol_table.get_address(allocated_at)
        return f"{self.A_INSTRUCTION_OPCODE}{int(allocated_at):015b}"

    def translate_c_instruction(self, instruction):
        dest = self.dest(instruction)
        comp = self.comp(instruction)
        jump = self.jump(instruction)
        dest_translation = self.DEST_LOOKUPS[dest]
        comp_translation = self.COMP_LOOKUPS[comp]
        jump_translation = self.JUMP_LOOKUPS[jump]
        prefix = self.C_INSTRUCTION_OPCODE * 3
        return f"{prefix}{comp_translation['op_code']}{comp_translation['comp']}{dest_translation}{jump_translation}"

    def translate_l_instruction(self, label, line):
        self.symbol_table.add_entry_for_label(label, line)
        return None
