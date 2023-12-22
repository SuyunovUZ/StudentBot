from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp

global nat, mistake
nat = []
mistake = []

from Buttonlar import start_button, next1_button, next2_button, next3_button, next4_button, next5_button, next6_button, \
    next7_button, next8_button, next9_button, next10_button, next11_button, next12_button, next13_button, next14_button, \
    next15_button, next16_button, next17_button, next18_button, next19_button, next20_button, kitob_buttons, \
    finish_button, togri_javoblar, stop_button, menu_button, testni_boshlash


@dp.message_handler(commands='start')
async def start(message: Message):
    image = open('/home/asilbek/Desktop/Backend-1/QuizBot/rasmlar/Bot.jpg', 'rb')
    await message.answer_photo(image, caption=f'🤖: Assalomu aleykum {message.from_user.full_name}\n'
                                              f' QuizBot ga xush kelibsiz 📚📖', reply_markup=menu_button)


@dp.message_handler(text='Bosh Menu🏠')
async def menu(message: Message):
    await message.answer('Bosh Menu🏠', reply_markup=start_button)


@dp.message_handler(text='Orqaga  ⬅️')
async def nexttt(message: Message):
    await message.answer('🤖', reply_markup=start_button)


@dp.message_handler(text='Orqaga ⬅️')
async def nexttt2(message: Message):
    await message.answer('🤖', reply_markup=start_button)


@dp.message_handler(text='Orqaga⬅️')
async def nexttt2(message: Message):
    await message.answer('🤖', reply_markup=menu_button)


@dp.message_handler(commands='help')
async def next(message: Message):
    await message.reply('Bu bot orqali siz o\'z bilimigizni kuchaytirishingiz mukin🚀🚀🚀')


@dp.message_handler(text='Testni Boshlash 📜')
async def aaa(message: Message):
    await message.reply('Savollarga javob bering⏳')
    await message.answer('1-savol [20 / 1]\n'
                         '2 x 3 = ?', reply_markup=next1_button)


@dp.message_handler(text='Programming 💻')
async def bbb(message: Message):
    await message.answer('TEST Boshlansinmi ?', reply_markup=testni_boshlash)


@dp.message_handler(text='⬅️ Orqaga')
async def ccc(message: Message):
    await message.answer('🤖', reply_markup=start_button)


@dp.message_handler(text='Kitoblar 📚')
async def kitob(message: Message):
    await message.answer('O\'zingizga kerakli kitobni tanlang👇👇👇', reply_markup=kitob_buttons)


@dp.message_handler(text='10 marta ko\'proq.pdf 📖')
async def kitoblarrr1(msg: Message):
    img1 = open('C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/10 marta ko‘proq.pdf', 'rb')
    await msg.answer_document(img1, caption='10 marta ko‘proq.pdf')


@dp.message_handler(text='Abdurauf Fitrat.pdf 📖')
async def kitoblarrr2(msg: Message):
    img2 = open('C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/Abdurauf Fitrat. Oila.pdf', 'rb')
    await msg.answer_document(img2, caption='Abdurauf Fitrat.pdf')


@dp.message_handler(text='English.pdf 📖')
async def kitoblarrr3(msg: Message):
    img3 = open('C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/English Through Reading.pdf', 'rb')
    await msg.answer_document(img3, caption='English.pdf')


@dp.message_handler(text='Akrom Malik.pdf 📖')
async def kitoblarrr3(msg: Message):
    img3 = open('C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/Halqa  Akrom Malik.pdf', 'rb')
    await msg.answer_document(img3, caption='Akrom Malik.pdf')


@dp.message_handler(text='Namoz haqida.pdf 📖')
async def kitoblarrr3(msg: Message):
    img4 = open('C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/Namozda xushu.pdf', 'rb')
    await msg.answer_document(img4, caption='Namoz haqida.pdf')


