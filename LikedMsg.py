class LikedMsg:
    def __init__(self, message):
        self.message = message
        self.count = 1

    def __str__(self):
        return "Message from {} on {} that said \"{}\" with points = {}".format(
            self.message.from_user.username,
            str(self.message.date),
            self.message.text,
            str(self.count)
        )
