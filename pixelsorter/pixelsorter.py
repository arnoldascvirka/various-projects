import cv2
import numpy as np
from PyQt5 import QtGui, QtWidgets, QtCore

class PixelSorter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # sorting start with
        self.sort_by = 'Red'
        self.sort_direction = 'Left'

        # video processing stuff
        self.capture = None
        self.timer = None
        self.is_video = False

    def init_ui(self):
        # window size title weaver
        self.setWindowTitle('most epic sorter')
        self.setGeometry(100, 100, 800, 600)

        # image display
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(10, 10, 780, 480)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setStyleSheet('border: 2px solid black;')

        # sort by dropdown
        self.sort_by_dropdown = QtWidgets.QComboBox(self)
        self.sort_by_dropdown.addItem('Red')
        self.sort_by_dropdown.addItem('Green')
        self.sort_by_dropdown.addItem('Blue')
        self.sort_by_dropdown.setGeometry(10, 500, 200, 30)

        # sort direction dropdown
        self.sort_direction_dropdown = QtWidgets.QComboBox(self)
        self.sort_direction_dropdown.addItem('Left')
        self.sort_direction_dropdown.addItem('Right')
        self.sort_direction_dropdown.addItem('Up')
        self.sort_direction_dropdown.addItem('Down')
        self.sort_direction_dropdown.setGeometry(220, 500, 200, 30)

        # sort
        sort_button = QtWidgets.QPushButton('Sort', self)
        sort_button.setGeometry(430, 500, 100, 30)
        sort_button.clicked.connect(self.sort_pixels)

        # open
        open_button = QtWidgets.QPushButton('Open', self)
        open_button.setGeometry(540, 500, 100, 30)
        open_button.clicked.connect(self.open_file)

        # play/pause
        self.play_pause_button = QtWidgets.QPushButton('Play', self)
        self.play_pause_button.setGeometry(650, 500, 100, 30)
        self.play_pause_button.clicked.connect(self.play_pause)

        self.show()

    def sort_pixels(self):
        # Get sorting variables
        self.sort_by = self.sort_by_dropdown.currentText()
        self.sort_direction = self.sort_direction_dropdown.currentText()

        # Get image data
        image_data = self.get_image_data()

        if image_data is None or image_data.isNull():  # check for None or empty
            return  # return so it doesnt crash

        # Sort pixels
        sorted_data = self.sort_pixels_by_direction(image_data, self.sort_direction)

        # Set sorted data in the image label
        self.set_image_data(sorted_data)

    # get image data
    def get_image_data(self):
        pixmap = self.image_label.pixmap()
        if pixmap is not None:
            image_data = pixmap.toImage()
            if image_data.isNull():  # check if image data is empty
                return None
            else:
                image_data = np.array(image_data)  # Convert QImage to NumPy array
                image_data = image_data.astype(np.uint8)  # Convert to uint8 data type
                image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
                height, width, channels = image_data.shape
                q_image = QtGui.QImage(image_data.data, width, height, channels * width, QtGui.QImage.Format_RGB888)
                return q_image
        else:
            return None


    # convert the image data to a pixmap
    def set_image_data(self, image_data):
        pixmap = QtGui.QPixmap.fromImage(image_data)
        self.image_label.setPixmap(pixmap)

    # convert image data to numpy array
    def sort_pixels_by_direction(self, image_data, direction):
        if image_data is None or image_data.isNull(): # check if image data is empty
            return None

        image_array = np.array(image_data)

        # get dimensions
        height, width, channels = image_array.shape

        # sort by HUE
        if self.sort_by == 'Red':
            sorted_pixels = sorted(image_array.reshape(-1, 3), key=lambda x: x[0])
        elif self.sort_by == 'Green':
            sorted_pixels = sorted(image_array.reshape(-1, 3), key=lambda x: x[1])
        elif self.sort_by == 'Blue':
            sorted_pixels = sorted(image_array.reshape(-1, 3), key=lambda x: x[2])

        # reshape already sorted pixels to og dimensions
        if sorted_pixels:
            sorted_array = np.array(sorted_pixels).reshape(height, width, channels)
        else:
            sorted_array = image_array

        # sort by direction
        if direction == 'Left':
            sorted_array = np.fliplr(sorted_array)
        elif direction == 'Right':
            pass
        elif direction == 'Up':
            sorted_array = np.flipud(sorted_array)
        elif direction == 'Down':
            sorted_array = sorted_array

        # convert back to image
        sorted_data = QtGui.QImage(sorted_array.data, width, height, channels * width, QtGui.QImage.Format_RGB888)

        return sorted_data

    def open_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')

        if file_path:
            self.is_video = False
            image_data = cv2.imread(file_path)
            if image_data is None:
                return  # return if image data is None

            image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
            height, width, channels = image_data.shape
            q_image = QtGui.QImage(image_data.data, width, height, channels * width, QtGui.QImage.Format_RGB888)
            self.set_image_data(q_image)

            # convert to capture object if video
            if file_path.endswith('.mp4') or file_path.endswith('.avi') or file_path.endswith('.flv'):
                self.is_video = True
                self.capture = cv2.VideoCapture(file_path)
                self.timer = QtCore.QTimer(self)
                self.timer.timeout.connect(self.update_frame)
                self.timer.start(30)

    def update_frame(self):
        # read a frame from the video object and set it in the image
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            q_image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            self.set_image_data(q_image)
        else:
            # ;loop if ended
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def play_pause(self):
        if self.is_video:
            if self.capture is None:
                # start playing if nothing is playing
                self.play_pause_button.setText('Pause')
                self.capture = cv2.VideoCapture(self.file_path)
                fps = self.capture.get(cv2.CAP_PROP_FPS)
                self.timer = QtCore.QTimer(self)
                self.timer.timeout.connect(self.next_frame)
                self.timer.start(int(1000/fps))
            else:
                # if nothing is playing, pause it (currently broken)
                self.play_pause_button.setText('Play')
                self.timer.stop()
                self.capture.release()
                self.capture = None
        else:
            # If image is displayed, do nothing
            pass
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = PixelSorter()
    app.exec_()
    