@dp.message_handler(text='Payg\'ambar haqida.pdf 📖')
async def kitoblarrr3(msg: Message):
    img4 = open(
        'C:/Users/NoutKomp/OneDrive/Рабочий стол/QuizBot/Kitob.pdf/Paygambarimiz-s.a.v.ning-muborak-101-duolari.pdf',
        'rb')
    await msg.answer_document(img4, caption='Payg\'ambar haqida.pdf')


# next2_button
@dp.callback_query_handler(text='5')
async def python(call: CallbackQuery):
    mistake.append(1)
    await call.message.answer('2-savol [20 / 2]\n'
                              '3 x 3 = ?', reply_markup=next2_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='6')
async def python(call: CallbackQuery):
    nat.append(1)
    await call.message.answer('2-savol [20 / 2]\n'
                              '3 x 3 = ?', reply_markup=next2_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='7')
async def python(call: CallbackQuery):
    mistake.append(1)
    await call.message.answer('2-savol [20 / 2]\n'
                              '3 x 3 = ?', reply_markup=next2_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='8')
async def python(call: CallbackQuery):
    mistake.append(1)
    await call.message.answer('2-savol [20 / 2]\n'
                              '3 x 3 = ?', reply_markup=next2_button)
    await call.answer(cache_time=10)


# next3_button
@dp.callback_query_handler(text='9')
async def python(call: CallbackQuery):
    nat.append(2)
    await call.message.answer('3-savol [20 / 3]\n'
                              '8 x 2 = ?', reply_markup=next3_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='10')
async def python(call: CallbackQuery):
    mistake.append(2)
    await call.message.answer('3-savol [20 / 3]\n'
                              '8 x 2 = ?', reply_markup=next3_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='11')
async def python(call: CallbackQuery):
    mistake.append(2)
    await call.message.answer('3-savol [20 / 3]\n'
                              '8 x 2 = ?', reply_markup=next3_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='12')
async def python(call: CallbackQuery):
    mistake.append(2)
    await call.message.answer('3-savol [20 / 3]\n'
                              '8 x 2 = ?', reply_markup=next3_button)
    await call.answer(cache_time=10)


# next4_button
@dp.callback_query_handler(text='13')
async def python(call: CallbackQuery):
    mistake.append(3)
    await call.message.answer('4-savol [20 / 4]\n'
                              '10 x 2 = ?', reply_markup=next4_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='14')
async def python(call: CallbackQuery):
    mistake.append(3)
    await call.message.answer('4-savol [20 / 4]\n'
                              '10 x 2 = ?', reply_markup=next4_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='15')
async def python(call: CallbackQuery):
    mistake.append(3)
    await call.message.answer('4-savol [20 / 4]\n'
                              '10 x 2 = ?', reply_markup=next4_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='16')
async def python(call: CallbackQuery):
    nat.append(3)
    await call.message.answer('4-savol [20 / 4]\n'
                              '10 x 2 = ?', reply_markup=next4_button)

    await call.answer(cache_time=10)


# next5_button
@dp.callback_query_handler(text='17')
async def python(call: CallbackQuery):
    mistake.append(4)
    await call.message.answer('5-savol [20 / 5]\n'
                              '6 x 4 = ?', reply_markup=next5_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='18')
async def python(call: CallbackQuery):
    mistake.append(4)
    await call.message.answer('5-savol [20 / 5]\n'
                              '6 x 4 = ?', reply_markup=next5_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='19')
async def python(call: CallbackQuery):
    mistake.append(4)
    await call.message.answer('5-savol [20 / 5]\n'
                              '6 x 4 = ?', reply_markup=next5_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='20')
async def python(call: CallbackQuery):
    nat.append(4)
    await call.message.answer('5-savol [20 / 5]\n'
                              '6 x 4 = ?', reply_markup=next5_button)
    await call.answer(cache_time=10)


