""" F stroka"""
name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = f"""Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб."""

print(text)

"""математические действия в строках"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = f"""Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {-balance * 2} руб.""" # математическое действие в balance

print(text)

"""методы в строке"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = f"""Дорогой {name.lower()} {mid_name.upper()}, # применено lower и upper
баланс Вашего лицевого счёта составляет {-balance * 2} руб."""

print(text)

"""совсем простой вариант - по переменным"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = f"""Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {56 * 2} руб."""

print(text)

"""работа с функциями в строке"""

name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = f"""Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {abs(-123)} руб."""

print(text)
