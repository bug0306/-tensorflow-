# 基于TensorFlow的手语识别
This python program is a translator between sign language and english and chinese. Currently only recognizes letters and converts letter by letter.It is currently possible to convert voice into gestures, but the conversion of gestures to voice needs to be improved.
Run `main.py` for the UI and each of the individeual files for other reasons.
<br />
<br />

### Prerequisites
* OpenCV for python - Image processing module. Install by `pip install opencv-python`
* SpeechRecognition - Voice recognition using Google's APIs. Install by `pip install SpeechRecognition`
* PyQt4 - Qt ported to python. Download the .whl here https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4 and install by pip.
* SpeechRecognition - Uses google's APIs to detect speech
* PyAudio - provides Python bindings for PortAudio
* Tensorflow - Machine Learning module for python
* Numpy - Linear algebra for python
* Python 3.X.X - Most python3 versions should work. Install here https://www.python.org/downloads/
<br />

### Files
* `speech_sign.py` - Converts Speech to Sign Language
* `sign_english.py` - Converts Sign Language to English
* `main.py` - Main UI and file to run 