# next6_button
@dp.callback_query_handler(text='21')
async def python(call: CallbackQuery):
    mistake.append(5)
    await call.message.answer('6-savol [20 / 6]\n'
                              '5 x 5 = ?', reply_markup=next6_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='22')
async def python(call: CallbackQuery):
    mistake.append(5)
    await call.message.answer('6-savol [20 / 6]\n'
                              '5 x 5 = ?', reply_markup=next6_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='23')
async def python(call: CallbackQuery):
    mistake.append(5)
    await call.message.answer('6-savol [20 / 6]\n'
                              '5 x 5 = ?', reply_markup=next6_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='24')
async def python(call: CallbackQuery):
    nat.append(5)
    await call.message.answer('6-savol [20 / 6]\n'
                              '5 x 5 = ?', reply_markup=next6_button)
    await call.answer(cache_time=10)


# next7_button
@dp.callback_query_handler(text='25')
async def python(call: CallbackQuery):
    nat.append(6)
    await call.message.answer('7-savol [20 / 7]\n'
                              '3 x 10 = ?', reply_markup=next7_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='26')
async def python(call: CallbackQuery):
    mistake.append(6)
    await call.message.answer('7-savol [20 / 7]\n'
                              '3 x 10 = ?', reply_markup=next7_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='27')
async def python(call: CallbackQuery):
    mistake.append(6)
    await call.message.answer('7-savol [20 / 7]\n'
                              '3 x 10 = ?', reply_markup=next7_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='28')
async def python(call: CallbackQuery):
    mistake.append(6)
    await call.message.answer('7-savol [20 / 7]\n'
                              '3 x 10 = ?', reply_markup=next7_button)
    await call.answer(cache_time=10)


# next8_button
@dp.callback_query_handler(text='29')
async def python(call: CallbackQuery):
    mistake.append(7)
    await call.message.answer('8-savol [20 / 8]\n'
                              '3 x 11 = ?', reply_markup=next8_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='30')
async def python(call: CallbackQuery):
    nat.append(7)
    await call.message.answer('8-savol [20 / 8]\n'
                              '3 x 11 = ?', reply_markup=next8_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='31')
async def python(call: CallbackQuery):
    mistake.append(7)
    await call.message.answer('8-savol [20 / 8]\n'
                              '3 x 11 = ?', reply_markup=next8_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='32')
async def python(call: CallbackQuery):
    mistake.append(7)
    await call.message.answer('8-savol [20 / 8]\n'
                              '3 x 11 = ?', reply_markup=next8_button)
    await call.answer(cache_time=10)


# next9_button
@dp.callback_query_handler(text='33')
async def python(call: CallbackQuery):
    nat.append(8)
    await call.message.answer('9-savol [20 / 9]\n'
                              '4 x 10 = ?', reply_markup=next9_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='34')
async def python(call: CallbackQuery):
    mistake.append(8)
    await call.message.answer('9-savol [20 / 9]\n'
                              '4 x 10 = ?', reply_markup=next9_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='35')
async def python(call: CallbackQuery):
    mistake.append(8)
    await call.message.answer('9-savol [20 / 9]\n'
                              '4 x 10 = ?', reply_markup=next9_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='36')
async def python(call: CallbackQuery):
    mistake.append(8)
    await call.message.answer('9-savol [20 / 9]\n'
                              '4 x 10 = ?', reply_markup=next9_button)
    await call.answer(cache_time=10)


# next10_button
@dp.callback_query_handler(text='37')
async def python(call: CallbackQuery):
    mistake.append(9)
    await call.message.answer('10-savol [20 / 10]\n'
                              '4 x 11 = ?', reply_markup=next10_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='38')
async def python(call: CallbackQuery):
    mistake.append(9)
    await call.message.answer('10-savol [20 / 10]\n'
                              '4 x 11 = ?', reply_markup=next10_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='39')
async def python(call: CallbackQuery):
    mistake.append(9)
    await call.message.answer('10-savol [20 / 10]\n'
                              '4 x 11 = ?', reply_markup=next10_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='40')
