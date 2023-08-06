# null
# Copyright (C) 2022 Pyro-ManUserbot
# Re-Code by DarkTeam - 2023
# This file is a part of < https://github.com/tracemoepy/DarkPyro-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/tracemoepy/DarkPyro-Userbot/blob/main/LICENSE/>.
# t.me/DiscussionDark & t.me/fuckdvck


from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from ProjectDark import CMD_HELP
from ProjectDark.helpers.basic import edit_or_reply
from ProjectDark.helpers.utility import split_list

@Client.on_message(filters.command("help", CMD_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        help_message = "**DarkPyro-REV Modules:**\n"
        for module in sorted(CMD_HELP.keys()):
            help_message += f"» `{module}`\n"
        await edit_or_reply(message, help_message)
        
    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for cmd, function in commands.items():
                this_command += f"  •  **Command:** `{CMD_HANDLER}{cmd}`\n  •  **Function:** `{function}`\n\n"
            await edit_or_reply(message, this_command, parse_mode=enums.ParseMode.MARKDOWN)
        else:
            await edit_or_reply(message, f"`{help_arg}` **Bukan Nama Modul yang Valid.**")


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
