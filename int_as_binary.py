class IntAsBinary:
    def __init__(self, value: int = None, binary: list[bool | None] = None, digits: int = None):
        test = digits is None
        if (digits is None) and (value is not None):
            digits = value.bit_length()
        elif digits is None:
            digits = len(binary)
        if value is not None:
            self.value = value
            self.binary = [((1 << i) & value) != 0 for i in range(value.bit_length())] + ([False] * (digits - value.bit_length()))
        elif binary is not None:
            self.binary = binary + ([False] * (digits - len(binary)))
            if None in binary:
                self.value = None
            else:
                self.value = sum([(1 << i) for i in binary if i])

    def minimize(self, other):
        new = IntAsBinary(binary=self.binary)
        has_changed = False
        for i, v in enumerate(self.binary):
            if v != other.binary[i] and (v is not None) and (other.binary[i]) is not None:
                if not has_changed:
                    new.binary[i] = None
                    has_changed = True
                else:
                    return None
        if has_changed:
            return new
        if self.binary.count(None) > other.binary.count(None):
            return self
        return other

    def __eq__(self, other):
        for i, v in enumerate(self.binary):
            if v != other.binary[i]:
                return False
        return True


