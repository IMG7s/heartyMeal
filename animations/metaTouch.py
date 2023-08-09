from pyrogram import filters
from pyrogram.errors import FloodWait
from time import sleep
from uploadNames import *


def linePrinter():
    @app.on_message(filters.command("touch", prefixes="|") & filters.me)
    def touch(_, msg):
        orig_text = msg.text.split("|touch ", maxsplit=1)[1]
        text = orig_text
        tbp = ""
        typing_symbol = "_"

        while (tbp != orig_text):
            try:
                msg.edit(tbp + typing_symbol)
                sleep(0.1)

                tbp = tbp + text[0]
                text = text[1:]

                msg.edit(tbp)
                sleep(0.05)

            except FloodWait as e:
                sleep(e.x)