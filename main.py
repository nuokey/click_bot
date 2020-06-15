import telebot

balance = "Ошибка, \nНапишите /start"

bot = telebot.TeleBot('1280076277:AAH67aF5LXmq41J1AzqmCO44YrLL_ehKlEc')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Click')

@bot.message_handler(commands=['start'])
def start_message(message):
	global balance
	bot.send_message(message.chat.id, 'Вас приветствует кликер, созданный NuoKey.\nВ случае странного поведения бота, обратитесь к @nuotimo', reply_markup=keyboard1)

	data = (open('data.txt', 'r').readlines())
	for i in range(len(data)):
		global balance
		if data[i].split(" ")[0] == str(message.chat.id):
			balance = int(data[i].split(" ")[1])
			break
		
		elif i == len(data)-1:
			dataa = open('data.txt', "a")
			dataa.write(str(message.chat.id) + " 0" + "\n")
			dataa.close()
			balance = 0

@bot.message_handler(content_types=['text'])
def send_text(message):
	global balance
	data = (open('data.txt', 'r').read()).split("\n")
	for i in range(len(data)):
		if data[i].split(" ")[0] == str(message.chat.id):
			balance = int(data[i].split(" ")[1])

	if message.text == 'Click':
		for n in range(len(data)):
			if len(data[n]) >= 3:
				data[n] = data[n].split(" ")
				data[n][1] = int(data[n][1])
				if data[n][0] == str(message.chat.id):
					data[n][1] = str(data[n][1] + 1)
					balance = data[n][1]
		
		print(message.text, message.chat.username, balance)
		bot.send_message(message.chat.id, 'Клик засчитан,\nВаш баланс: '+ str(balance))

		data_w = str(data).replace("], ", "\n")
		data_w = data_w.replace("[", "")
		data_w = data_w.replace("]", "")
		data_w = data_w.replace(",", "")
		data_w = data_w.replace("'", "")
		dataw = open('data.txt', 'w')
		print(data_w)
		dataw.write(data_w)
		dataw.close()
	else:
		bot.send_message(message.chat.id, 'Неизвестная команда')

bot.polling()
