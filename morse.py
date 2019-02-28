                                                                                        #импортируем библиотеки
import config                                                                           #в папке config.py хранится наш токен телеграм бота
import telebot                                                                          #телебот
import telegram                                                                         #телеграм
import sqlite3                                                                          #база данных
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters               #нужные функции


bot = telebot.TeleBot(config.token)                                                     #создаем переменную бот через токен который в файле конфиг
updater = Updater('762592341:AAHabfkeSv6y5GUYhuDbZraQd8LYuSV6tIU')                      #создаем апдейтер нужная переменная 
dispatcher = updater.dispatcher                                                         #создаем диспатчер чтобы длбавлять команды
connection = sqlite3.connect('order.db',check_same_thread=False)                        #подключаемся к нашей базе данных

data1=[]                                                                                #наш главный массив где будем сохранять текущие данные
function = 0                                                                            #переменная где будет хранится текущая функция
editing = 0                                                                             #переменная чтобы управлять коммандай edit
error = 0                                                                               #переменная которая проверяет наличие ошибки
user_id1=0                                                                              #переменная чтобы проверять текушего пользователя

def start(bot, update):                                                                 #функция старт
    global user_id1                                                                     #используем global чтобы использовать переменную в этой функции
    global data1                                                                        #используем global чтобы использовать переменную в этой функции
    global function                                                                     #используем global чтобы использовать переменную в этой функции
    function = 0                                                                        #обнуляем переменную
    data1 = []                                                                          #обнуляем переменную
    
    update.message.reply_text(
                              'Привет {}'.format(update.message.from_user.first_name))  #пишем сообщение через функцию sendMessage
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Чтобы сделать регистрацию вы должны написать некоторые данные! Напишите фамилию!") #пишем дальнейшею через функцию sendMessage
    user_id1=update.message.from_user.id                                                #берем текущий id клиента чтобы именно его данные запольнялись дальше



