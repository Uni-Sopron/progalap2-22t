class NonExistentFileException(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.origin = args[1]

    def __str__(self):
        return f'{self.origin}: {self.message}'


class WrongGuessException(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return f'Sorry your programs just crashed for guessing wrong. Reason: {self.message}'


def guess_the_correct_number_or_else(x):
    try:
        if type(x) != int:
            raise WrongGuessException('not a number')
    except Exception as e:
        print(e)
    else:
        if x == 4:
            return True
        else:
            raise WrongGuessException('wrong guess')


try:
    print(guess_the_correct_number_or_else('egy'))
except Exception as e:
    print(e)
try:
    print(guess_the_correct_number_or_else(1))
except Exception as e:
    print(e)
try:
    print(guess_the_correct_number_or_else(4))
except Exception as e:
    print(e)


# try:
#     f = open('hello.txt', 'r')
#     try:
#         f.write('hello')
#     except Exception as e:
#         print('error')
#         raise NonExistentFileException(
#             'hello.txt cannot be written to', 'from main')
#     finally:
#         print('closing')
#         f.close()
# except Exception as e:
#     print(e)
# else:
#     print('file success')
# finally:
#     print('all closed')
