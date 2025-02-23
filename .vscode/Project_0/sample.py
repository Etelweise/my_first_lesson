# Напоминаем способ создания словаря через список кортежей
# (ключ, значение)
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
client_ages = dict(data)
print(client_ages)
# По результатам 3 повторов получились вот такие результаты:
# {'Maria': 20, 'Mark': 25, 'Ivan': 19, 'Andrey': 23}
# {'Ivan': 19, 'Andrey': 23, 'Mark': 25, 'Maria': 20}
# {'Andrey': 23, 'Mark': 25, 'Maria': 20, 'Ivan': 19}