def get_j_k_encoding(start: bool, end: bool):
    if not start and not end:
        return {"j": False, "k": None}
    elif not start and end:
        return {"j": True, "k": None}
    elif start and end:
        return {"j": None, "k": False}
    else:
        return {"j": None, "k": True}


class TableElement:
    def __init__(self, value: int, mod: int):
        self.value = value
        self.next_value = (value + 1) % mod
        self.amount_bits = (mod - 1).bit_length()
        self.flipflops = self.get_flipflops()

    def get_flipflops(self):
        flipflops = []
        for i in range(self.amount_bits):
            get_bit = 1 << i
            flipflops.append(get_j_k_encoding((get_bit & self.value) != 0, (get_bit & self.next_value) != 0))
        return flipflops

    def to_list(self):
        buffer = [self.value, self.next_value]
        for i in self.flipflops:
            if i["j"] is None:
                buffer.append("X")
            else:
                buffer.append(i["j"])

            if i["k"] is None:
                buffer.append("X")
            else:
                buffer.append(i["k"])
        return buffer
