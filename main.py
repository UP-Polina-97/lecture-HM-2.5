import datetime
import time
import os
import bs4
import requests
from bs4 import BeautifulSoup

# exercise 1 function
def logger(function_in_work):

    def information_for_log(*args, **kwargs):
        start = time.time()
        date_times = datetime.datetime.now()
        time_spend = int(time.time() - start)
        file_path_of_function = __file__
        file_path = os.getcwd()
        with open('log file.txt', 'a') as file:
            file.write(f'date and time of the call:{date_times } \n')
            file.write(f'call function: {function_in_work.__name__} '
              f'time spend calling {time_spend} \n')
            file.write(f'arguments {args} {kwargs} in {function_in_work.__name__} \n')
            file.write(f'results: {function_in_work(*args, **kwargs)} \n')
            file.write('-' * 50)
            file.write(('\n'))

        print(f'date and time of the call:{date_times }')
        print(f'call function: {function_in_work.__name__} '
              f'time spend calling {time_spend}')
        print(f'file recorded in {file_path} in log file.txt')
        print(f'function recorded in {file_path_of_function}')
        print(f'arguments {args} {kwargs} in {function_in_work.__name__}')
        print(f'results: {function_in_work(*args, **kwargs)} ')
        print('-' * 20)
        return '\n'
    return information_for_log


####### exercise 2 function
file_path = os.getcwd()

def parametrized_decor(parameter):
    def decor(function_in_decor):
        def new_function(*args, **kwargs):
            file_path_of_function = __file__
            start = time.time()
            date_times = datetime.datetime.now()
            time_spend = int(time.time() - start)
            with open('log file_ex_2.txt', 'a') as file:
                file.write(f'date and time of the call:{date_times} \n')
                file.write(f'call function: {function_in_decor.__name__} '
                           f'time spend calling {time_spend} \n')
                file.write(f'arguments {args} {kwargs} in {function_in_decor.__name__} \n')
                file.write(f'results: {function_in_decor(*args, **kwargs)} \n')
                file.write('-' * 50)
                file.write(('\n'))
            print(f'date and time of the call:{date_times}')
            print(f'call function: {function_in_decor.__name__} '
                  f'time spend calling {time_spend}')
            print(f'file recorded in {parameter} in log file_ex_2.txt')
            print(f'function recorded in {file_path_of_function}')
            print(f'arguments {args} {kwargs} in {function_in_decor.__name__}')
            print(f'results: {function_in_decor(*args, **kwargs)} ')
            return '-' * 20

        return new_function
    return decor

@parametrized_decor(file_path)
def summator(x, y):
   return x + y

three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

print('result: ', result)
print('result type: ', type(result))