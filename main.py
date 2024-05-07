from src.GetAPIHH import GetApiHh
from src.JsonSaver import JsonSaver
from src.Vacancy import Vacancy

response = GetApiHh()

while True:
    user_vacancy: str = input("Наименование вакансии для поиска:\n")
    user_city: str = input("В каком городе ищем вакансию:\n")
    if isinstance(user_city, str) and isinstance(user_vacancy, str):
        break
    print(f"Пожалуйста, напишите город {user_city}")

while True:
    user_salary = input("На какую минимальную ЗП вы готовы:\n")
    if user_salary.isdigit():
        break
    print(f"Пожалуйста, введите цифрами {user_salary}")

# Получаем список вакансий по заданным параметрам
response.get_vacancy_from_api(user_vacancy)

file_json = JsonSaver()

# Сохраняем список вакансий в JSON файле
file_json.save_file(response.all_vacancy)

# Читаем список вакансий из JSON файла
file_vacancies = file_json.read_file()

# Печатываем список вакансий
vacancy = Vacancy.get_vacancy_list(file_vacancies, user_city, int(user_salary))
sorted_vacancies = sorted(vacancy)

while True:
    count = input("Какие вакансии вы хотите видеть :\n")
    if count.isdigit():
        break
    print(f"Пжл, введите {count}")

print(*sorted_vacancies[:int(count)])