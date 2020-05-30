from datetime import datetime

def logger(old_function):
    def log(*args, **kwargs):
        start = str(datetime.now())
        result = old_function(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf8' ) as f:
            f.write(f'{start} - вызов функции\n{str(old_function.__name__)} - название функции\n{str(args)}{str(kwargs)} - аргументы функции\n{(result)} - результат функции\n\n')
        return result
        with open('log.txt', 'a', encoding='utf8' ) as f:
            f.write(f'{str(result)} - результат функции\n\n')
    return log


if __name__ == "__main__":

    @logger
    def test(a, b=3):
        my_list = []
        my_list.append(a + b)
        return (my_list)

    test(2)