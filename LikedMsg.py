class LikedMsg:
    def __init__(self, message):
        self.message = message
        self.likers = []

    def __str__(self):
        return "Message from {} on {} that said \"{}\" with points = {}".format(
            self.message.from_user.username,
            str(self.message.date),
            self.message.text,
            str(len(self.likers))
        )

    def add_liker(self, liker):
        liker_ids = [x.id for x in self.likers]
        if(liker.id not in liker_ids):
            self.likers.append(liker);

    def get_sort_val(self):
        return(len(self.likers))

    def get_reply_id(self):
        return(self.message.message_id)
