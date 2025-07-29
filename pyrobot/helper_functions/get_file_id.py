# outdated code :( don't bother reading this shit

from pyrogram.types import Message
from pyrogram.types.messages_and_media import message


def get_file_id(msg: Message):
    if not msg:
        return None
    if msg.media:
        obj = getattr(msg, msg.media.value, None)
        if obj:
            setattr(obj, "message_type", msg.media.value)
            setattr(obj, "message_raw", msg._raw.media)
            return obj
    return None
