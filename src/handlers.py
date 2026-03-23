import asyncio
from aiogram import types, filters, Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from CommandsText import commands


router = Router()

@router.message(filters.Command(commands["start"]))
async def start_handler(msg: Message):
    await msg.reply(
        "Привет! Напиши /help для дополнительной информации."
    )

@router.message(filters.Command(commands["help"]))
async def help_handler(msg: Message):
    await msg.reply(
        "/start - приветственное сообщение"
        "/help - выводит данный текст"
        "/register - запускает регистрацию нового пользователя"
        "/login - войти в свой аккаунт"
        "/add_task [name] [deadline] [priority] [desc] - добавить задачу"
        "/edit_task [id] - редактировать существующую задачу"
        "/complete_task [id] - пометить задачу как выполненную"
        "/delete_task [id] - удалить задачу"
        "/view_tasks [filters/sort] - просмотр списка задач"
        "/reminders [set/edit] - настройка напоминаний"
        "/statistics [period] - просмотр статистики"
        "/set_pin [pin-code] - установить пин-код для задачи"
    )