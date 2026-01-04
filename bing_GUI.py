import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from bing_image_downloader.downloader import download

class DownloadWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int, int)
    log = QtCore.pyqtSignal(str)
    
    def __init__(self, query, limit, output_dir, adult_filter_off, force_replace, timeout):
        super().__init__()
        self.query = query
        self.limit = limit
        self.output_dir = output_dir
        self.adult_filter_off = adult_filter_off
        self.force_replace = force_replace
        self.timeout = timeout

    def run(self):
        download(
            self.query,
            limit=self.limit,
            output_dir=self.output_dir,
            adult_filter_off=self.adult_filter_off,
            force_replace=self.force_replace,
            timeout=self.timeout,
            progress_callback=self.emit_progress,
            log_callback=self.emit_log
        )
        self.finished.emit()

    def emit_progress(self, count, limit):
        self.progress.emit(count, limit)

    def emit_log(self, message):
        self.log.emit(message)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 671, 600))
        self.frame.setStyleSheet("background-color: rgb(61, 56, 70);\n"
"font: 57 11pt \"Ubuntu Sans\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(61, 56, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.search = QtWidgets.QLineEdit(self.frame)
        self.search.setGeometry(QtCore.QRect(132, 80, 421, 27))
        self.search.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"color: rgb(0, 0, 0);\n"
"font: 57 11pt \"Ubuntu Sans\";")
        self.search.setMaxLength(50)
        self.search.setFrame(False)
        self.search.setObjectName("search")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(130, 150, 121, 28))
        self.spinBox.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"color: rgb(0, 0, 0);\n"
"font: 57 11pt \"Ubuntu Sans\";")
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setRange(1, 100)
        self.spinBox.setValue(10) 
        self.spinBox.setObjectName("spinBox")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(130, 120, 181, 19))
        self.label1.setStyleSheet("color: rgb(246, 245, 244);\n"
"font: 57 14pt \"Ubuntu Sans\";")
        self.label1.setObjectName("label1")
        self.Directory = QtWidgets.QLineEdit(self.frame)
        self.Directory.setGeometry(QtCore.QRect(372, 250, 201, 27))
        self.Directory.setStyleSheet("background-color: rgb(246, 245, 244);\n"
"color: rgb(0, 0, 0);\n"
"font: 57 11pt \"Ubuntu Sans\";")
        self.Directory.setObjectName("Directory")
        self.Save = QtWidgets.QPushButton(self.frame)
        self.Save.setGeometry(QtCore.QRect(480, 306, 101, 31))
        self.Save.setStyleSheet("background-color: rgb(61, 56, 70);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.Save.setObjectName("Save")
        self.Cancel = QtWidgets.QPushButton(self.frame)
        self.Cancel.setGeometry(QtCore.QRect(367, 306, 101, 31))
        self.Cancel.setStyleSheet("background-color: rgb(61, 56, 70);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Cancel.setObjectName("Cancel")
        self.checkBox1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox1.setGeometry(QtCore.QRect(130, 190, 161, 25))
        self.checkBox1.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu Sans\";")
        self.checkBox1.setChecked(True)
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox2.setGeometry(QtCore.QRect(130, 230, 161, 25))
        self.checkBox2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 14pt \"Ubuntu Sans\";")
        self.checkBox2.setObjectName("checkBox2")
        self.title_line = QtWidgets.QLabel(self.frame)
        self.title_line.setGeometry(QtCore.QRect(20, 30, 271, 41))
        self.title_line.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Liberation Sans\";")
        self.title_line.setObjectName("title_line")
        
        # Add Progress Bar
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(130, 350, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        
        # Add Progress Label
        self.progressLabel = QtWidgets.QLabel(self.frame)
        self.progressLabel.setGeometry(QtCore.QRect(130, 380, 451, 23))
        self.progressLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Ubuntu Sans\";")
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setText("Downloaded: 0 / 0")
        self.progressLabel.setObjectName("progressLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bing Image Downloader"))
        self.search.setPlaceholderText(_translate("MainWindow", "Search images..."))
        self.label1.setText(_translate("MainWindow", "Limits"))
        self.Directory.setText(_translate("MainWindow", "dataset"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))
        self.checkBox1.setText(_translate("MainWindow", "Adult Filter Off"))
        self.checkBox2.setText(_translate("MainWindow", "Force Replace"))
        self.title_line.setText(_translate("MainWindow", "Bing Image Downloader"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Save.clicked.connect(self.start_download)
        self.Cancel.clicked.connect(self.close)
        self.worker = None

    def start_download(self):
        query = self.search.text()
        if not query:
            self.statusbar.showMessage("Please enter a search term.")
            return

        limit = self.spinBox.value()
        output_dir = self.Directory.text() or "dataset"
        adult_filter_off = self.checkBox1.isChecked()
        force_replace = self.checkBox2.isChecked()
        timeout = 60 

        self.Save.setEnabled(False)
        self.statusbar.showMessage(f"Downloading images for '{query}'...")
        self.progressBar.setValue(0)
        self.progressLabel.setText(f"Downloaded: 0 / {limit}")

        self.worker = DownloadWorker(query, limit, output_dir, adult_filter_off, force_replace, timeout)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.on_download_finished)
        self.worker.start()

    def update_progress(self, count, limit):
        if limit > 0:
            percentage = int((count / limit) * 100)
            self.progressBar.setValue(percentage)
            self.progressLabel.setText(f"Downloaded: {count} / {limit}")

    def on_download_finished(self):
        self.Save.setEnabled(True)
        self.statusbar.showMessage("Download completed!")
        self.progressBar.setValue(100)
        QtWidgets.QMessageBox.information(self, "Success", "Download completed successfully!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
