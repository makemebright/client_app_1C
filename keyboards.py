from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Функционал')
b2 = KeyboardButton(text='Моя кулинарная книга')
b3 = KeyboardButton(text='Динамика')
b4 = KeyboardButton(text='Добавить потребление калорий')
b5 = KeyboardButton(text='Найти блюдо в моих')

kb.add(b1, b2, b3)
kb.add(b4, b5)

kb_receipt = ReplyKeyboardMarkup(resize_keyboard=True)
br1 = KeyboardButton(text='Следующий рецепт')
br2 = KeyboardButton(text='Добавить в мою книгу')
br3 = KeyboardButton(text='Моя кулинарная книга')
br4 = KeyboardButton(text='Функционал')

kb_receipt.add(br1, br2)
kb_receipt.add(br3, br4)

#kb_dishes = ReplyKeyboardMarkup(resize_keyboard=True)
#bd1 = KeyboardButton(text='Динамика потребления калорий')
#bd2 = KeyboardButton(text='Добавить потребление калорий')
#bd3 = KeyboardButton(text='Найти блюдо в моих')

#kb_dishes.add(bd1, bd2)
#kb_dishes.add(bd3)

# kb_receipt2 = ReplyKeyboardMarkup(resize_keyboard=True)
# br21 = KeyboardButton(text='Следующий рецепт')
# br22 = KeyboardButton(text='Отмена последнего действия')
# br23 = KeyboardButton(text='Моя кулинарная книга')
#
# kb_receipt.add(br21, br22)
# kb_receipt.add(br23)
