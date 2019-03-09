def cut_cake(parts):
    try:
        return 1/ int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "вы что с ума посходили"
cake = cut_cake("hghghghgh")
print(cake)