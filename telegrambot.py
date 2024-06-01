
import telebot
import sqlite3

bot = telebot.TeleBot('7146268262:AAFmy4SshIj97VnHQqqM32TGhyIZ9oR5DJE')

name = None

@bot.message_handler(commands=['start'])
def site(message):
    bot.send_message(message.chat.id, 'Для регестриции тебе понадобиться твой телегрем id,'
                                      ' чтобы его узнать напиши id, если ты его знаешь напиши /go')

@bot.message_handler(commands=['go'])
def reg1(message):
    conn = sqlite3.connect('БАЗА ДАННЫХ.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id ,'Окей, введи своё имя:')
    bot.register_next_step_handler(message ,user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введи свой id:')
    bot.register_next_step_handler(message ,user_id)


def user_id(message):
    conn = sqlite3.connect('БАЗА ДАННЫХ.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users(name,id) VALUES("%s", "%s")' % (name, id))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Ты зарегистрированы!', )
@bot.message_handler(commands=['Authorization'])
def hr(message):
    conn = sqlite3.connect('БАЗА ДАННЫХ.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users(name,id) VALUES("%s", "%s")' % (name, id))
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('База данных:', callback_data='users'))
    bot.send_message(message.chat.id,f'i',reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('БАЗА ДАННЫХ.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info =''
    for el in users:
        info += f'Имя:{el[1]}, id: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)
@bot.message_handler()
def ky(message):
    if message.text.lower() =='id':
      bot.send_message(message.chat.id ,f'{message.from_user.id}')
bot.polling(none_stop=True)
