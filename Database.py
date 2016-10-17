from sortedcontainers import SortedListWithKey
from LikedMsg import LikedMsg

class Database:
    def __init__(self):
        self.db = {}

    def insert(self, message):
        chat_id = message.chat_id
        reply_id = message.reply_to_message.message_id

        if(chat_id not in self.db.keys()):
            self.db[chat_id] = SortedListWithKey(key=lambda x: -x.get_sort_val())
            self._add_new_liked_msg(message)

        # can proabably eliminate the next two lines by using SortedDict
        pairs = {x.get_reply_id(): x for x in self.db[chat_id]}
        if(reply_id not in pairs.keys()):
            self._add_new_liked_msg(message)
        else:
            pairs[reply_id].add_liker(message.from_user)
            # This is disgusting and needs to be fixed
            self.db[chat_id] = SortedListWithKey(iterable=iter(self.db[chat_id]), key=lambda x: x.get_sort_val())

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
        # top_msgs = [self.db[chat_id][i] for i in range(0,n)]
        return(self.db[chat_id][0:n])

    def getTopNStr(self, chat_id, n):
        top_msgs = self.getTopN(chat_id, n)
        output = 'Top Posts \n'
        i = 1
        for msg in top_msgs:
            output += '{}. {} \n'.format(i, str(msg))
            i += 1
        return(output)
