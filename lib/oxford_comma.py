def oxford_comma(items):
    if len(items) >= 2:
        items[-1] = f'and {items[-1]}'
        return " ".join(items) if len(items) == 2 else ", ".join(items)
    else:
        return str(items[0])