def register(bot,update):                                                               #функция регистр
    user_id=update.message.from_user.id                                                 #берем текущий id клиента чтобы сравнить с начальним
    global data1                                                                        #используем global чтобы использовать переменную в этой функции
    global function                                                                     #используем global чтобы использовать переменную в этой функции
    global editing                                                                      #используем global чтобы использовать переменную в этой функции
    global user_id1                                                                     #используем global чтобы использовать переменную в этой функции
    # Get the text the user sent
    text = update.message.text                                                          #переменная берет значение входяшего сообщения
    # Run it through the summarizer
    if len(data1)==0 and function == 0 and user_id1==user_id:                           #проверяем массив, функцию и совпадает ли юсер айди
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь имя!")                           #отправляем дальнейшую инструкцию
    elif len(data1)==1 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь день рождения в формате дд/мм/гггг!")  #отправляем дальнейшую инструкцию
    elif len(data1)==2 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        print(data1)                                                                    #выводим на экран
    elif len(data1)==3 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь специалность!")                  #отправляем дальнейшую инструкцию
    elif len(data1)==4 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь год поступления!")               #отправляем дальнейшую инструкцию
    
    elif len(data1)==5 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь программу обучения(бакалавр, магистр, дневное, вечерное)!")  #отправляем дальнейшую инструкцию
    elif len(data1)==6 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь грант или договор!")             #отправляем дальнейшую инструкцию
    elif len(data1)==7 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,                                 
                        text="Принято. Напишите теперь получаети ли вы степендию. Да или Нет") #отправляем дальнейшую инструкцию
    elif len(data1)==8 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите теперь причину для справки! Примеры, получить справку; написать заявление;") #отправляем дальнейшую инструкцию
    elif len(data1)==9 and function == 0 and user_id1==user_id:                         #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий                    элемент
        data1.append(text)                                                              #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Пожайлуста проверьте данные которые вы ввели!\n"+data1[0]+"\n"+data1[1]+"\n"+data1[2]+"\n"+data1[3]+"\n"+data1[4]+"\n"+data1[5]+"\n"+data1[6]+"\n"+data1[7]+"\n"+data1[8]+"\n"+data1[9]+"\n"+"Если вы хотите изменить то выберите комманду /edit, если хотите удалить /delete, если всё правильно то комманду /save! Если хотите стать на электронную очередь на изменение расписание выберите команду /timetable!")  #отправляем дальнейшую инструкцию
    elif len(data1)==10 and function == 1 and user_id1==user_id:                        #проверяем юсер айд заполнено ли все и нажал ли клиент на команду делит
        if text.upper() == "ДА":                                                        #увеоичиваем буквы в стринге текст и сравниваем
            data1 = []                                                                  #очищаем
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Принято. Ваши данные удалены")                        #отправляем дальнейшую инструкцию
        elif text.upper == "НЕТ":                                                       #увеоичиваем буквы в стринге текст и сравниваем
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Принято.")                                            #отправляем дальнейшую инструкцию
            function = 0                                                                #просто изменяем вариабл на номер команду регистр
        else:                                                                           
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Извините, произошла ошибка. Можете написать сначала!")#отправляем дальнейшую инструкцию
    elif len(data1) == 10 and function ==2 and user_id1==user_id:                       #проверяем юсер айд заполнено ли все и нажал ли клиент на команду эдит
        if editing == 0:                                                                #проверяем первый ли этот шаг в этой команде
            editing = int(text)                                                         #меняем тип сообщение на инт и даеи это значение на переменную эдитинг
            if editing > 0 and editing <11:                                             #если она в этом промежутке
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Принято. Напишите новое знаечние этого поля!")    #отправляем дальнейшую инструкцию
            else:                                                                       #если не в этом промежутке
                editing = 0                                                             #то просто передаем на начальный шаг
                bot.sendMessage(chat_id=update.message.chat_id,
                                text="Извините, произошла ошибка. Можете написать сначала!") #отправляем дальнейшую инструкцию
        elif editing > 0 and editing < 11 and editing != 3:                             #проверяем юсер айд заполнено ли все и нажал ли клиент на команду эдит
            data1[editing-1]=text                                                       #делаем минус 1 потому что массив начинается с 0 и просто даем новое значение для этого ноиера в массиве
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="Пожайлуста проверьте данные которые вы ввели!\n"+data1[0]+"\n"+data1[1]+"\n"+data1[2]+"\n"+data1[3]+"\n"+data1[4]+"\n"+data1[5]+"\n"+data1[6]+"\n"+data1[7]+"\n"+data1[8]+"\n"+data1[9]+"\n"+"Если вы хотите изменить то выберите комманду /edit, если хотите удалить /delete, если всё правильно то комманду /save! Если хотите стать на электронную очередь на изменение расписание выберите команду /timetable!")  #отправляем дальнейшую инструкцию
            function = 0                                                                #просто изменяем вариабл на номер команду регистр

    elif function == 3 :                                                                #проверяем функции нажал ли на команду админ
        if text=="1234567":                                                             #проверям пароль
            #bot.sendDocument(chat_id=chat_id, document=open('1.pdf', 'rb'))             #отправляем данные
            #bot.sendDocument(chat_id=chat_id, document=open('kaznitu_stutotdel.txt', 'rb')) #отправляем данные
            #bot.sendDocument(chat_id=chat_id, document=open('kaznitu_stutotdel_timetable.txt', 'rb'))   #отправляем данные
            sql = 'delete from KAZNITUstut_otdel'                                       #пишем код для очищение данные в базе данных
            sql1 = 'delete from KAZNITUstut_otdel_timetable'                            #пишем код для очищение данные в базе данных
            cur = connection.cursor()                                                   #переменная чтобы запустить код для базы данных
            cur1 = connection.cursor()                                                  #переменная чтобы запустить код для базы данных
            cur.execute(sql)                                                            #запускаем код
            cur1.execute(sql1)                                                           #запускаем код
            open('kaznitu_stutotdel.txt', 'w').close()                                  #очищаем текстовой документ
            open('kaznitu_stutotdel_timetable.txt', 'w').close()                        #очищаем текстовой документ
            bot.sendMessage(chat_id=update.message.chat_id,
                    text="Данные очищены!")                                             #отправляем дальнейшую инструкцию
            function=0                                                                  #просто изменяем вариабл на номер команду регистр


    else:
        bot.sendMessage(chat_id=update.message.chat_id,
                    text="Извините, произошла ошибка. Можете написать сначала!")        #отправляем дальнейшую инструкцию


