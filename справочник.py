def calculate_ages(persons):
    ages = {}
    for person, details in persons.items():
        birth_year = details.get('born', 0)
        death_year = details.get('died', 2024)  
        ages[person] = death_year - birth_year
    return ages

# Пример данных
persons = {
    "lenin": {"born": 1870, "died": 1924},
    "mao": {"born": 1893, "died": 1976},
    "gandhi": {"born": 1869, "died": 1948},
    "hirohito": {"born": 1901, "died": 1989},
}
result = calculate_ages(persons)
print(result)  # Ожидаемый результат: {'lenin': 54, 'mao': 83, 'gandhi': 79, 'hirohito': 88}

