class Database:
    def __init__(self):
        pass

    def insert(self, message):
        # chat_id = message.chat_id
        # reply_id = message.reply_to_message.message_id
        #
        # if(chat_id not in msg_db.keys()):
        #     msg_db[chat_id] = {}
        #
        # if(reply_id not in msg_db[chat_id].keys()):
        #     liked_msg = LikedMsg(message.reply_to_message)
        #     liked_msg.add_liker(message.from_user)
        #     msg_db[chat_id][reply_id] = liked_msg
        # else:
        #     msg_db[chat_id][reply_id].add_liker(message.from_user)
        pass

    def getStr(self, message):
        pass

    def getTopN(self, chat_id, n):
        pass