def database(user_id,bot,update):                                                       #команда для сохранение данных в команде сэйв
    global error                                                                        #используем global чтобы использовать переменную в этой функции
    cursor = connection.cursor()                                                        #переменная чтобы запустить код для базы данных
    cursor.execute('SELECT * FROM KAZNITUstut_otdel')                                   #запускаем код
    for row in cursor:                                                                  #создаем цикл из полученных данных
        if int(row[0])==user_id:                                                        #проверяем делал ли регистрацию для этого
            error=error+1                                                               #изменяем переменную
    if error==0:                                                                        #проверяем наличие ошибок
        connection.execute("INSERT INTO KAZNITUstut_otdel VALUES (?)",(str(user_id),))  #запускаем код для ввода данных в базу данных
        connection.commit()                                                             #закрываем операцию
        cursor = connection.cursor()                                                    #переменная чтобы запустить код для базы данных
        cursor.execute('SELECT * FROM KAZNITUstut_otdel')                               #запускаем код
        numberOfStudents= 0                                                             #создаем переменную чтобы узнать позицию
        for row in cursor:                                                              #создаем цикл
            numberOfStudents=numberOfStudents+1                                         #вычесляем позицию
        
        bot.send_message(chat_id=update.message.chat_id,text="Ваша позиция в очереде "+str(numberOfStudents)+". Приём студентов начинается с 12:00. Время ожидание 3 минуты. После этого заходит следущий. Спасибо за воспользование наших новых технологий!")  #отправляем дальнейшую инструкцию
    else:
        bot.send_message(chat_id=update.message.chat_id,text="Вы уже зарегистрировались, вы можете зарегистрироваться только завтра!")  #отправляем дальнейшую инструкцию

def database1(user_id,bot,update):                                                      #команда для сохранение данных в команде таймтэйбл
    global error                                                                        #используем global чтобы использовать переменную в этой функции
    cursor = connection.cursor()                                                        #переменная чтобы запустить код для базы данных
    cursor.execute('SELECT * FROM KAZNITUstut_otdel_timetable')                         #запускаем код
    for row in cursor:                                                                  #создаем цикл из полученных данных
        if int(row[0])==user_id:                                                        #проверяем делал ли регистрацию для этого
            error=error+1                                                               #изменяем переменную
    if error==0:                                                                        #проверяем наличие ошибок
        connection.execute("INSERT INTO KAZNITUstut_otdel_timetable VALUES (?)",(str(user_id),))    #запускаем код для ввода данных в базу данных
        connection.commit()                                                             #закрываем операцию
        cursor = connection.cursor()                                                    #переменная чтобы запустить код для базы данных
        cursor.execute('SELECT * FROM KAZNITUstut_otdel_timetable')                     #запускаем код
        numberOfStudents= 0                                                             #создаем переменную чтобы узнать позицию
        for row in cursor:                                                              #создаем цикл
            numberOfStudents=numberOfStudents+1                                         #вычесляем позицию
        
        bot.send_message(chat_id=update.message.chat_id,text="Ваша позиция в очереде "+str(numberOfStudents)+". Приём студентов начинается с 12:00. Время ожидание 3 минуты. После этого заходит следущий. Спасибо за воспользование наших новых технологий!")      #отправляем дальнейшую инструкцию
    else:
        bot.send_message(chat_id=update.message.chat_id,text="Вы уже зарегистрировались, вы можете зарегистрироваться только завтра!") #отправляем дальнейшую инструкцию

