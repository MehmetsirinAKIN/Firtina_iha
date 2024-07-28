from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QApplication
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

        # Ana düzen oluştur
        main_layout = QHBoxLayout(self)

        # Sol taraftaki düzen
        left_layout = QVBoxLayout()
        web_view1 = ClickableWebEngineView(self.stream1_url, self)
        web_view1.setStyleSheet("background-color: #E8CDB3; height: 300px; border-radius: 10px; border: 1px solid #070944;")
        left_layout.addWidget(web_view1)
        button1 = QPushButton("Görüntü 1'i Aç", self)
        button1.clicked.connect(lambda: self.open_new_window(self.stream1_url))
        left_layout.addWidget(button1)

        # Sağ taraftaki düzen
        right_layout = QVBoxLayout()
        web_view2 = ClickableWebEngineView(self.stream2_url, self)
        web_view2.setStyleSheet("background-color: #E8CDB3; height: 300px; border-radius: 10px; border: 1px solid #070944;")
        right_layout.addWidget(web_view2)
        button2 = QPushButton("Görüntü 2'yi Aç", self)
        button2.clicked.connect(lambda: self.open_new_window(self.stream2_url))
        right_layout.addWidget(button2)

        # Ana düzeni oluşturulan sol ve sağ düzenleri ekleyerek tamamla
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

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
        new_window.exec_()
