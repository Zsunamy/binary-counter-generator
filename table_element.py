def get_j_k_encoding(start: bool, end: bool) -> dict:
    if not start and not end:
        return {"j": False, "k": None}
    elif not start and end:
        return {"j": True, "k": None}
    elif start and end:
        return {"j": None, "k": False}
    else:
        return {"j": None, "k": True}


# def get_j_k_encoding(start, end):
#    if start and not end:
#        return {"T": 1}
#    elif start and end:
#        return {"T": 0}
#    elif not start and end:
#        return {"T": 1}
#    else:
#        return {"T": 0}


class TableElement:
    def __init__(self, value: int, mod: int) -> None:
        self.value: int = value
        self.next_value: int = (value + 1) % mod
        self.amount_bits: int = (mod - 1).bit_length()
        self.flipflops: [dict] = self.get_flipflops()

    def get_flipflops(self) -> [dict]:
        flipflops: [dict] = []
        for i in range(self.amount_bits):
            get_bit = 1 << i
            flipflops.append(get_j_k_encoding((get_bit & self.value) != 0, (get_bit & self.next_value) != 0))
        return flipflops

    def to_list(self) -> [str]:
        buffer: [str] = [self.value, self.next_value]
        for i in self.flipflops:
            buffer.append(i["T"])
        return buffer