def dateConverter(bot,update):                                                          #создаем функцию для формата дня рождения
    global function                                                                     #используем global чтобы использовать переменную в этой функции
    global data1                                                                        #используем global чтобы использовать переменную в этой функции
    global user_id1
    day,month,year=update.message.text.split('/')                                       #создаем три переменные и через функцию сплит сохраняем в эти переменные
    user_id=update.message.from_user.id
    if len(data1) == 2 and function == 0 and user_id1==user_id:                                               #проверяем массив, функцию и совпадает ли юсер айди и заполнен ли предыдущий
        textDate = str(day)+"/"+month+"/"+year                                          #из трех элементов делаем один
        data1.append(textDate)                                                          #добавляем в массив переменную
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Принято. Напишите институт!")                             #отправляем дальнейшую инструкцию
    elif len(data1) == 10 and function == 2 and editing == 3 and user_id1==user_id:                           #проверяем массив, функцию и шаг в команде эдит потому что нам нужно изменить данную
        textDate = str(day)+"/"+month+"/"+year                                          #из трех элементов делаем один
        data1[2]=textDate                                                               #изменяем переменную в массиве
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Пожайлуста проверьте данные которые вы ввели!\n"+data1[0]+"\n"+data1[1]+"\n"+data1[2]+"\n"+data1[3]+"\n"+data1[4]+"\n"+data1[5]+"\n"+data1[6]+"\n"+data1[7]+"\n"+data1[8]+"\n"+data1[9]+"\n"+"Если вы хотите изменить то выберите комманду /edit, если хотите удалить /delete, если всё правильно то комманду /save! Если хотите стать на электронную очередь на изменение расписание выберите команду /timetable!")  #отправляем дальнейшую инструкцию
        function = 0                                                                    #просто изменяем вариабл на номер команду регистр
    else:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Извините, произошла ошибка. Можете написать сначала!")        #отправляем дальнейшую инструкцию
def delete(bot,update):                                                                     #создаем функцию для функции делит
    global data1                                                                            #используем global чтобы использовать переменную в этой функции
    global user_id1
    global function                                                                         #используем global чтобы использовать переменную в этой функции
    user_id=update.message.from_user.id
    if len(data1) != 10 and user_id1==user_id:                                              #проверяем все ли заполнено и юсер айди
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Сначала заполните данные нажав комманду /start!")              #отправляем дальнейшую инструкцию
    else:
        function = 1                                                                        #меняем переменную на номер команды делит
        bot.sendMessage(chat_id=update.message.chat_id,
                    text="Вы уверены что хотите удалить? Напишите ДА или НЕТ!")             #отправляем дальнейшую инструкцию
def edit(bot,update):
    global data1                                                                            #используем global чтобы использовать переменную в этой функции
    global editing                                                                          #используем global чтобы использовать переменную в этой функции
    global function                                                                         #используем global чтобы использовать переменную в этой функции
    if len(data1) == 10:                                              #проверяем все ли заполнено и юсер айди
        function = 2                                                                        #меняем переменную на номер команды эдит
        editing = 0                                                                         #меняем переменную и таким образом мы говорим что это первый шаг
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Напишите номер поля который вы хотите изменить! \n 1. Фамилия \n 2. Имя \n 3. День рождения \n 4. Институт \n 5. Специальность \n 6. Год поступления \n7. Программа обучения(бакалавр, магистр, дневное, вечерное) \n 8. Грант/договор \n 9. Получает степендию/ не получает \n 10. Причина для справки")                                     #отправляем дальнейшую инструкцию
    
    
    else:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Сначала заполните данные нажав комманду /start!")               #отправляем дальнейшую инструкцию

def saving(bot,update):
    global data1                                                                              #используем global чтобы использовать переменную в этой функции
    global error                                                                                #используем global чтобы использовать переменную в этой функции
    error = 0                                                                                   #очищаем переменную
    user_id=update.message.from_user.id                                                         #берем текущий id клиента чтобы сравнить с начальним
    database(user_id,bot,update)                                                                #отправляем данные для проверки и сохранении в функции датабэцз
    if len(data1)==10 and error==0:                                                             #проверяем все ли заполнено и наличие ошибок
        main_row=data1[0]+", "+data1[1]+", "+data1[2]+", "+data1[3]+", "+data1[4]+", "+data1[5]+", "+data1[6]+", "+data1[7]+", "+data1[8]+", "+data1[9]+"." #из всех элементов массива делаем один
        f = open('kaznitu_stutotdel.txt','a')                                                   #открываем текстовой документ
        f.write('\n' +main_row)                                                                 #добавляем в текстовой документ
        f.close()                                                                               #закрываем в текстовой документ
    
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Пожайлуста проверьте данные которые вы ввели!\n"+data1[0]+"\n"+data1[1]+"\n"+data1[2]+"\n"+data1[3]+"\n"+data1[4]+"\n"+data1[5]+"\n"+data1[6]+"\n"+data1[7]+"\n"+data1[8]+"\n"+data1[9]+"\n"+"Если вы хотите изменить то выберите комманду /edit, если хотите удалить /delete, если всё правильно то комманду /save! Если хотите стать на электронную очередь на изменение расписание выберите команду /timetable!")  #отправляем дальнейшую инструкцию                                                                       #отправляем на комманду старт
    else:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Извините, произошла ошибка. Можете повторить сначачла!")          #отправляем дальнейшую инструкцию
