# null
# Copyright (C) 2022 Pyro-ManUserbot
# Re-Code by DarkTeam - 2023
# This file is a part of < https://github.com/tracemoepy/DarkPyro-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/tracemoepy/DarkPyro-Userbot/blob/main/LICENSE/>.
# t.me/DiscussionDark & t.me/fuckdvck

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from ProjectDark.helpers.basic import edit_or_reply

from .help import add_command_help


@Client.on_message(filters.command("join", cmd) & filters.me)
async def join(client: Client, message: Message):
    Dark = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Berhasil Bergabung ke Chat ID** `{Dark}`")
        await client.join_chat(Dark)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave", "kickme"], cmd) & filters.me)
async def leave(client: Client, message: Message):
    Dark = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group, bye!!")
        await client.leave_chat(Dark)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], cmd) & filters.me)
async def kickmeall(client: Client, message: Message):
    Dark = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Dark.edit(
        f"**Berhasil Keluar dari {done} Group, Gagal Keluar dari {er} Group**"
    )


@Client.on_message(filters.command(["leaveallch"], cmd) & filters.me)
async def kickmeallch(client: Client, message: Message):
    Dark = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Dark.edit(
        f"**Berhasil Keluar dari {done} Channel, Gagal Keluar dari {er} Channel**"
    )


add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "Keluar dari grup dengan menampilkan pesan has left this group, bye!!.",
        ],
        ["leaveallgc", "Keluar dari semua grup telegram yang anda gabung."],
        ["leaveallch", "Keluar dari semua channel telegram yang anda gabung."],
        ["join <UsernameGC>", "Untuk Bergabung dengan Obrolan Melalui username."],
        ["leave <UsernameGC>", "Untuk keluar dari grup Melalui username."],
    ],
)
