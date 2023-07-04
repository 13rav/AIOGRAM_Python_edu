from TOKEN import TOKEN_API
from aiogram import Dispatcher, Bot
bot = Bot(TOKEN_API)

list1 = [(bot.send_message), (bot.send_message), 'Кто сегодня будет настоящим пидором в красных кроссовках?', 'Держитесь крепче, вы не готовы к этому!']

list2 = [(bot.send_message), (bot.send_message), (bot.send_message), (bot.send_video), 'Кто сегодня будет освещать танцпол пидорскими движениями?', 'Готовьтесь, огонь разгорается, и пидоры с нами!', 'И вот, главный зажигатель дня... O, нет, накосячил! Оказывается, он всего лишь... пидор', 'CgACAgQAAxkBAAN7ZKPrqSR2MLIoutZ55SBX4N9VKnwAAv4CAAJSXA1TGIuwur40fk4vBA']

chose_list = [list1, list2]
