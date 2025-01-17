"""Нейросеть для помощи в учебе."""

from secrets import choice

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from utils.ask_gpt import ask_gpt
from utils.db import counter
from utils.messages import error

router = Router(name=__name__)


# Нейронная сеть, для помощи в учебе
@router.message(Command("chatgpt"))
async def lessons_msg(msg: Message) -> None:
    """Отвечает за /chatgpt."""
    examples = [
        "Напиши сочинение по роману Отцы и дети",
        "Расскажи о теореме пифагора",
        "Что такое диактелизмы?",
        "Что такое гигабайт?",
        "Расскажи о булиевой алгебре",
        "Напиши реферат о лыжных гонках",
        "Что такое конфессия?",
        "Напиши ТТХ Автомата Калашникова",
        "Как рассчитать вероятность события?",
        "Напиши вступление проекта о создании telegram бота",
        "Что такое функциональная грамотность?",
    ]

    # Выводим лог в консоль
    logger.debug("[m] {}", msg.text)

    # Проверяем ошибки
    try:
        # Обновляем значение счётчика
        counter(msg.from_user.id, msg.text.split()[0][1:])

        if msg.text == "/chatgpt":
            await msg.answer(
                f'Комманда работает так - <b>"/chatgpt {choice(examples)}"</b>',
                "HTML",
            )
        else:
            # TODO @iamlostshe: answer_msg = await msg.answer('ChatGPT думает...')
            send_text = ask_gpt(
                " ".join(msg.text.split()[1:]),
                msg.from_user.first_name,
            )
            # TODO @iamlostshe: await msg.edit_text(send_text)

            # ВРЕМЕННОЕ РЕШЕНИЕ >>>
            await msg.answer(send_text)

    except Exception as e:
        await msg.edit_text(error(e, msg.from_user.language_code), parse_mode="HTML")
