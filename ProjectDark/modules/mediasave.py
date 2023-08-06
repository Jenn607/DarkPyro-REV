# GAADA CREDITS SEMUANYA DI TANGGUNG AJI KONTOL


import os
from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaDocument
from pyrogram.errors import RPCError

from ProjectDark.helpers.tools import get_arg
from config import CMD_HANDLER as cmd
from .help import add_command_help



@Client.on_message(filters.command("save", cmd) & filters.me)
async def pencuri(client, message):
        rep = message.reply_to_message

        if not rep:
            await message.reply("Reply to media.")
            return

        cap = rep.caption or None
        mmk = await message.reply("Please wait...")
        await mmk.delete()

        if rep.text:
            await dia.copy("me")
            await message.delete()
        elif rep.photo:
            anu = await client.download_media(rep)
            await client.send_photo("me", anu, cap)
            await message.delete()
            os.remove(anu)
        elif rep.video:
            anu = await client.download_media(rep)
            await client.send_video("me", anu, cap)
            await message.delete()
            os.remove(anu)
        elif rep.audio:
            anu = await client.download_media(rep)
            await client.send_audio("me", anu, cap)
            await message.delete()
            os.remove(anu)
        elif rep.voice:
            anu = await client.download_media(dia)
            await client.send_voice("me", anu, cap)
            await message.delete()
            os.remove(anu)
        elif rep.document:
            anu = await client.download_media(rep)
            await client.send_document("me", anu, cap)
            await message.delete()
            os.remove(anu)


add_command_help(
  "mediasave",
  [
    ["save", "to save the photo with timer"],
  ],
)
