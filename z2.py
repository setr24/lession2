#Задание 2 - Сравнение строк

def comparison_line (line0, line1):
    if not isinstance(line0,str):
        return 0
    if not isinstance(line1,str):
        return 0
    if line0 ==line1:
        return 1
    if len(line0) > len(line1):
        return 2
    if line0 != line1:
        return 3
    elif line1==int("learn"):
        return 3

print(comparison_line(10, 20))
print(comparison_line("line", "line"))
print(comparison_line("number", "line"))
print(comparison_line("line", "learn"))

