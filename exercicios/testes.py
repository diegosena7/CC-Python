def fat(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat


print(fat(5))


def test_fat():
    assert fat(5) == 120

