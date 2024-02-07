import requests

class Episode:
    def __init__(self, providerId, episodeId, title, episodeNumber, id):
        self.episodeId = episodeId
        self.providerId = providerId
        self.title = title
        self.episodeNumber = episodeNumber
        self.id = id
        self.subType = 'sub'
    
    def source(self):
        url = "https://api.anify.tv/sources?providerId=" + str(self.providerId) + "&watchId=%2F" + str(self.episodeId) + "&episodeNumber=" + str(self.episodeNumber) + "&id=" + str(self.id) + "&subType=" + self.subType
        #url = "https://api.anify.tv/sources?providerId=gogoanime&watchId=%2Fkubo-san-wa-mob-wo-yurusanai-episode-10&episodeNumber=10&id=148969&subType=sub"
        response = requests.get(url)
        data = response.json()
        return data