async def python(call: CallbackQuery):
    nat.append(9)
    await call.message.answer('10-savol [20 / 10]\n'
                              '4 x 11 = ?', reply_markup=next10_button)
    await call.answer(cache_time=10)


# next11_button
@dp.callback_query_handler(text='41')
async def python(call: CallbackQuery):
    mistake.append(10)
    await call.message.answer('11-savol [20 / 11]\n'
                              '3 x 15 = ?', reply_markup=next11_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='42')
async def python(call: CallbackQuery):
    mistake.append(10)
    await call.message.answer('11-savol [20 / 11]\n'
                              '3 x 15 = ?', reply_markup=next11_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='43')
async def python(call: CallbackQuery):
    mistake.append(10)
    await call.message.answer('11-savol [20 / 11]\n'
                              '3 x 15 = ?', reply_markup=next11_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='44')
async def python(call: CallbackQuery):
    nat.append(10)
    await call.message.answer('11-savol [20 / 11]\n'
                              '3 x 15 = ?', reply_markup=next11_button)
    await call.answer(cache_time=10)


# next12_button
@dp.callback_query_handler(text='45')
async def python(call: CallbackQuery):
    nat.append(11)
    await call.message.answer('12-savol [20 / 12]\n'
                              '5 x 10 = ?', reply_markup=next12_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='46')
async def python(call: CallbackQuery):
    mistake.append(11)
    await call.message.answer('12-savol [20 / 12]\n'
                              '5 x 10 = ?', reply_markup=next12_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='47')
async def python(call: CallbackQuery):
    mistake.append(11)
    await call.message.answer('12-savol [20 / 12]\n'
                              '5 x 10 = ?', reply_markup=next12_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='48')
async def python(call: CallbackQuery):
    mistake.append(11)
    await call.message.answer('12-savol [20 / 12]\n'
                              '5 x 10 = ?', reply_markup=next12_button)
    await call.answer(cache_time=10)


# next13_button
@dp.callback_query_handler(text='49')
async def python(call: CallbackQuery):
    mistake.append(12)
    await call.message.answer('13-savol [20 / 13]\n'
                              '5 x 11 = ?', reply_markup=next13_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='50')
async def python(call: CallbackQuery):
    nat.append(12)
    await call.message.answer('13-savol [20 / 13]\n'
                              '5 x 11 = ?', reply_markup=next13_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='51')
async def python(call: CallbackQuery):
    mistake.append(12)
    await call.message.answer('13-savol [20 / 13]\n'
                              '5 x 11 = ?', reply_markup=next13_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='52')
async def python(call: CallbackQuery):
    mistake.append(12)
    await call.message.answer('13-savol [20 / 13]\n'
                              '5 x 11 = ?', reply_markup=next13_button)
    await call.answer(cache_time=10)


# next14_button
@dp.callback_query_handler(text='53')
async def python(call: CallbackQuery):
    mistake.append(13)
    await call.message.answer('14-savol [20 / 14]\n'
                              '6 x 10 = ?', reply_markup=next14_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='54')
async def python(call: CallbackQuery):
    mistake.append(13)
    await call.message.answer('14-savol [20 / 14]\n'
                              '6 x 10 = ?', reply_markup=next14_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='55')
async def python(call: CallbackQuery):
    nat.append(13)
    await call.message.answer('14-savol [20 / 14]\n'
                              '6 x 10 = ?', reply_markup=next14_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='56')
async def python(call: CallbackQuery):
    mistake.append(13)
    await call.message.answer('14-savol [20 / 14]\n'
                              '6 x 10 = ?', reply_markup=next14_button)
    await call.answer(cache_time=10)


# next15_button
@dp.callback_query_handler(text='57')
async def python(call: CallbackQuery):
    mistake.append(14)
    await call.message.answer('15-savol [20 / 15]\n'
                              '7 x 9 = ?', reply_markup=next15_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='58')
