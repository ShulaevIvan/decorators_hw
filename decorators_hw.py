from ast import Num, Str
from pprint import pprint
import os
import datetime
import time
import re

         
def logger(func):
    
    def decor(*args, **kwargs):
        path_file = None
        pattern = r'\w+(\/|\\)'
        
        for i in args:
            print(type(i))
            if type(i) == str:
                if re.match(pattern, i) is not None:
                    path_file = i
               
        if os.path.isdir(path_file):
            pass
        else:
            os.mkdir(path_file)
            
            
        func_name = func.__name__
        time_start = datetime.datetime.now()
        result = func(*args, **kwargs)
        ret_value = f'аргументы функции:{args} {kwargs}'
        
        with open(path_file + 'log.txt', 'w+', encoding='UTF-8')as f:
            f.write('Имя Функции: '+ func_name + '\n')
            f.write('Время вызова: '+ str(time_start) + '\n')
            f.write('Вывод: '+ ret_value + '\n')
            f.write('Результат: '+ (str(result)) + '\n')
            clear = os.getcwd()+'\\'+ (str(path_file)+'log.txt')
            clear_path = clear.replace('/', '\\')
            f.write('Путь к файлу: '+clear_path + '\n')
        return result
        
    return decor

@logger
def run_dec(*args, **kwargs):
    
    return [args, kwargs]
    
run_dec('folder/', 'test1', 1, 'test3')     
         

    

    
    


    
    
    
   



