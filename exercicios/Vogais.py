def vogal(n):
    if n in "aeiouAEIOU":
        return True
    else:
        return False


print(vogal('b'))
print(vogal('B'))
print(vogal('a'))
print(vogal('A'))