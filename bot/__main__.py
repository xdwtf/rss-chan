from telegram import Bot
from .modules.rsshandler import rss_init, session_rss
from bot import BOT_TOKEN, updater, LOGGER

def main():
    # Bot Commands
    bot = Bot(BOT_TOKEN)
    botcmds = [
        ('help', 'To get this message'),
        ('list', 'List your subscriptions'),
        ('get', 'Force fetch last n item(s)'),
        ('sub', 'Subscribe to a RSS feed'),
        ('unsub', 'Remove a specific subscription'),
        ('unsuball', 'Remove all subscriptions'),
    ]

    bot.set_my_commands(botcmds)
    rss_init()
    if session_rss is not None:
        session_rss.start()
        LOGGER.info("Ok SESSION_STRING using for RSS feeds.")

main()
updater.start_polling()
updater.idle()
