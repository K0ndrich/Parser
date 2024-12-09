# Создаем програму для парсинга сайтов
import requests

from bs4 import BeautifulSoup

# подменна данных от сайта при запросе на него
header = {"user-agent": "aaabbbccc"}

# url-адресс сайта, который просто возвращает наш ip компьютера
# link = "https://icanhazip.com/"

link = "https://browser-info.ru/"

# отправляем GET-запрос на наш сайт для получения данных
# headers указывает свою шапку запроса, подменяем ответ,данные полученные от сайта
response = requests.get(link, headers=header).text


# response.status_code)  # -> 200
# response.text  # -> 159.224.217.57

# soup являеться обьектом BeautifulSoup с которим дальше будем работать для получения данных
# lxml указивает тип парсера, также еще есть html.parser или html5lib
soup = BeautifulSoup(response, "lxml")

# берем часть кода html по указаному id
# find нахоидт только первое значение
block = soup.find("div", id="tool_padding")

# CHECK JAVA SCRIPT
# из взятого блока берем внутренний блко по меньше
check_js = block.find("div", id="javascript_check")
# find_alL будет находить все значения
# берем воторой span по индексу
status_js = check_js.find_all("span")[1].text  # -> выключено
result_js = f"java script: {status_js}"  # -> java script: выключено

# CHECK FLASH
check_flash = block.find("div", id="flash_version")
status_flash = check_flash.find_all("span")[1].text  # -> отсутствует/выключен
result_flash = f"flash: {status_flash}"  # -> flash: отсутствует/выключен


# CHEKC USER AGENT
result_user = block.find("div", id="user_agent").text


# PRINT
print(result_js)
print(result_flash)
print(result_user)
