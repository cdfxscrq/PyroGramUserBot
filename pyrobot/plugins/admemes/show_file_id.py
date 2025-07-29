"""Get id of the replied user
Syntax: .id"""

from pyrogram import Client, filters
from pyrogram.file_id import FileId
from pyrogram.enums import ChatType
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import f_onw_fliter
from pyrobot.helper_functions.get_file_id import get_file_id


@Client.on_message(filters.command(["id"], COMMAND_HAND_LER) & f_onw_fliter)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == ChatType.PRIVATE:
        _id = ""
        _id += f"<b>User ID</b>: <code>{message.from_user.id}</code>\n"
        file_info = get_file_id(message.reply_to_message)
        if file_info:
            file_id = file_info.file_id
            d_file_id = FileId.decode(file_id)
            _id += f"<b>DC ID</b>: <code>{d_file_id.dc_id}</code>\n"
        await message.reply_text(_id, quote=True)

    elif chat_type in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        _id = ""
        _id += f"<b>Chat ID</b>: <code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
            if file_info:
                _id += (
                    f"<b>{file_info.message_type}</b>: "
                    f"<code>{file_info.file_id}</code>\n"
                )
                d_file_id = FileId.decode(file_info.file_id)
                _id += f"<b>DC ID</b>: <code>{d_file_id.dc_id}</code>\n"
        else:
            _id += f"<b>User ID</b>: <code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
            if file_info:
                _id += (
                    f"<b>{file_info.message_type}</b>: "
                    f"<code>{file_info.file_id}</code>\n"
                )
                d_file_id = FileId.decode(file_info.file_id)
                _id += f"<b>DC ID</b>: <code>{d_file_id.dc_id}</code>\n"
        await message.reply_text(_id, quote=True)
