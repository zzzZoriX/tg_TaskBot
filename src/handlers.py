import asyncio
from aiogram import types, filters, Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(filters.Command("start"))
async def start_handler(msg: Message):
    await msg.reply(
        "Привет! Напиши /help для дополнительной информации."
    )

