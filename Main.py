import sys
import urllib.request

from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from youtubeDownloader import YT

video = None

class Main(QWidget):


    def __init__(self):
        super().__init__()
        uic.loadUi('Views/ventana.ui', self)
        self.btnlink.clicked.connect(self.buscarVideo)
        self.btnVideo.clicked.connect(self.btnDescargarVideo)
        self.btnAudio.clicked.connect(self.btnDescargarAudio)

        self.progressBar = QProgressBar()
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, 100) 



    def btnDescargarVideo(self):
        global video
        dw = video.getStream(self.listaVideo.currentIndex())
        dw.download()


    def btnDescargarAudio(self):
        global video
        dw = video.getStreamAudio(self.listaAudio.currentIndex())
        dw.download()


    def buscarVideo(self):
        global video
        link = self.link.toPlainText()
        video = YT(link, self.progressBar)

        self.titulo.setText(video.getTitulo())
        self.getThumbnail(video)

        self.btnVideo.setEnabled(True)
        self.btnAudio.setEnabled(True)

        self.listaVideo.setEnabled(True)
        self.listaAudio.setEnabled(True)

        self.llenarComboBox(video)


    def llenarComboBox(self, videoData):
        self.listaVideo.clear()
        self.listaAudio.clear()

        streamsV = videoData.getVideos()
        streamsA = videoData.getAudio()
        
        for streamV in streamsV:
            self.listaVideo.addItem(streamV.getResolution())
            
        for streamA in streamsA:
            self.listaAudio.addItem(streamA.getABR())


    def getThumbnail(self, videoData):
        urllib.request.urlretrieve(videoData.getThumbnail(), 'thumbnail.png')
        pixmap = QPixmap('thumbnail.png')
        self.imagen.setPixmap(pixmap)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myApp = Main()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Cerrando ventanda')