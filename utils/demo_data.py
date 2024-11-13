'Билдеры демонстрационных сообщений'

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def me() -> str:
    'Демонстрационная информация о пользователе'

    return (
        'ФИО (родителя) - Иванов Павел Сергеевич\n'
        'Номер телефона - +7 (777) 777-77-77\n\n'
        '1 ребенок:\n\n'
        'ФИО - Иванов Иван Павлович\n'
        'Дата рождения - 22.11.2008\n'
        'Школа - МБОУ "СОШ № 9"\n'
        'Класс - 10 А\n\n'
        '2 ребенок:\n\n'
        'ФИО - Иванов Павел Павлович\n'
        'Дата рождения - 22.11.2008\n'
        'Школа - МБОУ "СОШ № 9"\n'
        'Класс - 10 А\n'
    )


def cs() -> str:
    'Демонстрационная информация о классных часах'

    return 'Информация о классных часах отсутсвует'


def events() -> str:
    'Демонстрационное сообщение об ивентах'

    return 'Кажется, ивентов не намечается)'


def birthdays() -> str:
    'Демонстрационное сообщение о днях рождения'

    return 'Кажется, дней рождений не намечается)'


def marks() -> str:
    'Демонстрационное сообщение об оценках'

    return (
        'Оценки:\n\n'
        '<pre>'
        '🟧 Рус. Яз.  │ 3.00 │ 3 2 3 4\n'
        '🟨 Англ. Яз. │ 3.75 │ 3 4 3 5\n'
        '🟩 ОБЗР      │ 5.00 │ 5 5 5 5\n'
        '🟨 Биология  │ 3.66 │ 4 3 4\n'
        '🟨 Физ-ра    │ 3.83 │ 5 4 4 3 3 4\n'
        '🟥 Алгебра   │ 2.00 │ 2\n'
        '🟨 Литер.    │ 4.16 │ 5 5 5 2 5 3\n'
        '🟨 История   │ 4.00 │ 4\n'
        '🟧 Геометрия │ 3.25 │ 3 4 3 3\n'
        '🟩 Теор. Вер.│ 5.00 │ 5 5\n'
        '🟥 Химия     │ 2.00 │ 2 2\n'
        '</pre>'
    )


def i_marks() -> str:
    'Демонстрационное сообщение об итоговых оценках'

    return (
        'Итоговые оценки:\n\n'
        '1-4 - Четвертные оценки\n'
        'Г - Годовая\n'
        'Э - Экзаменационная (если есть)\n'
        'И - Итоговая\n\n'
        '<pre>'
        'Предмет    │ 1 │ 2 │ 3 │ 4 │ Г │ Э │ И │\n'
        '───────────┼───┼───┼───┼───┼───┼───┼───┤\n'
        'Алгебра    │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'Биология   │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Теор. Вер. │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'География  │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Геометрия  │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'Инд. пр.   │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Англ. Яз.  │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Информ.    │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'История    │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Литер.     │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Обществ.   │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'ОБЗР       │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Рус. Яз.   │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'Физика     │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │ 5 │\n'
        'Физ-ра     │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        'Химия      │ 5 │ 5 │ 5 │ 5 │ 5 │ - │ 5 │\n'
        '</pre>'
    )


