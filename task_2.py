import os
from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            data_function = []
            keywords = ['Текущее время и дата', 'Имя функции', 'Аргументы вызова функции',
                        'Возвращаемое значение функции']
            date = datetime.now()
            date_string = date.strftime('%m/%d/%y %H:%M:%S')
            data_function.append(date_string)
            function_name = old_function.__name__
            data_function.append(function_name)
            if args and kwargs:
                arguments = [list(args), kwargs]
                data_function.append(arguments)
            elif args:
                data_function.append(list(args))
            elif kwargs:
                data_function.append(kwargs)
            result = old_function(*args, **kwargs)
            data_function.append(result)
            data = dict(zip(keywords, data_function))
            with open(path, 'a', encoding='utf8') as f:
                f.write(f'{str(data)}\n')
            return result

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path, encoding='utf8') as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'
