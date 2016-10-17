from sortedcontainers import SortedListWithKey
from LikedMsg import LikedMsg

class Database:
    def __init__(self):
        self.db = {}

    def insert(self, message):
        chat_id = message.chat_id
        reply_id = message.reply_to_message.message_id

        if(chat_id not in self.db.keys()):
            self.db[chat_id] = SortedListWithKey(key=lambda x: x.get_sort_val())
            self._add_new_liked_msg(message)

        # can proabably eliminate the next two lines by using SortedDict
        pairs = {x.get_reply_id(): x for x in self.db[chat_id]}
        if(reply_id not in pairs.keys()):
            self._add_new_liked_msg(message)
        else:
            pairs[reply_id].add_liker(message.from_user)

    def _add_new_liked_msg(self, message):
        like_msg = LikedMsg(message.reply_to_message)
        like_msg.add_liker(message.from_user)
        self.db[message.chat_id].add(like_msg)

    def getStr(self, message):
        pairs = {x.get_reply_id(): x for x in self.db[message.chat_id]}
        return(str(pairs[message.reply_to_message.message_id]))

    def getTopN(self, chat_id, n):
        if(n > len(self.db[chat_id])):
            n = len(self.db[chat_id])
        top_msgs = [self.db[chat_id][i] for i in range(0,n)]
        return(top_msgs)

    def getTopNStr(self, chat_id, n):
        top_msgs = self.getTopN(chat_id, n)
        output = ""
        for msg in top_msgs:
            output += str(msg) + "\n"
        return(output)
