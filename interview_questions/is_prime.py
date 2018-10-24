num = 13


def is_prime(num):
    if num < 2:
        print('False')
    else:
        for i in range(2, num):
            if num % i == 0:
                print('False')
            else:
                print('True')


is_prime(num)
