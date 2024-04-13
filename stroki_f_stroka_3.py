"""Теперь ваша программа спрашивает у пользователя не только имя, но и его возраст. 
После этого программа должна вывести сообщение:
"Hello <name>. You are <age> years old."
Обратите внимание, что буквы в имени все должны быть заглавные. И не забывайте пользоваться f-строкой
Sample Input:
Messi
33
Sample Output:
Hello MESSI. You are 33 years old."""
name = input()
age = int(input())
result = f""" Hello {name.upper()}. You are {age} years old."""
print(result)

"""77 лет
Напишите программу, которая запрашивает имя пользователя и его год рождения.
 Программа должна вывести на экран сообщение "<Имя пользователя>, вам исполнится 77 лет в <год>"""
"""Sample Input 1:
Геннадий
1990
Sample Output 1:
Геннадий, вам исполнится 77 лет в 2067"""
name = input()
age = int(input())
result = f"""{name}, вам исполнится 77 лет в {age + 77}"""
print(result)