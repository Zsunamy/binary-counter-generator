from int_as_binary import IntAsBinary
from table_element import TableElement


def minimize_batch(terms: [IntAsBinary]) -> ([IntAsBinary], bool):
    no_double_terms: [IntAsBinary] = []
    for i, v in enumerate(terms):
        is_double = False
        for j in range(i + 1, len(terms)):
            if v.__eq__(terms[j]):
                is_double = True
                break
        if not is_double:
            no_double_terms.append(v)

    terms = no_double_terms
    has_changed: bool = False
    new_terms: [IntAsBinary] = []
    is_minimized_list: [bool] = [False] * len(terms)
    for i, v in enumerate(terms):
        for j in range(i + 1, len(terms)):
            buffer = v.minimize(terms[j])
            if buffer is not None:
                new_terms.append(buffer)
                is_minimized_list[i] = True
                is_minimized_list[j] = True
                has_changed = True
        if not is_minimized_list[i]:
            new_terms.append(v)

    return new_terms, has_changed


class Terms:
    def __init__(self, table: [TableElement], index: int, key: str) -> None:
        self.must: [IntAsBinary] = []
        self.maybe: [IntAsBinary] = []
        digits: int = table[-1].value.bit_length()
        for elem in table:
            if elem.flipflops[index][key] is None:
                self.maybe.append(IntAsBinary(elem.value, digits=digits))
            else:
                self.must.append(IntAsBinary(elem.value, digits=digits))

    def get_minimal_terms(self) -> [IntAsBinary]:
        new_batch = self.must + self.maybe
        while True:
            new_batch, has_changed = minimize_batch(new_batch)
            if not has_changed:
                break

        return new_batch