async def python(call: CallbackQuery):
    mistake.append(14)
    await call.message.answer('15-savol [20 / 15]\n'
                              '7 x 9 = ?', reply_markup=next15_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='59')
async def python(call: CallbackQuery):
    mistake.append(14)
    await call.message.answer('15-savol [20 / 15]\n'
                              '7 x 9 = ?', reply_markup=next15_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='60')
async def python(call: CallbackQuery):
    nat.append(14)
    await call.message.answer('15-savol [20 / 15]\n'
                              '7 x 9 = ?', reply_markup=next15_button)
    await call.answer(cache_time=10)


# next16_button
@dp.callback_query_handler(text='61')
async def python(call: CallbackQuery):
    mistake.append(15)
    await call.message.answer('16-savol [20 / 16]\n'
                              '5 x 13 = ?', reply_markup=next16_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='62')
async def python(call: CallbackQuery):
    mistake.append(15)
    await call.message.answer('16-savol [20 / 16]\n'
                              '5 x 13 = ?', reply_markup=next16_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='63')
async def python(call: CallbackQuery):
    nat.append(15)
    await call.message.answer('16-savol [20 / 16]\n'
                              '5 x 13 = ?', reply_markup=next16_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='64')
async def python(call: CallbackQuery):
    mistake.append(15)
    await call.message.answer('16-savol [20 / 16]\n'
                              '5 x 13 = ?', reply_markup=next16_button)
    await call.answer(cache_time=10)


# next17_button
@dp.callback_query_handler(text='65')
async def python(call: CallbackQuery):
    nat.append(16)
    await call.message.answer('17-savol [20 / 17]\n'
                              '2 x 35 = ?', reply_markup=next17_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='66')
async def python(call: CallbackQuery):
    mistake.append(16)
    await call.message.answer('17-savol [20 / 17]\n'
                              '2 x 35 = ?', reply_markup=next17_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='67')
async def python(call: CallbackQuery):
    mistake.append(16)
    await call.message.answer('17-savol [20 / 17]\n'
                              '2 x 35 = ?', reply_markup=next17_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='68')
async def python(call: CallbackQuery):
    mistake.append(16)
    await call.message.answer('17-savol [20 / 17]\n'
                              '2 x 35 = ?', reply_markup=next17_button)
    await call.answer(cache_time=10)


# next18_button
@dp.callback_query_handler(text='69')
async def python(call: CallbackQuery):
    mistake.append(17)
    await call.message.answer('18-savol [20 / 18]\n'
                              '2 x 37 = ?', reply_markup=next18_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='70')
async def python(call: CallbackQuery):
    nat.append(17)
    await call.message.answer('18-savol [20 / 18]\n'
                              '2 x 37 = ?', reply_markup=next18_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='71')
async def python(call: CallbackQuery):
    mistake.append(17)
    await call.message.answer('18-savol [20 / 18]\n'
                              '2 x 37 = ?', reply_markup=next18_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='72')
async def python(call: CallbackQuery):
    mistake.append(17)
    await call.message.answer('18-savol [20 / 18]\n'
                              '2 x 37 = ?', reply_markup=next18_button)
    await call.answer(cache_time=10)


# next19_button
@dp.callback_query_handler(text='73')
async def python(call: CallbackQuery):
    mistake.append(18)
    await call.message.answer('19-savol [20 / 19]\n'
                              '20 x 4 = ?', reply_markup=next19_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='74')
async def python(call: CallbackQuery):
    nat.append(18)
    await call.message.answer('19-savol [20 / 19]\n'
                              '20 x 4 = ?', reply_markup=next19_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='75')
async def python(call: CallbackQuery):
    mistake.append(18)
    await call.message.answer('19-savol [20 / 19]\n'
                              '20 x 4 = ?', reply_markup=next19_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='76')
