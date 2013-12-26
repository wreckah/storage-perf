# coding: utf-8
try:
    from ujson import dumps
except ImportError:
    from json import dumps

SMALL_RECORD = {}

MID_RECORD = {
    'name': 'short name #%s',
    'data': dumps({
        'id': 1,
        'value': '1.2',
        'text': u'''Авраáмъ роди́ Исаáка. Исаáкъ же роди́ Иáкова. Иáковъ же роди́ Иýду и брáтiю егó.
Иýда же роди́ Фарéса и Зáру от­ Ѳамáры. Фарéсъ же роди́ Есрóма. Есрóмъ же роди́ Арáма.
Арáмъ же роди́ Аминадáва. Аминадáвъ же роди́ Наассóна. Наассóнъ же роди́ Салмóна.
Салмóнъ же роди́ воóза от­ Рахáвы. Воóзъ же роди́ ови́да от­ рýѳы. Ови́дъ же роди́ Иессéа.
Иессéй же роди́ Дави́да царя́. Дави́дъ же цáрь роди́ соломóна от­ урíины.
Соломóнъ же роди́ ровоáма. Ровоáмъ же роди́ Авíю. Авíа же роди́ áсу.
А́са же роди́ Иосафáта. Иосафáтъ же роди́ Иорáма. Иорáмъ же роди́ Озíю.
Озíа же роди́ Иоаѳáма. Иоаѳáмъ же роди́ Ахáза. Ахáзъ же роди́ езекíю.
Езекíа же роди́ Манассíю. Манассíа же роди́ Амóна. Амóнъ же роди́ Иосíю.
Иосíа же роди́ Иехóнiю и брáтiю егó, въ преселéнiе Вавилóнско­е {Ст. 11 въ нѣ́кiихъ грéч.: Иосíа же роди́ Иоаки́ма и брáтiю егó. Иоаки́мъ же роди́ Иехóнiю въ преселéнiе Вавилóнское.}.
По преселéнiи же Вавилóнстѣмъ, Иехóнiа роди́ Салаѳíиля. Салаѳíиль же роди́ зоровáвеля.
Зоровáвель же роди́ Авiýда. Авiýдъ же роди́ Елiаки́ма. Елiаки́мъ же роди́ азóра.
Азóръ же роди́ садóка. Садóкъ же роди́ Ахи́ма. Ахи́мъ же роди́ Елiýда.
Елiýдъ же роди́ Елеазáра. Елеазáръ же роди́ матѳáна. Матѳáнъ же роди́ Иáкова.
Иáковъ же роди́ Иóсифа, мýжа Марíина, изъ нея́же роди́ся Иисýсъ, глагóлемый Христóсъ.
Всѣ́хъ же родóвъ от­ Авраáма до Дави́да рóдове четыре­нá­де­ся­те: и от­ Дави́да до преселéнiя Вавилóнскаго рóдове четыре­нá­де­ся­те: и от­ преселéнiя Вавилóнскаго до Христá рóдове четыре­нá­де­ся­те.''',
        'list': [
            u'Авраáмъ', u'Исаáкъ', u'Иáковъ', u'Иýда', u'Фарéсъ', u'Есрóмъ',
            u'Арáмъ', u'Аминадáвъ', u'Наассóнъ', u'Салмóнъ', u'Воóзъ',
            u'Ови́дъ', u'Иессéй', u'Дави́дъ', u'Соломóнъ', u'Ровоáмъ', u'Авíа',
            u'А́са', u'Иосафáтъ', u'Иорáмъ', u'Озíа', u'Иоаѳáмъ', u'Ахáзъ',
            u'Езекíа', u'Манассíа', u'Амóнъ', u'Иосíа', u'Иоаки́мъ', u'Иехóнiа',
            u'Салаѳíиль', u'Зоровáвель', u'Авiýдъ', u'Елiаки́мъ', u'Азóръ',
            u'Садóкъ', u'Ахи́мъ', u'Елiýдъ', u'Елеазáръ', u'Матѳáнъ', u'Иáковъ',
            u'Иóсифъ', u'Иисýсъ',
        ],
    }),
}

LARGE_RECORD = {}