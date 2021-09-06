from pytube import YouTube
from PyQt6.QtWidgets import QProgressBar

class YT():

    def __init__(self, link, progressBar):
        self.progressBar = QProgressBar()
        self.yt = YouTube(link, on_progress_callback=self.progress_func)
        self.titulo = self.yt.title
        self.thumbnail = self.yt.thumbnail_url
        self.streamsVideos = self.yt.streams.filter(mime_type="video/mp4").asc()
        self.streamsAudio = self.yt.streams.filter(mime_type="audio/mp4").desc()
        self.progressBar = progressBar
        

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

    def getStreamAudio(self, indice):
        return self.getAudio().__getitem__(indice)

    def getProgress(self):
        return self.progressDownload

    def progress_func(self, stream, chunk ,bytes_remaining):
        size = stream.filesize
        progress = (float (abs (bytes_remaining-size)/size)) *float(100)
        print(progress)
        #self.progressBar.setValue(progress)
