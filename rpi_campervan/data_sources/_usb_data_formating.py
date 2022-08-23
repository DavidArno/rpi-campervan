def _split_as_strings(item : bytes) -> tuple[str, str]:
    (name_bytes, value_bytes) = item.split(b'\t')
    return (name_bytes.decode("utf-8"), value_bytes.decode("utf-8"))

def tab_list_to_dictionary(tab_list : list[bytes]) -> dict[str, str]:
    dict = {}
    for item in tab_list:
        (name, value) = _split_as_strings(item)
        dict[name] = value

    return dict