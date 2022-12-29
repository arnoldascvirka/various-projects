import pyaudio
import numpy as np
import pyqtgraph as pg
import sounddevice as sd

# Set up PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                frames_per_buffer=1024)

# Set up PyQtGraph
app = pg.QtWidgets.QApplication([])
plot = pg.plot()
plot.setXRange(0, 1024)
plot.setYRange(-30000, 30000)\


# Start the audio stream and visualizer loop
while True:
    data = np.fromstring(stream.read(1024), dtype=np.int16)
    plot.plot(data, clear=True)
    plot.getPlotItem().hideAxis('bottom')
    plot.getPlotItem().hideAxis('left')
    app.processEvents()

# Clean up PyAudio
stream.stop_stream()
stream.close()
p.terminate()