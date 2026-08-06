class Codec:

    def __init__(self):
        self.url_map = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        self.id += 1
        shortUrl = "http://tinyurl.com/" + str(self.id)
        self.url_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]