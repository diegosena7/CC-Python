def fizzbuzz(numUsuario):
    if numUsuario % 3 == 0 and not numUsuario % 5 == 0:
        print("Fizz")
    if numUsuario % 5 == 0 and not numUsuario % 3 == 0:
        print("Buzz")
    if numUsuario % 5 == 0 and numUsuario % 3 == 0:
        print("FizzBuzz")
    else:
        return numUsuario


fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
fizzbuzz(4)