def admin(bot,update):
    global function                                                                             #используем global чтобы использовать переменную в этой функции
    function = 3
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Введите пароль!")                                                     #отправляем дальнейшую инструкцию

def timetable(bot,update):
    global data1                                                                                #используем global чтобы использовать переменную в этой функции
    global error                                                                                #используем global чтобы использовать переменную в этой функции
    error = 0                                                                                   #очищаем переменную
    user_id=update.message.from_user.id                                                         #берем текущий id клиента чтобы сравнить с начальним
    database1(user_id,bot,update)                                                               #отправляем данные для проверки и сохранении в функции датабэйз
    if len(data1)==10 and error==0:                                                             #проверяем все ли заполнено и наличие ошибок
        main_row=data1[0]+", "+data1[1]+", "+data1[2]+", "+data1[3]+", "+data1[4]+", "+data1[5]+", "+data1[6]+", "+data1[7]+", "+data1[8]+", "+data1[9]+"." #из всех элементов массива делаем один
        f = open('kaznitu_stutotdel_stutotdel.txt','a')                                         #открываем текстовой документ
        f.write('\n' +main_row)                                                                 #добавляем в текстовой документ
        f.close()                                                                               #закрываем в текстовой документ
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Пожайлуста проверьте данные которые вы ввели!\n"+data1[0]+"\n"+data1[1]+"\n"+data1[2]+"\n"+data1[3]+"\n"+data1[4]+"\n"+data1[5]+"\n"+data1[6]+"\n"+data1[7]+"\n"+data1[8]+"\n"+data1[9]+"\n"+"Если вы хотите изменить то выберите комманду /edit, если хотите удалить /delete, если всё правильно то комманду /save! Если хотите стать на электронную очередь на изменение расписание выберите команду /timetable!")  #отправляем дальнейшую инструкцию                                                                       #отправляем на комманду старт

if __name__=='__main__':                                                                        #главная функция которая запускается
    
        connection.execute('''CREATE TABLE IF NOT EXISTS KAZNITUstut_otdel(user_id text)''')    #создаем если нету таблицу с переменной юсер айди
        connection.execute('''CREATE TABLE IF NOT EXISTS KAZNITUstut_otdel_timetable(user_id text)''')  #создаем если нету таблицу с переменной юсер айди
        
        
        start_handler = CommandHandler('start', start)                                          #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        delete_handler = CommandHandler('delete', delete)                                       #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        edit_handler = CommandHandler('edit', edit)                                             #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        save_handler = CommandHandler('save', saving)                                           #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        admin_handler = CommandHandler('admin', admin)                                          #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        timetable_handler = CommandHandler('timetable', timetable)                              #переменная для создание команды внутри написана имя и функция на которую она отправляет при нажатии
        
        updater.dispatcher.add_handler(MessageHandler(Filters.text, register),group=0)          #переменная для принятие сообщение принимает каждое сообщение и смотрит подходит ли она под нее в этом случае она принимает только один элемент
        updater.dispatcher.add_handler(MessageHandler(Filters.text, dateConverter),group=1) #переменная для принятие сообщение принимает каждое сообщение и смотрит подходит ли она под нее в этом случае она принимает только вот такой формат 01/01/2001
        
        
        dispatcher.add_handler(start_handler)                                                   #добавляем переменную как команду для улавливания в боте
        dispatcher.add_handler(delete_handler)                                                  #добавляем переменную как команду для улавливания в боте
        dispatcher.add_handler(edit_handler)                                                    #добавляем переменную как команду для улавливания в боте
        dispatcher.add_handler(save_handler)                                                    #добавляем переменную как команду для улавливания в боте
        dispatcher.add_handler(admin_handler)                                                   #добавляем переменную как команду для улавливания в боте
        dispatcher.add_handler(timetable_handler)                                               #добавляем переменную как команду для улавливания в боте
        
        updater.start_polling()                                                                 #команда чтобы бот работал непрерывно
        updater.idle()                                                                          #команда чтобы бот работал непрерывно

