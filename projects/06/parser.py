from code import Code


class Parser:
    SYMBOL = "@"
    LABEL_PREFIX = "("
    LABEL_SUFFIX = ")"
    JUMP = ";j"
    COMMENT_SYMBOL = "//"

    def __init__(self, file_path):
        self.raw_lines = []
        self.parsed_lines = []
        self.current_line = None
        self.code = Code()
        with open(file_path, "r") as file:
            for line in file.readlines():
                comments_index = line.find(self.COMMENT_SYMBOL)
                if comments_index != -1:
                    line = line[:comments_index]
                line = line.strip()
                if line:
                    self.raw_lines.append(line)
        self.translate(file_path)

    def hasMoreCommands(self):
        return self.current_line < len(self.raw_lines)

    def advance(self):
        self.current_line += 1

    def commandType(self, command):
        downcased_command = command.lower()
        if downcased_command.startswith(self.SYMBOL):
            return "A_COMMAND"
        elif downcased_command.startswith(
            self.LABEL_PREFIX
        ) and downcased_command.endswith(self.LABEL_SUFFIX):
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def symbol(self, command):
        match self.commandType(command):
            case "A_COMMAND":
                return command.removeprefix(self.SYMBOL)
            case "L_COMMAND":
                return command.removeprefix(self.LABEL_PREFIX).removesuffix(
                    self.LABEL_SUFFIX
                )
            case _:
                return None

    def translate(self, file_path):
        self.translated_lines = []
        self.current_line = 0
        self.allocate_labels()
        while self.hasMoreCommands():
            binary_instruction = self.translate_instruction()
            if binary_instruction is not None:
                self.translated_lines.append(binary_instruction)
            self.advance()

        self.generate_hack_file(file_path)

    def generate_hack_file(self, file_path):
        hack_file_path = file_path.replace(".asm", ".hack")
        with open(hack_file_path, "w") as output:
            output.write("\n".join(self.translated_lines))

    def current_command(self):
        return self.raw_lines[self.current_line].strip()

    def translate_instruction(self):
        command = self.current_command()
        match self.commandType(command):
            case "A_COMMAND":
                return self.code.translate_a_instruction(self.symbol(command))
            case "C_COMMAND":
                return self.code.translate_c_instruction(command)

    def allocate_labels(self):
        command_index = 0
        label_indexes = []
        for index, raw_line in enumerate(self.raw_lines):
            if self.commandType(raw_line) == "L_COMMAND":
                self.code.translate_l_instruction(self.symbol(raw_line), command_index)
                label_indexes.append(index)
            else:
                command_index += 1
