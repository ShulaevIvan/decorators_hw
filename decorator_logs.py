import datetime
import os


def logger(param):
    def decor(func):
        def wrapper(*args, **kwargs):
    
            func_name = func.__name__
            time_start = datetime.datetime.now()
            arguments = f'Аргументы функции: {param}'
            path = os.getcwd()
            folder = os.mkdir('log')
            result = func(*args, **kwargs)
            
            with open('log/'+param, 'w+', encoding='UTF-8')as f:
                f.write('Имя Функции: '+ func_name + '\n')
                f.write('Время вызова: '+ str(time_start) + '\n')
                f.write(arguments + '\n')
                f.write('Возвращаемое значение: '+ (str(result)) + '\n')
                f.write(f'Путь к файлу: {path}\{param} \n')
                
            return result
        return wrapper
    return decor


@logger('test.txt')
def start_func(ret_str):
    return ret_str

start_func('dddddd')

