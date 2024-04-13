"""форматирование строки"""
"""конкатенация"""
name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой """ + 'Семён' + " " + 'Семёныч' + """, 
баланс Вашего лицевого счёта составляет """ + '32.56' + """ руб."""

print(text)

"""приводим с учетом"""
name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой """ + name + " " + mid_name + """, 
баланс Вашего лицевого счёта составляет """ + str(balance) + """ руб."""

print(text)

"""МЕТОД ФОРМАТ"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {0} {1}, 
баланс Вашего лицевого счёта составляет {2} руб.""".format(name, mid_name, balance) # в фигурных скобках 
# стоят номера - 0,1,2 - соответственно как стоят в скобках метода format!! name - 0, mid_name - 1 и т д 

print(text)

""" результат перестановки в format местами"""
name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {0} {1}, 
баланс Вашего лицевого счёта составляет {2} руб.""".format(mid_name, name, balance)

print(text)

"""именованное использование переменных"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб.""".format(mid_name=mid_name, name=name, balance=balance)

print(text)

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб. {name}""".format(mid_name=mid_name, name=name, balance=balance)

print(text)

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {n} {m}, 
баланс Вашего лицевого счёта составляет {b} руб.""".format(m=mid_name, n=name, b=balance)

print(text)