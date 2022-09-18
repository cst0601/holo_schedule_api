class Schedule:
    """ Hololive schedule structre data
    """

    def __init__(self, time, member, youtube_url):
        self.time = time
        self.member = member
        self.youtube_url = youtube_url

    def to_dict(self):
        return {
            "time": self.time,
            "member": self.member,
            "youtube_url": self.youtube_url
        }