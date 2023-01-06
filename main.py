import pydatatable
from table_element import *
from int_as_binary import IntAsBinary


def get_terms_for_flipflop(index: int, data: list[TableElement]):
    must_js = []
    must_ks = []
    maybe_js = []
    maybe_ks = []
    digits = data[-1].value.bit_length()
    for i in data:
        flipflop = i.flipflops[index]
        if flipflop["j"]:
            must_js.append(IntAsBinary(i.value, digits=digits))
        elif flipflop["j"] is None:
            maybe_js.append(IntAsBinary(i.value, digits=digits))
        if flipflop["k"]:
            must_ks.append(IntAsBinary(i.value, digits=digits))
        elif flipflop["k"] is None:
            maybe_ks.append(IntAsBinary(i.value, digits=digits))
    return {"j": (must_js, maybe_js), "k": (must_ks, maybe_ks)}


def main():
    mod_counter = int(input("Please enter your mod counter: "))
    table = [TableElement(i, mod_counter) for i in range(mod_counter)]

    counter = pydatatable.Table(location='counter', title=f'mod {mod_counter} counter')
    data = [i.to_list() for i in table]
    js = [f"J{i}" for i in range((mod_counter - 1).bit_length())]
    ks = [f"K{i}" for i in range((mod_counter - 1).bit_length())]
    title = ["x", "x\'"]
    for i, v in enumerate(js):
        title.append(v)
        title.append(ks[i])
    counter.add_data(data, title)

    next_terms = []
    must_js, maybe_js = get_terms_for_flipflop(0, table)["j"]
    must_ks, maybe_ks = get_terms_for_flipflop(0, table)["k"]
    combined_js = must_js + maybe_js
    minimized_list = [False] * len(combined_js)
    for i, v in enumerate(combined_js):
        if i != len(combined_js):
            for j, j_v in enumerate(combined_js[i + 1:]):
                buffer = v.minimize(j_v)
                if buffer is not None:
                    next_terms.append(buffer)
                    minimized_list[i] = True
                    minimized_list[j + i + 1] = True
        if not minimized_list[i]:
            next_terms.append(v)
    pass


if __name__ == "__main__":
    main()