def hw(index: str | int) -> str:
    'Демонстрационное сообщение о домашнем задании'

    hw_text = [
        (
            'Д/З на 04.11.2024 понедельник\n\n'
            'На этот день не указано д/з'
        ),
        (
            'Д/З на 05.11.2024 вторник\n\n'
            '1. Информ.    │\n'
            '2. Информ.    │\n'
            '3. Физика     │\n'
            '4. Геометрия  │ п.4,п.7 выучить теоремы, повторить п.1-3,п.7\n'
            '5. Физ-ра     │\n'
            '6. География  │\n'
            '7. Обществ.   │\n'
        ),
        (
            'Д/З на 06.11.2024 среду\n\n'
            '1. Алгебра    │ п.4, п.7 - выучить теоремы\n'
            '2. Инд. пр.   │\n'
            '3. Физ-ра     │\n'
            '4. Англ. Яз.  │ не задано\n'
        ),
        (
            'Д/З на 07.11.2024 четверг\n\n'
            '1. Функ. Гр.  │\n'
            '2. Алгебра    │ выучить записи подготовиться к самостоятельной работе\n'
            '3. ОБЗР       │ Нет задания\n'
            '4. Рус. Яз.   │\n'
            '5. Англ. Яз.  │ описать школьную систему в России\n'
        ),
        (
            'Д/З на 08.11.2024 пятницу\n\n'
            '1. Геометрия  │ п.5 выучить лемму и теорему\n'
            '2. Геометрия  │\n'
            '3. Англ. Яз.  │ написать письмо о школьной системе в России другу\n'
            '4. Обществ.   │\n'
            '5. Литер.     │ Проанализировать смерть Базарова\n'
            '6. Биология   │ Изучить пар.5,6, ответить на вопр.4 (стр.35)\n'
            '7. История    │ стр.114-122 изучить\n'
        ),
        (
            'Д/З на 09.11.2024 субботу\n\n'
            '1. Информ.    │\n'
            '2. Информ.    │\n'
            '3. Теор. Вер. │ выучить записи в тетради и выполнить задание в тетради\n'
            '4. Литер.     │ Прочитать критические статьи\n'
            '5. Информ.    │\n'
            '6. Физика     │\n'
        )
    ]

    hw_keyboard = [
        [
            [
                InlineKeyboardButton(text="Нет Д/З", callback_data='None')
            ]
        ],
        [
            [
                InlineKeyboardButton(text="вт Геометрия", callback_data='None'),
                InlineKeyboardButton(text="chatgpt",  callback_data="chatgpt_1_3"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%"
                    "B8%D1%8F%20%D0%93%D0%94%D0%97 %D0%BF.4%2C%D0%BF.7%20%D0%B2%D1%8B%D1%83%D1%87%D"
                    "0%B8%D1%82%D1%8C%20%D1%82%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D1%8B%2C%20%D0%BF%D0%B"
                    "E%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D1%82%D1%8C%20%D0%BF.1-3%2C%D0%BF.7"
                ))
            ]
        ],
        [
            [
                InlineKeyboardButton(text="ср Алгебра", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_2_0"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%90%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0%20%"
                    "D0%93%D0%94%D0%97 %D0%BF.4%2C%20%D0%BF.7%20-%20%D0%B2%D1%8B%D1%83%D1%87%D0%B8%"
                    "D1%82%D1%8C%20%D1%82%D0%B5%D0%BE%D1%80%D0%B5%D0%BC%D1%8B"
                ))
            ],
            [
                InlineKeyboardButton(text="ср Англ. Яз.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_2_3"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%98%D0%BD%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%"
                    "BD%D0%BD%D1%8B%D0%B9%20%D1%8F%D0%B7%D1%8B%D0%BA%20%28%D0%B0%D0%BD%D0%B3%D0%BB%"
                    "D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%29%20%D0%93%D0%94%D0%97 %D0%BD%D0%B5%20%D0"
                    "%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%BE"))
            ]
        ],
        [
            [
                InlineKeyboardButton(text="чт Алгебра", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_3_1"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%90%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0%20%"
                    "D0%93%D0%94%D0%97 %D0%B2%D1%8B%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B7%D0%B0%D0"
                    "%BF%D0%B8%D1%81%D0%B8%20%D0%BF%D0%BE%D0%B4%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%B8"
                    "%D1%82%D1%8C%D1%81%D1%8F%20%D0%BA%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE"
                    "%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B0%D0%B1%D0%BE%D1"
                    "%82%D0%B5"))
            ],
            [
                InlineKeyboardButton(text="чт ОБЗР", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_3_2"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%B1%"
                    "D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%B8%20%"
                    "D0%B7%D0%B0%D1%89%D0%B8%D1%82%D1%8B%20%D0%A0%D0%BE%D0%B4%D0%B8%D0%BD%D1%8B%20%"
                    "D0%93%D0%94%D0%97 %D0%9D%D0%B5%D1%82%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1"
                    "%8F"))
            ],
            [
                InlineKeyboardButton(text="чт Англ. Яз.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_3_4"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%98%D0%BD%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%"
                    "BD%D0%BD%D1%8B%D0%B9%20%D1%8F%D0%B7%D1%8B%D0%BA%20%28%D0%B0%D0%BD%D0%B3%D0%BB%"
                    "D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%29%20%D0%93%D0%94%D0%97 %D0%BE%D0%BF%D0%B8"
                    "%D1%81%D0%B0%D1%82%D1%8C%20%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%83%D1%8E%20"
                    "%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83%20%D0%B2%20%D0%A0%D0%BE%D1%81%D1%81"
                    "%D0%B8%D0%B8"))
            ]
        ],
        [
            [
                InlineKeyboardButton(text="пт Геометрия", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_4_0"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%"
                    "B8%D1%8F%20%D0%93%D0%94%D0%97 %D0%BF.5%20%D0%B2%D1%8B%D1%83%D1%87%D0%B8%D1%82%"
                    "D1%8C%20%D0%BB%D0%B5%D0%BC%D0%BC%D1%83%20%D0%B8%20%D1%82%D0%B5%D0%BE%D1%80%D0%"
                    "B5%D0%BC%D1%83"))
            ],
            [
                InlineKeyboardButton(text="пт Англ. Яз.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_4_2"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%98%D0%BD%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%"
                    "BD%D0%BD%D1%8B%D0%B9%20%D1%8F%D0%B7%D1%8B%D0%BA%20%28%D0%B0%D0%BD%D0%B3%D0%BB%"
                    "D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%29%20%D0%93%D0%94%D0%97 %D0%BD%D0%B0%D0%BF"
                    "%D0%B8%D1%81%D0%B0%D1%82%D1%8C%20%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE%20%D0%BE"
                    "%20%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%81%D0%B8%D1%81%D1%82"
                    "%D0%B5%D0%BC%D0%B5%20%D0%B2%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%20%D0%B4%D1"
                    "%80%D1%83%D0%B3%D1%83"))
            ],
            [
                InlineKeyboardButton(text="пт Литер.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_4_4"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%9B%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%"
                    "83%D1%80%D0%B0%20%D0%93%D0%94%D0%97 %D0%9F%D1%80%D0%BE%D0%B0%D0%BD%D0%B0%D0%BB"
                    "%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%20%D1%81%D0%BC%D0%B5%D1"
                    "%80%D1%82%D1%8C%20%D0%91%D0%B0%D0%B7%D0%B0%D1%80%D0%BE%D0%B2%D0%B0%E2%80%8B"))
            ],
            [
                InlineKeyboardButton(text="пт Биология", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_4_5"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%91%D0%B8%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%"
                    "8F%20%D0%93%D0%94%D0%97 %D0%98%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%BF%D0"
                    "%B0%D1%80.5%2C6%2C%20%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B8%D1%82%D1%8C%20%D0%BD"
                    "%D0%B0%20%D0%B2%D0%BE%D0%BF%D1%80.%E2%80%8B4%20%28%D1%81%D1%82%D1%80.35%29"))
            ],
            [
                InlineKeyboardButton(text="пт История", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_4_6"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%"
                    "D0%93%D0%94%D0%97 %D1%81%D1%82%D1%80.114-122%20%D0%B8%D0%B7%D1%83%D1%87%D0%B8%"
                    "D1%82%D1%8C%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B%E2%80%8B"))
            ]
        ],
        [
            [
                InlineKeyboardButton(text="сб Теор. Вер.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_5_2"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%92%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%"
                    "BE%D1%81%D1%82%D1%8C%20%D0%B8%20%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%"
                    "B8%D0%BA%D0%B0%20%D0%93%D0%94%D0%97 %E2%80%8B%D0%B2%D1%8B%D1%83%D1%87%D0%B8%D1"
                    "%82%D1%8C%20%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8%20%D0%B2%20%D1%82%D0%B5%D1%82"
                    "%D1%80%D0%B0%D0%B4%D0%B8%20%D0%B8%20%E2%80%8B%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0"
                    "%BD%D0%B8%D1%82%D1%8C%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B2%20"
                    "%D1%82%D0%B5%D1%82%D1%80%D0%B0%D0%B4%D0%B8"))
            ],
            [
                InlineKeyboardButton(text="сб Литер.", callback_data='None'),
                InlineKeyboardButton(text="chatgpt", callback_data="chatgpt_5_3"),
                InlineKeyboardButton(text="google", url=(
                    "https://www.google.com/search?q=%D0%9B%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%"
                    "83%D1%80%D0%B0%20%D0%93%D0%94%D0%97 %D0%9F%D1%80%D0%BE%D1%87%D0%B8%D1%82%D0%B0"
                    "%D1%82%D1%8C%20%D0%BA%D1%80%D0%B8%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0"
                    "%B5%20%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8%E2%80%8B"))
            ]
        ]
    ]

    if index == 't':
        text = hw_text[4]
        keyboard = hw_keyboard[4]

        keyboard.append([
            InlineKeyboardButton(text='На неделю', callback_data='hw_w')
        ])

    elif index == 'w':
        text = '\n\n'.join(''.join(map(str, hw)) for hw in hw_text)
        keyboard = sum(hw_keyboard, [])

        keyboard.append([
            InlineKeyboardButton(text='На завтра', callback_data='hw_t')
        ])

    else:
        index = int(index)

        text = hw_text[index]
        keyboard = hw_keyboard[index]

        keyboard.append([
            InlineKeyboardButton(text='На завтра', callback_data='hw_t'),
            InlineKeyboardButton(text='На неделю', callback_data='hw_w')
        ])

    keyboard.append([
        InlineKeyboardButton(text='Дни недели', callback_data='hw_days')
    ])

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    text = (
        f'<pre>{''.join(text)}'
        '</pre>\n\n'
        'Д/З МОЖЕТ БЫТЬ НЕ АКТУАЛЬНЫМ!!!\n\n'
        'Его указывают (зачастую не указывают) '
        'учителя и мы никак не можем повлиять на этот процесс.\n\n'
        'Для получения актуального Д/З попросите вашего учителя указывать его в дневнике)'
    )

    return text, markup