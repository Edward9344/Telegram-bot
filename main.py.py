import telebot
from telebot import types
from faker import Faker
import random

# Инициализируем бота
bot = telebot.TeleBot(token='6956679212:AAG7D_zF6b5ff8--Qj28nXRj-x9-sadJMwM', parse_mode='html')
faker = Faker()

# Клавиатура для выбора типа карты
card_type_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
card_type_keyboard.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
card_type_keyboard.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Hello! I can generate test numbers for bank cards\nSelect card type:',
        reply_markup=card_type_keyboard
    )

@bot.message_handler(func=lambda message: message.text in ['VISA', 'Mastercard', 'Maestro', 'JCB'])
def card_type_handler(message: types.Message):
    card_type = message.text.lower()
    card_number = faker.credit_card_number(card_type)
    cvc = faker.credit_card_security_code(card_type)
    expiration_date = faker.credit_card_expire()
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Test card {card_type}:\n<code>{card_number}</code>\nCVC: {cvc}\nExpiration Date: {expiration_date}',
        parse_mode='html'
    )

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Select one of the options:',
        reply_markup=card_type_keyboard
    )

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()




