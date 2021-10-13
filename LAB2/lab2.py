def main():
    moduleNo = int(input('Module?: '))
    if moduleNo == 1:
         module1()
    if moduleNo == 2:
         module2()
    if moduleNo == 3:
         module3()
    if moduleNo == 4:
         module4()
    if moduleNo == 5:
         module5()
    if moduleNo == 6:
         module6()

def module1():
    """
    n = 10 => False False
    n = 5 => False False
    n = 20 False True
    n = -5 True False
    """
    n = -5
    result1 = (n < 5)
    result2 = (n >= 20)

    print(result1)
    print(result2)

def module2():
    """
    x = 10 => 5
    x = 15 => 7.5
    x = -2 => -4
    """
    x = 10
    y = 0
    if x < 10:
       y = x*2
    else:
      y = x/2

    print(y)

def module3():
    """
    n = 55 => pos and odd
    n = 2 => pos and even
    n = 0 => neither pos nor neg
    n = -32 => neg
    """
    n = 14
    n_type = ''
    if n > 0:
        if n % 2 == 0:
            n_type = "pos and even"
        else:
            n_type = "pos and odd"
    elif n < 0:
        n_type = "neg"
    else:
        n_type = "neither pos nor neg"

    print(n_type)

def module4():
    """
    x = 10 => 30
    x = 15 => 30
    x = 25 => 40
    """
    x = 4
    y = 0
    if x < 10:
        y = 20
    elif x < 20:
        y = 30
    else:
        y = 40

    print(y)

def module5():
    """
    x = 10 => 30
    x = 15 => 30
    x = 25 => 40
    """

    x = int(input(''))
    y = 0
    if x < 10:
        y = 20
    if x < 20:
        y = 30
    else:
        y = 40
    
    print(y)

    module5()

def module6():
    msg = ''
    height = int(input('What is your height in inches?: '))
    in_limits = ((height >= 55) & (height <= 75))
    if in_limits:
        msg = 'Hooray (height within limits)'
    else:
        msg = 'Oops (height out of limit)'

    print(msg)


if __name__ == '__main__':
    main()