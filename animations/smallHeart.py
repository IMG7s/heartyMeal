from pyrogram import filters
from pyrogram.errors import FloodWait
from time import sleep
from uploadNames import app

def smallHeartAnim():
    @app.on_message(filters.command("heart", prefixes="|") & filters.me)
    def touch(_, msg):
        orig_text = msg.text.split("|heart ", maxsplit=1)[1]
        text = orig_text

        try:
            tbp = 'I♥U'
            msg.edit(tbp)
            sleep(0.1)

            tbp = '🤍🤍\n🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍\n🤍🤍🤍\n🤍🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍🤍\n🤍🤍🤍🤍\n🤍🤍🤍🤍\n🤍🤍🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            #next step
            tbp = '🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍\n❤️❤️❤️❤️❤️\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍🤍🤍🤍🤍\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍❤️🤍❤️🤍\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            #NEXT
            tbp = '🤍🧡🤍🧡🤍\n🧡🧡🧡🧡🧡\n🧡🧡🧡🧡🧡\n🤍🧡🧡🧡🤍\n🤍🤍🧡🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍💛🤍💛🤍\n💛💛💛💛💛\n💛💛💛💛💛\n🤍💛💛💛🤍\n🤍🤍💛🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍💚🤍💚🤍\n💚💚💚💚💚\n💚💚💚💚💚\n🤍💚💚💚🤍\n🤍🤍💚🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍💙🤍💙🤍\n💙💙💙💙💙\n💙💙💙💙💙\n🤍💙💙💙🤍\n🤍🤍💙🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '🤍💜🤍💜🤍\n💜💜💜💜💜\n💜💜💜💜💜\n🤍💜💜💜🤍\n🤍🤍💜🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            #final step
            tbp = '🤍❤️🤍❤️🤍\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n🤍❤️❤️❤️🤍\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n🤍🤍❤️🤍🤍'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️️❤️❤️\n❤️️❤️❤️❤️'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️❤️️\n❤️❤️❤️\n❤️❤️❤️'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❤️❤️️\n❤️❤️'
            msg.edit(tbp)
            sleep(0.45)

            tbp = '❣️ '+text+'\n'+about
            msg.edit(tbp)
            sleep(0.45)

        except FloodWait as e:
            sleep(e.x)