from pytube import YouTube

class YT():

    def __init__(self, link):
        yt = YouTube(link)
        self.titulo = yt.title
        self.thumbnail = yt.thumbnail_url
        self.streamsVideos = yt.streams.filter(mime_type="video/mp4").asc()
        self.streamsAudio = yt.streams.filter(mime_type="audio/mp4").desc()
        

    def getTitulo(self):
        return self.titulo
    
    def getVideos(self):
        return self.streamsVideos

    def getAudio(self):
        return self.streamsAudio

    def getThumbnail(self):
        return self.thumbnail

    def getStream(self, indice):
        return self.getVideos().__getitem__(indice)

