from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QDialog, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class ClickableWebEngineView(QWebEngineView):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.url = url
        self.setUrl(QUrl(url))

    def mousePressEvent(self, event):
        self.parent().open_new_window(self.url)

class CameraWidget(QWidget):
    def __init__(self, stream1_url, stream2_url, parent=None):
        super().__init__(parent)
        
        self.stream1_url = stream1_url
        self.stream2_url = stream2_url

        # Stil ve boyut ayarları
        self.setStyleSheet("background-color: #34495E; border-radius: 10px; border: 1px solid #070944; ")

        # Ana düzen oluştur
        layout = QHBoxLayout(self)

        # İlk web view oluştur ve stili ayarla
        web_view1 = ClickableWebEngineView(self.stream1_url, self)
        web_view1.setStyleSheet("background-color: #E8CDB3; height: 300px; border-radius: 10px; border: 1px solid #070944;")
        layout.addWidget(web_view1)

        # İkinci web view oluştur ve stili ayarla
        web_view2 = ClickableWebEngineView(self.stream2_url, self)
        web_view2.setStyleSheet("background-color: #E8CDB3; height: 300px; border-radius: 10px; border: 1px solid #070944;")
        layout.addWidget(web_view2)

        self.setLayout(layout)

    def open_new_window(self, stream_url):
        # Yeni pencere oluştur
        new_window = QDialog(self)
        new_window.setWindowTitle("Yeni Pencere")
        new_window.setGeometry(750, 150, 900, 550)  # Örnek boyut ve konum
        
        # Web view oluştur
        web_view = QWebEngineView(new_window)
        web_view.setUrl(QUrl(stream_url))
        
        # Web view düzeni
        layout = QVBoxLayout(new_window)
        layout.addWidget(web_view)
        
        new_window.setLayout(layout)
        new_window.exec_()  # Pencereyi modal olarak göstermek için exec_() kullanabilirsiniz

