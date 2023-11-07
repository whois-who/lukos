import telebot

from telebot import types
    
TOKEN = '6635135019:AAG9pmkP45_NdRPpQpYSo0r__VYqT8zmXQk';

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):   
    
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("Обратная связь")
    item4 = types.KeyboardButton("Каталог Товаров")
    item1 = types.KeyboardButton("Доставка")
    
    markup.add(item1, item3, item4)
    
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь с материалами для постройки ваших домов.".format(message.from_user, bot.get_me()),
parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Команды для вашего удобства \n \n /site - Для перехода на наш сайт. \n \n', parse_mode="HTML") 

@bot.message_handler(commands=['site'])
def site(message): 
    bot.send_message(message.chat.id, '<a href="https://lukos-stroy.ru/">Telegram</a>', parse_mode="HTML") 

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Ответы на часто задаваемые вопросы":
            
            markup = types.InlineKeyboardMarkup(row_width=1)    
            item1 = types.InlineKeyboardButton("Где вы находитесь?", callback_data='firstque')
            item2 = types.InlineKeyboardButton("Есть ли возврат на материлы?", callback_data='secondque')
            item3 = types.InlineKeyboardButton("Какую скидку вы можете сделать?", callback_data='thirdque')
            item4 = types.InlineKeyboardButton("Какие сроки доставки?", callback_data='fourthque')   
            item5 = types.InlineKeyboardButton("Какие документы по заказу вы предоставляете?", callback_data='fifthque') 
            item6 = types.InlineKeyboardButton("Отправляете ли вы заказы в регионы РФ?.", callback_data='#')
            item7 = types.InlineKeyboardButton("Адрес самовывоза?", callback_data='#')
            item8 = types.InlineKeyboardButton("Есть ли услуга по подъему на этаж?", callback_data='#')
            item9 = types.InlineKeyboardButton("Вы можете выставить счет с НДС?", callback_data='#')
            item10 = types.InlineKeyboardButton("Как связать с менеджером?", callback_data='#')
    
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

            bot.send_message(message.chat.id, 'Список вопросов', reply_markup=markup)
    
        elif message.text == "Каталог Товаров":
            
            markup = types.InlineKeyboardMarkup(row_width=1)
            item11 = types.InlineKeyboardButton("Вспененный полиэтилен", callback_data='tovar1')
            item12 = types.InlineKeyboardButton("Звукоизоляция", callback_data='tovar2')
            item13 = types.InlineKeyboardButton("Межвенцовый утеплитель", callback_data='tovar3')
            item14 = types.InlineKeyboardButton("Минеральная вата", callback_data='tovar4')   
            item15 = types.InlineKeyboardButton("Пенопласт ПСБ", callback_data='tovar5')
            item16 = types.InlineKeyboardButton("Пенополистирол", callback_data='tovar6')
            
            markup.add(item11, item12, item13, item14, item15, item16 )

            bot.send_message(message.chat.id, 'Теплоизоляционные материалы', reply_markup=markup)    

            markup = types.InlineKeyboardMarkup(row_width=1)
            item21 = types.InlineKeyboardButton("OSB (ориентированно-стружечные плиты)", callback_data='tovar8')
            item22 = types.InlineKeyboardButton("Плиты МДФ, ДВП, ДСП", callback_data='tovar9')
            item23 = types.InlineKeyboardButton("Фанера Шлифованная", callback_data='tovar10')
            item24 = types.InlineKeyboardButton("Фанера Ламинированная", callback_data='tovar11')   
            item25 = types.InlineKeyboardButton("Фанера ФК Влагостойкая", callback_data='tovar12')
            item26 = types.InlineKeyboardButton("Фанера ФК Калиброванная", callback_data='tovar13')
            item27 = types.InlineKeyboardButton("Фанера ФСФ Водостойкая", callback_data='tovar14')

            markup.add(item21, item22, item23, item24, item25, item26, item27)
            bot.send_message(message.chat.id, 'Древесно-плитные материалы', reply_markup=markup)   
    
        elif message.text == "Доставка":
            bot.send_message(message.chat.id, 'По вопросам доставки позвоните менеджеру оп номеру \n \n +7 (495) 761 22 33 \n \n +7 (985) 761 22 33 ')
        
        elif message.text == "Обратная связь":
            bot.send_message(message.chat.id, '<a href="https://t.me/lukosstroy">Telegram</a>', parse_mode="HTML" )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:        
        if call.message:
            if call.data == 'tovar1':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/polietilen.png', 'rb'))
                bot.send_message(call.message.chat.id, '1) Изолайн НПЭ подложка вспененная 30000x1000x10мм (30м²)\n \n 2) Изолайн НПЭ подложка вспененная 50000x1000x2мм (50м²)\n \n 3) Изолайн НПЭ подложка вспененная 50000x1000x3мм (50м²)\n \n 4) Изолайн НПЭ подложка вспененная 50000x1000x5мм (50м²)\n \n5) Изолайн утеплитель фольгированный 15000x1200x10мм (18м²)\n \n 6) Изолайн утепли  тель фольгированный 25000x1200x2мм (30м²)\n \n 7) Изолайн утеплитель фольгированный 25000x1200x3мм (30м²) \n \n 8) Изолайн утеплитель фольгированный 25000x1200x5мм (30м²) \n \n')
            elif call.data == 'tovar2':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/knauf.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Кнауф Акустик Звукоизоляция 1250x610x50мм (12м²)\n \n 2) Роквул Акустик Баттс Звукоизоляция 1000x600x100мм (3м²)\n    \n 3) Роквул Акустик Баттс Звукоизоляция 1000x600x50мм (6м²)\n \n 4) Роквул Акустик Баттс Про Ультратонкий 1000x600x27мм (7,2м²)\n \n 5) СтопЗвук-М двухслойная гидро-звукоизоляция (10м²)\n \n 6) ТермоЗвукИзоляция Стандарт (ТЗИ) Звукоизоляция 10мм (15м²) \n \n 7) ТермоЗвукИзоляция Стандарт (ТЗИ) Звукоизоляция 14мм (15м²)')   
            elif call.data == 'tovar3':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/uteplutil.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Межвенцовый утеплитель джутовый 5мм 0,10х20м \n \n 2) Межвенцовый утеплитель джутовый 5мм 0,15х20м \n \n 3) Межвенцовый утеплитель джутовый 5мм 0,20х20м \n \n 4) Межвенцовый утеплитель лёноватин 5мм 0,10х20м \n \n 5) Межвенцовый утеплитель лёноватин 5мм 0,15х20м \n \n 6) Межвенцовый утеплитель лёноватин 5мм 0,20х20м')
            elif call.data == 'tovar4':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/vata.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Утеплитель Изовол Л-35 1200x600x100мм (2,88м²) \n \n 2) Утеплитель Изовол Л-35 1200x600x50мм (5,76м²) \n \n 3) Утеплитель Изорок Изолайт Л 1000x600x100мм (2,4м²) \n \n 4)Утеплитель Изорок Изолайт Л 1000x600x50мм (4,8м²) \n \n 5) Утеплитель Изорок Изолайт П-50. 1000x500x100мм (2м²) \n \n 6) Утеплитель Изорок Изолайт П-50. 1000x500x50мм (4м²)')
            elif call.data == 'tovar5': 
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/pen.jpeg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Пенопласт ПСБ С-15 Утеплитель 2000х1000х100мм (2м²) \n \n 2) Пенопласт ПСБ С-15 Утеплитель 2000х1000х50мм (2м²) \n \n 3) Пенопласт ПСБ-С 15 Утеплитель 1000x1000x50мм (1м²) \n \n 4) Пенопласт ПСБ-С 15 Утеплитель 1000х1000х100мм (1м²) \n \n 5) Пенопласт ПСБ-С 25 Фасад 1000x1000x100мм (1м²).')
            elif call.data == 'tovar6':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/penopol.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Пеноплекс Комфорт 1185x585x100мм (2,77м²) \n \n 2) Пеноплекс Комфорт 1185x585x20мм (13,9м²) \n \n 3) Пеноплекс Комфорт 1185x585x30мм (9,012м²) \n \n 4) Пеноплекс Комфорт 1185x585x50мм (4,85м²) \n \n 5) Пеноплекс Фундамент 1185x585x100мм (2,78м²)\n \n 6) Пеноплекс Фундамент 1185x585x50мм (4,86м²) \n \n \n   <strong><u>Техноплекс XPS Пенополистирол</u></strong> \n \n 1) Техноплекс XPS Пенополистирол 1180x580x100мм (2,74м²) \n \n  2) Техноплекс XPS Пенополистирол 1180x580x20мм (13,6м²) \n \n 3) Техноплекс XPS Пенополистирол 1180x580x20мм (13,6м²) \n \n 4) Техноплекс XPS Пенополистирол 1180x580x30мм (8,9м²) \n \n 5) Техноплекс XPS Пенополистирол 1180x580x50мм (5,47м²) \n \n \n <strong><u>Урса XPS N-III L-PRO</u></strong> \n \n 1) Урса XPS N-III L-PRO Пенополистирол 1180x600x100мм (2,832м²) \n \n 2)Урса XPS N-III L-PRO Пенополистирол 1180x600x20мм (12,96м²) \n \n 3) Урса XPS N-III L-PRO Пенополистирол 1180x600x30мм (8,496м²) \n \n 4) Урса XPS N-III L-PRO Пенополистирол 1180x600x50мм (4,95м²) ' , parse_mode="HTML") 
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Пока пусто')

        if call.message:
            if call.data == 'tovar8':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/osb.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) ОСБ-3 Талион Ультралам плита влагостойкая 1250x2500x12мм \n \n 2) ОСБ-3 Талион Ультралам плита влагостойкая 1250x2500x15мм \n \n 3) ОСБ-3 Талион Ультралам плита влагостойкая 1250x2500x18мм \n \n 4) ОСБ-3 Талион Ультралам плита влагостойкая 1250x2500x22мм \n \n  5) ОСБ-3 Талион Ультралам плита влагостойкая 1250x2500x9мм \n \n 6) ОСП-3 Калевала плита влагостойкая 1250x2500x12мм \n \n 7) ОСП-3 Калевала плита влагостойкая 1250x2500x15мм \n \n 8) ОСП-3 Кроношпан плита влагостойкая 1220x2440x18мм \n \n 9) ОСП-3 Кроношпан плита влагостойкая 1220x2440x9мм')
            elif call.data == 'tovar9':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/dsp.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Белтермо-TOП (МДВП-плиты) шип-паз 2480х580х35мм \n \n 2) Белтермо-TOП (МДВП-плиты) шип-паз 2490х590х20мм \n \n 3) Белтермо-TOП (МДВП-плиты) шип-паз 2490х590х25мм \n \n 4) Белтермо-TOП (МДВП-плиты) шип-паз 2490х590х28мм \n \n 5) ДВП лист Оргалит 1220x2440x2,8мм (2,97м²) \n \n 6) ДВП лист Оргалит 1220х2140х3мм (2,61м²) \n \n 7) ДСП плита шлифованная 1-сорт 2440х1830х16мм (4,46м²) \n \n 8) ДСП плита шлифованная 1-сорт 2750х1830х16мм (5,03м²) \n \n 9) ЛДСП плита ламинированная белая 2440х1830х16мм (4,46м²) \n \n 10) МДФ плита шлифованная 1-сорт 2440x1830x16мм (4,46м²).')
            elif call.data == 'tovar10':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/fanera.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Фанера шлифованная ФК 3/4 береза 1525x1525x10мм \n \n 2) Фанера шлифованная ФК 3/4 береза 1525x1525x12мм \n \n 3) Фанера шлифованная ФК 3/4 береза 1525x1525x15мм \n \n 4) Фанера шлифованная ФК 3/4 береза 1525x1525x18мм \n \n 5) Фанера шлифованная ФК 3/4 береза 1525x1525x21мм \n \n 6) Фанера шлифованная ФК 3/4 береза 1525x1525x24мм \n \n 7) Фанера шлифованная ФК 3/4 береза 1525x1525x30мм \n \n 8) Фанера шлифованная ФК 3/4 береза 1525x1525x3мм \n \n 9) Фанера шлифованная ФК 3/4 береза 1525x1525x6мм \n \n 10) Фанера шлифованная ФК 3/4 береза 1525х1525х4мм \n \n 11) Фанера шлифованная ФК 3/4 береза 1525х1525х9мм')
            elif call.data == 'tovar11':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/faneralam.webp', 'rb'))
                bot.send_message(call.message.chat.id, '1) Фанера ламинированная 1-сорт Россия 1220x2440x18мм \n \n 2) Фанера ламинированная 1-сорт Россия 1220x2440x21мм \n \n 3) Фанера ламинированная 2-сорт Россия 1220x2440x21мм \n \n 4) Фанера ламинированная 2-сорт Россия 1220х2440х18мм \n \n 5) Фанера ламинированная 2-сорт Хвоя 1220х2440х18мм')
            elif call.data == 'tovar12':        
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/faneravlag.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Фанера ФК сорт ТУ влагостойкая 1525x1525x10мм \n \n 2) Фанера ФК сорт ТУ влагостойкая 1525x1525x12мм \n \n 3) Фанера ФК сорт ТУ влагостойкая 1525x1525x15мм \n \n 4) Фанера ФК сорт ТУ влагостойкая 1525x1525x18мм \n \n 5) Фанера ФК сорт ТУ влагостойкая 1525x1525x21мм \n \n 6) Фанера ФК сорт ТУ влагостойкая 1525x1525x24мм \n \n 7) Фанера ФК сорт ТУ влагостойкая 1525x1525x4мм \n \n 8) Фанера ФК сорт ТУ влагостойкая 1525x1525x6мм \n \n 9) Фанера ФК сорт ТУ влагостойкая 1525x1525x8мм')
            elif call.data == 'tovar13':
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/faneracalib.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x10мм \n \n 2) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x12мм \n \n 3) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x15мм \n \n 4) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x24мм \n \n 5) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x30мм \n \n 6) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x6мм \n \n 7) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x8мм \n \n 8) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x1525x9мм \n \n 9) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525x525x21мм \n \n 10) Фанера ФК ГОСТ (калиброванная) Сорт 4/4 1525х1525x18мм')
            elif call.data == 'tovar14':   
                bot.send_photo(call.message.chat.id, photo=open('C:/Users/zalka/Desktop/Lukos/lukosbot/img/fsf.jpg', 'rb'))
                bot.send_message(call.message.chat.id, '1) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x12мм \n \n 2) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x15мм \n \n 3) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x18мм \n \n 4) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x21мм \n \n 5) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x24мм \n \n 6) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x30мм \n \n 7) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x4мм \n \n 8) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x6мм \n \n 9) Фанера ФСФ 3/4 Береза водостойкая 1220x2440x9мм \n \n 10) Фанера ФСФ 4/4 Береза водостойкая 1220x2440x12мм \n \n 11) Фанера ФСФ 4/4 Береза водостойкая 1220x2440x9мм \n \n 12) Фанера ФСФ Хвоя Водостойкая сорт ТУ 1220x2440x12мм \n \n 13) Фанера ФСФ Хвоя Водостойкая сорт ТУ 1220x2440x15мм \n \n 14) Фанера ФСФ Хвоя Водостойкая сорт ТУ 1220x2440x18мм')   
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, '')
            else:
            # remove inline buttons
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="В разработке", 
                reply_markup=None)

            # show alert    
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="!")


    except Exception as e:  
        print(repr(e))  

# RUN
bot.polling(none_stop=True)