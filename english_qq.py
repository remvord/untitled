import sys
import time

def blink_once():
    sys.stdout.write('\rTEXT')
    time.sleep(0.5)
    b = ("Loading")
    sys.stdout.write('\r     ')
    time.sleep(0.5)


def blink(number):
    for x in range(0, number):
        blink_once()


blink(3)

# Language Focus
a = 'I`d like to book a flight to Moscow (Я хотел бы забронировать авиабилет в Москву)'
b = 'I`d like to book a seat for two (У вас есть путевка?)'

c = 'Do you have a package tour?'
d = 'Do you have an individual tour?'

# Conservation
Sr_1 = 'I`d like to book a ------ -- ------'
Tr_1 = 'May I know the date of you departure? (Могу я узнать дату вашего отъезда?)'
Sr_2 = 'That will be on March 19th so how much does it cost? (Это будет 19 марта, так сколько это будет стоить?")'
Tr_2 = 'It`s $621 (Six hundred twenty-one)'
Sr_3 = 'Do you have a/an ------ ----?'
Tr_3 = 'Certainly, I`ll look for it. (Конечно, я буду искать его.)'
Dr_4 = 'Thank you.'

# Questions
Q_1 = 'How will you tell the clerk that you would like to book a flight to Moscow? (Как вы скажете клерку,' \
      'что хотите заказать билет до Москвы?)'
Q_2 = 'How will you ask the clerk if they have a package tour? (Как вы спросите служащего, есть ли у них турпакет?)'


print('\n' + a)
print(b)
print('\n' + c)
print(d)
