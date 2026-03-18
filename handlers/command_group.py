from aiogram import types, Router, Bot
from filter.filters import ChatTypeFilter

router_group_user = Router()
router_group_user.message.filter(ChatTypeFilter(["group", "supergroup"]))

restricted_words = {
    'дурак', 'идиот', 'глупец', 'тупой', 'кретин', 'мразь', 'сволочь', 'урод',
    'дебил', 'придурок', 'засранец', 'тварь', 'скотина', 'гнида', 'сука',
    'падла', 'ублюдок', 'шлюха', 'проститутка', 'блядь', 'хрен', 'чмо',
    'козёл', 'баран', 'осёл', 'мерзавец', 'жопа', 'пизда', 'мудак', 'лох',
    'гандон', 'пидор', 'гей', 'тупица', 'недоумок', 'говно', 'задница',
    'петух', 'курва', 'шваль', 'хренов', 'шалава', 'говнюк', 'козлина'
}

@router_group_user.message()
async def group_command(message: types.Message, bot: Bot):
    if message.text.lower() in restricted_words:
        await bot.send_message(bot.my_admin_list[0], f"{message.from_user.id} used restricted words")