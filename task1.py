import random
import telebot

bot = telebot.TeleBot('1895322488:AAHX8crVcyhhpwrROL0gsXz_GSIpznrw-ME')

DIGITS = [str(i) for i in range(10)]
my_number = ''
my_table = list()

@bot.message_handler(commands=['start', 'game'])
def start_game(message):
    digits = DIGITS.copy()
    global my_number
    global my_table
    my_number = ''
    for pos in range(4):
        if pos:
            digit = random.choice(digits)
        else:
            digit = random.choice(digits[1:])
        my_number += digit
        digits.remove(digit)

    bot.reply_to(message, 
      "Игра Быки и Коровы\n\n" + 
      f"Я загадал 4-значное число. Попробуй отгадать, {message.from_user.first_name}!")

@bot.message_handler(content_types=['text'])
def bot_answer(message):
    text = message.text
    if len(text) == 4 and text.isnumeric() and len(text) == len(set(text)):
        cows, bulls = 0, 0
        for i in range(len(text)):
            if text[i] in my_number:
                cows += 1
                if text[i] == my_number[i]:
                    bulls += 1
        if bulls == 4:
            response = "Ты угадал!"
        else:
            my_table.append(f"{text} | {cows} / {bulls}\n")
            liNE = ""
            for z in range(len(my_table)):
                liNE += my_table[z]
            response = liNE
    else:
        response = 'Пришли мне 4-значное число с разными цифрами!'
    bot.send_message(message.from_user.id, response)

bot.polling(none_stop=True)
