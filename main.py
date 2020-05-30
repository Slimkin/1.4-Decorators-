from loggers.decorator_v2 import logger_with_path as logger
from hashlib import md5

if __name__ == "__main__":

    @logger('E:\\4git\\1.4 «Decorators»\\1.4-Decorators-\\log.txt')
    def generator(file_path):
        with open(file_path, 'r', encoding='utf8') as f:
            for line in f:
                hash_line = md5(line.encode())
                yield hash_line.hexdigest()


    for i, line in enumerate(generator('E:\\4git\\1.4 «Decorators»\\1.4-Decorators-\\log.txt'), 1):
        return (f'{i} - {line}')
    