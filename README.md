# Клиентское приложение

Реализовано клинетское приложение в формате telegram-бота на telebot.

# Функции бота @ThorFitness_bot

Бот умеет добавлять в базу (в виде json-файла) блюда и их КБЖУ, редактировать уже добавленные блюда и выводить КБЖУ блюда по его названию (так реализован "поиск блюд"). Бот также умеет искать рецепты блюд в системе eda.ru по названию или описанию и выводить ссылки на них. ЕФсли блюдо не понравлось можно посмотреть следующий рецепт. Реализована функция добавления рецепта по ссылке в свою "кулинарную книгу", рецепты из которой затем можно вывести и посмотреть. Реализована также функция добавления приема пищи - для этого пользователь пишет дату приема пищи и название блюда (обязательно из своего списка блюд), бот автоматически подсчитает калории и добавит в базу. Это делалось с целью вывода динамики потребления калорий, но из-за недостатка времени функция не была реализована (планировалась реализация через библиотеку matplotlib). 


Весь пользовательский интерфейс бота реализован через понятные кнопки и инструкции.
