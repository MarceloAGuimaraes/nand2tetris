class SymbolTable:
    BUILT_IN_SYMBOLS = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
    }

    LOWEST_AVAILABLE_ADDRESS = 15
    HIGHEST_AVAILABLE_ADDRESS = 16383

    def __init__(self):
        self.allocations = dict(self.BUILT_IN_SYMBOLS)
        self.tracked_addresses = set(self.allocations.values())

    def add_entry(self, symbol):
        if self.contains(symbol) is not True:
            allocated_at = self.generate_address()
            self.allocations[symbol] = allocated_at
            self.tracked_addresses.add(allocated_at)

    def contains(self, symbol):
        return symbol in self.allocations

    def get_address(self, symbol):
        return self.allocations[symbol]

    def generate_address(self):
        valid_address = None
        for possible_address in range(
            self.LOWEST_AVAILABLE_ADDRESS, self.HIGHEST_AVAILABLE_ADDRESS + 1
        ):
            if possible_address not in self.tracked_addresses:
                valid_address = possible_address
                break
        return valid_address

    def add_entry_for_label(self, label, address):
        self.allocations[label] = address
