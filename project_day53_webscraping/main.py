from soup import Soup
from bot import FormsBot

souper = Soup()
bot = FormsBot()
details = souper.getDetails()

for detail in details:
  bot.fill(detail)
