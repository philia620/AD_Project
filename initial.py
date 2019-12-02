from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from block import Block
import sys
import time
from character import *



class Main(QWidget):
    is_first_right = True
    is_first_left = True
    is_first_release_right = True
    is_first_release_left = True
    current_x = 0
    current_y = 0
    def __init__(self, title, gif_file, parent=None):
        QWidget.__init__(self, parent)

        # initial mainWindow
        self.resize(1046, 3772) # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # background
        background_image = QImage('resource/back_ground_1.png')
        modified_background_image = background_image.scaled(QSize(1046, 3772)) # original 1046 x 3772
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # blocks
        block = Block(20000, 1000)
        main_layout.addWidget(block)

        # character
        self.movie = QMovie(gif_file, QByteArray(), self)
        self.character = Character()
        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.character.setAlignment(Qt.AlignCenter)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.character.setMovie(self.movie, self.current_x, self.current_y)
        self.movie.start()
        self.movie.loopCount()
        main_layout.addWidget(self.character)


    def keyPressEvent(self, e):
        self.character.move(self.current_x, self.current_y)
        # right
        if e.key() == Qt.Key_D:
            if self.is_first_right:
                # initial character
                self.character.setVisible(False)
                self.movie = QMovie('resource/avatar_walk1_default_flip.gif', QByteArray(), self)
                self.character.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.is_first_right = False
                self.is_first_left = True
                self.is_first_release_right = True
                print('click')
            # self.character.move(self.current_x + 5, self.current_y)
            self.character.move(self.current_x + 1, self.current_y)
            self.character.setVisible(True)
            self.character.move(self.current_x + 4, self.current_y)
            self.current_x = self.character.pos().x()
            self.current_y = self.character.pos().y()


        # left
        elif e.key() == Qt.Key_A:
            if self.is_first_left:
                # initial character
                self.character.setVisible(False)
                self.movie = QMovie('resource/avatar_walk1_default.gif', QByteArray(), self)
                self.character.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.is_first_right = True
                self.is_first_left = False
                self.is_first_release_left = True
            # self.character.move(self.current_x + 5, self.current_y)
            self.character.move(self.current_x - 1, self.current_y)
            self.character.setVisible(True)
            self.character.move(self.current_x - 4, self.current_y)
            self.current_x = self.character.pos().x()
            self.current_y = self.character.pos().y()


        # up
        elif e.key() == Qt.Key_W:
            self.character.move(self.current_x, self.current_y - 5)
            self.current_x = self.character.pos().x()
            self.current_y = self.character.pos().y()

        # down
        elif e.key() == Qt.Key_S:
            self.character.move(self.current_x, self.current_y + 5)
            self.current_x = self.character.pos().x()
            self.current_y = self.character.pos().y()


    def keyReleaseEvent(self, eventQKeyEvent):
        key = eventQKeyEvent.key()
        print(key)
        # release right
        if key == 68 and not eventQKeyEvent.isAutoRepeat():
            if self.is_first_release_right:
                self.character.setVisible(False)
                print('released')
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.character.move(self.current_x, self.current_y)
                self.movie = QMovie('resource/avatar_stand1_default_flip.gif', QByteArray(), self)
                self.character.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.character.move(self.current_x - 2, self.current_y)
                self.character.setVisible(True)
                self.character.move(self.current_x + 2, self.current_y)
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.is_first_release_right = False
                self.is_first_right = True

        elif key == 65 and not eventQKeyEvent.isAutoRepeat():
            if self.is_first_release_left:
                self.character.setVisible(False)
                print('released')
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.character.move(self.current_x, self.current_y)
                self.movie = QMovie('resource/avatar_stand1_default.gif', QByteArray(), self)
                self.character.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.character.move(self.current_x - 2, self.current_y)
                self.character.setVisible(True)
                self.character.move(self.current_x + 2, self.current_y)
                self.current_x = self.character.pos().x()
                self.current_y = self.character.pos().y()
                self.is_first_release_left = False
                self.is_first_left = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main("update this gif", "resource/avatar_walk1_default.gif")
    main.show()
    sys.exit(app.exec_())
