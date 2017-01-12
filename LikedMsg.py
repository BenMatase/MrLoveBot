MSG_LIM = 40

class LikedMsg:
    def __init__(self, message):
        self.message = message
        self.likers = []

    def __str__(self):
        return "{} [{}]: \"{}\"".format(
            self.message.from_user.username,
            str(len(self.likers)),
            self.limit_length(self.message.text, MSG_LIM)
        )

    def add_liker(self, liker):
        liker_ids = [x.id for x in self.likers]
        if(liker.id not in liker_ids):
            self.likers.append(liker);

    def get_sort_val(self):
        return(len(self.likers))

    def get_reply_id(self):
        return(self.message.message_id)

    def limit_length(self, msg, length):
        if len(msg) > length:
            return msg[:length]
        else:
            return msg
