import getpass
from bot import InternetSpeedTwitterBot

username = input("Username: ")
password = getpass.getpass()

bot = InternetSpeedTwitterBot(username, password)
bot.getInternetSpeed()
bot.tweetAtProvider()
