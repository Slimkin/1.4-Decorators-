from datetime import datetime

def logger_with_path(path_to_log):
    def logger(old_function):
        def log(*args, **kwargs):
            start = str(datetime.now())
            result = old_function(*args, **kwargs)
            with open(path_to_log, 'a', encoding='utf8' ) as f:
                f.write(f'{start} - вызов функции\n{str(old_function.__name__)} - название функции\n\
{str(args)}{str(kwargs)} - аргументы функции\n{(result)} - результат функции\n\n')
            return result
        return log
    return logger


if __name__ == "__main__":

    @logger_with_path('E:\\4git\\1.4 «Decorators»\\1.4-Decorators-\\log.txt')
    def test2(a, b=3):
        my_list = []
        my_list.append(a + b)
        return (my_list)

    test2(4)