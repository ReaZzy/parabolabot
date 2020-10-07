#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import math
from flask import Flask, request
import os

TOKEN = '1258032906:AAFM6VXY630JpSNUX19w2mFWPUsJI8nXPww'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands = ['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Функція")
    item2 = types.KeyboardButton("Допомога 📚")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Вітаю, {0.first_name}!\nЯ - <b>{1.first_name}</b>, цей бот допоможе тобі дослідити графік функції".format(message.from_user, bot.get_me(),),
                     parse_mode = "html", reply_markup = markup)

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id, '🔸 Введіть 3 цифри з рівняння параболи (y(x)= <b>a</b>x² (<b>+</b>/<b>-</b>)'
                                      ' <b>b</b>x (<b>+</b>/<b>-</b>) <b>c</b>) через пробіл, '
                                      'а саме: <b>a b c</b> \n🔸 Якщо предед <b>x</b> стоїть "-"'
                                      ' або нічого, потрібно писати "-1" чи "1"\n\n🔸 Якщо b або с пропущенно,'
                                      ' потрібно писати "0"\n\n<b>НАПРИКЛАД: -4 5 2</b>\n\n<b>‼️ДОПУСКАЮТЬСЯ ЛИШЕ ЧИСЛА‼️</b> ',parse_mode = "html")

@bot.message_handler(content_types = ['text'])
def lalala(message):
    try:
        if message.chat.type == 'private':

            if message.text == "Функція":
                bot.send_message(message.chat.id, "▫️Введіть 3 цифри з рівняння параболи y(x)= <b>a</b>x² (<b>+</b>/<b>-</b>) <b>b</b>x (<b>+</b>/<b>-</b>)"
                                                  " <b>c</b> через пробіл, а саме: <b>a b c</b>",parse_mode = "html")
            elif message.text == "Допомога 📚":
                bot.send_message(message.chat.id,
                                 '🔸 Введіть 3 цифри з рівняння параболи (y(x)= <b>a</b>x² (<b>+</b>/<b>-</b>) <b>b</b>x'
                                 ' (<b>+</b>/<b>-</b>) <b>c</b>) через пробіл, а саме: <b>a b c</b> \n🔸 Якщо предед <b>x</b> стоїть "-"'
                                 ' або нічого, потрібно писати "-1" чи "1"\n\n🔸 Якщо b або с пропущенно, потрібно писати "0"\n\n<b>НАПРИКЛАД: -4 5 2</b><b>\n\n‼️ДОПУСКАЮТЬСЯ'
                                 ' ЛИШЕ ЧИСЛА‼️</b> ',parse_mode = "html")
            else:
                lis = message.text.split()

                a = int(lis[0])
                b = int(lis[1])
                c = int(lis[2])

                def sdqq(a, b, c):
                    agg = []
                    xv = (-1 * b) / (2 * a)
                    yv = ((4 * a * c) - (b ** 2)) / (4 * a)
                    ans = b ** 2 - (4 * a * c)

                    if a > 0:
                        static = True
                    else:
                        static = False
                    agg.append('\nD(f) = (-∞;∞)')
                    # E(F)
                    if static:
                        agg.append("E(f) = (" + str(yv) + ";∞)\n")
                    else:
                        agg.append("E(f) = (-∞;" + str(yv) + ")\n")

                    # X, Y Вершини
                    agg.append("X Вершини - (" + str(xv) + ";0)"+
                          "\nY Вершини - (" + str(yv) + ";0)\n\n" + "Вісь Oy парабола перетинає в точці (0;" + str(c) + ")\n")

                    if int(ans) == 0:
                        agg.append("Вісь Оx парабола перетинає лише в одній точці = (" + str(int(-1 * b / 2 * a)) + ";0)\n")

                    if int(ans) < 0:
                        agg.append("Парабола не перетинає вісь Ox\n")
                    else:
                        x1 = (-1 * b + math.sqrt(ans)) / (2 * a)
                        x2 = (-1 * b - math.sqrt(ans)) / (2 * a)

                        lx = [x1, x2]
                        x1 = min(lx)
                        x2 = max(lx)

                        agg.append("Вісь Оx парабола перетинає в точках: x1 (" + str(x1) + ";0) і x2 (" + str(x2) + ";0)\n")

                    # ПАРНА НЕ ПАРНА
                    if xv == 0:
                        agg.append("Парабола парна\n")
                    else:
                        agg.append("Парабола ні парна ні не парна\n")

                    # Спадає Зростаэ
                    if static:
                        agg.append("Парабола вітками вверх\n\nЗростає на інтервалі (" + str(
                            xv) + ";∞)\nСпадає на інтервалі (-∞;" + str(xv) + ")\n")

                    else:
                        agg.append("Парабола вітками вниз\n\nЗростає на інтервалі (-∞;" + str(xv) + ")\nСпадає на інтервалі (" + str(
                            xv) + ";∞)\n")

                    # Додатна Відємна
                    if static:
                        if int(ans) == 0:
                            agg.append("Прабола додатна всюди окрім 0: R/{0}\nПрабола  не від'ємна")
                        elif int(ans) < 0:
                            agg.append("Парабола додатна всюди R\nПрабола  не від'ємна")

                        else:
                            agg.append("Парабола додатна на проміжках (-∞;" + str(x1) + ") U (" + str(
                                x2) + ";∞)" + "\nПарабола відємна на проміжку ({};{})".format(x1, x2))

                    else:
                        if int(ans) == 0:
                            agg.append("Прабола відємна всюди окрім 0: R/{0}\nПрабола  не додатна")
                        elif int(ans) < 0:
                            agg.append("Парабола відємна всюди R\nПрабола не додатна")

                        else:
                            agg.append("Парабола відємна на проміжках (-∞;" + str(x1) + ") U (" + str(
                                x2) + ";∞)" + "\nПарабола додатна на проміжку ({};{})".format(x1, x2))

                    bot.send_message(message.chat.id, "".join(i+"\n" for i in agg))
                sdqq(a, b, c)
    except:
        bot.send_message(message.chat.id, "{0.first_name}, введіть /help для допомоги".format(message.from_user, bot.get_me()))

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-9"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://dry-chamber-52499.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
