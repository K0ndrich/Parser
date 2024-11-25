# Создаем програму для парсинга сайтов
import requests

# url-адресс сайта, который просто возвращает наш ip компьютера
link = "https://icanhazip.com/"

# отправляем GET-запрос на наш сайт для получения данных

# возвращает статус(успешность) запроса
response = requests.get(link)  # -> <Response [200]>

# .text возвращает данные с страници в виде html или json
response = requests.get(link).text  # -> 159.224.217.57

# .content возвращет данные с странци в виде байтовой строки 
response = requests.get(link).content  # -> b'159.224.217.57\n'