async def python(call: CallbackQuery):
    mistake.append(18)
    await call.message.answer('19-savol [20 / 19]\n'
                              '20 x 4 = ?', reply_markup=next19_button)
    await call.answer(cache_time=10)


# next20_button
@dp.callback_query_handler(text='77')
async def python(call: CallbackQuery):
    mistake.append(19)
    await call.message.answer('20-savol [20 / 20]\n'
                              '2 x 42 = ?', reply_markup=next20_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='78')
async def python(call: CallbackQuery):
    mistake.append(19)
    await call.message.answer('20-savol [20 / 20]\n'
                              '2 x 42 = ?', reply_markup=next20_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='79')
async def python(call: CallbackQuery):
    mistake.append(19)
    await call.message.answer('20-savol [20 / 20]\n'
                              '2 x 42 = ?', reply_markup=next20_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='80')
async def python(call: CallbackQuery):
    nat.append(19)
    await call.message.answer('20-savol [20 / 20]\n'
                              '2 x 42 = ?', reply_markup=next20_button)
    await call.answer(cache_time=10)


# Finish
@dp.callback_query_handler(text='81')
async def python(call: CallbackQuery):
    mistake.append(20)
    await call.message.answer('Siz 20-ta Savolga Javob berdingiz ⚡⚡⚡', reply_markup=finish_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='82')
async def python(call: CallbackQuery):
    mistake.append(20)
    await call.message.answer('Siz 20-ta Savolga Javob berdingiz ⚡⚡⚡', reply_markup=finish_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='83')
async def python(call: CallbackQuery):
    mistake.append(20)
    await call.message.answer('Siz 20-ta Savolga Javob berdingiz ⚡⚡⚡', reply_markup=finish_button)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='84')
async def python(call: CallbackQuery):
    nat.append(20)
    await call.message.answer('Siz 20-ta Savolga Javob berdingiz ⚡⚡⚡', reply_markup=finish_button)
    await call.answer(cache_time=10)


@dp.message_handler(text='Testni yakunlash🏁')
async def finishshsh(message: Message):
    await message.answer(
        f'⌛Test Yakunlandi\n\n{message.from_user.full_name} siz bu testda:\n✔️To\'g\'ri - {len(nat)}\n❌Xato - {len(mistake)}\nNatija ko\'rsatdingiz\n📝Testlar soni 20ta\n👨🏽‍💻Siz {mistake} savollarda xato qildingiz\n👨🏽‍💻Siz {nat} savollarda to\'g\'ri javob berdingiz',
        reply_markup=togri_javoblar)


@dp.message_handler(text='To\'g\'ri Javoblar ✔️')
async def next(message: Message):
    await message.answer(
        f'To\'g\'ri Javoblar ✔️:\n'
        f'1) 6-B\n'
        f'2) 9-A\n'
        f'3) 16-D\n'
        f'4) 20-D\n'
        f'5) 24-D\n'
        f'6) 25-A\n'
        f'7) 30-B\n'
        f'8) 33-A\n'
        f'9) 40-D\n'
        f'10) 44-D\n'
        f'11) 45-A\n'
        f'12) 50-B\n'
        f'13) 55-C\n'
        f'14) 60-D\n'
        f'15) 63-C\n'
        f'16) 65-A\n'
        f'17) 70-B\n'
        f'18) 74-B\n'
        f'19) 80-D\n'
        f'20) 84-D', reply_markup=stop_button)


@dp.message_handler(text='STOP♨')
async def next(message: Message):
    await message.answer('Bot to\'xtadi.\n'
                         'Botni ishga tushirish uchun /start komandasini bosing')


@dp.message_handler(text='Menu 🏠')
async def menu1(message: Message):
    await message.answer('🤖', reply_markup=start_button)


@dp.message_handler()
async def yoq_malumot(message: Message):
    await message.answer('Kechirasiz bunday ma\'lumot topilmadi 😔')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
