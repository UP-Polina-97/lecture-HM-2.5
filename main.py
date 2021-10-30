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


####### exercise 2
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
            print('-' * 20)
            return '\n'
        return new_function
    return decor






########thing to try on the exerises

@parametrized_decor(parameter= file_path)
def calculate_salary(amount_in_a_year):
    amount_you_get_in_a_year = (amount_in_a_year * 12)
    return f"This is your salary in a year: {amount_you_get_in_a_year}"

calculate_salary(12000)


############# another one
@logger
def search_articles_on_habr(link):
    KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Big Data'}

    ret = requests.get(link)
    soup = BeautifulSoup(ret.text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all(class_='tm-article-snippet__hubs-item')
        hubs = set(hub.find('span').text for hub in hubs)
        if KEYWORDS & hubs:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = 'https://habr.com' + href
            dates = article.find(class_='tm-article-snippet__datetime-published').time['datetime']
            print ('<', dates, '>', '-', '<', article.find('h2').text, '>', '-', '<', link, '>')
    return 'done you can see all the articles above'


link_for_harb = 'https://habr.com/ru/all/'

search_articles_on_habr(link_for_harb)

