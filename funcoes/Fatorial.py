def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat


fatorial(5)


def test_fat():
    assert fatorial(5) == 120
