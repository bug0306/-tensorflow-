import sys
from sign_english_auto import *
import cv2
import speech_recognition as sr
from translate import Translator
import requests
import json
import base64
import os
import re
import logging


class Sign(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_record, QtCore.SIGNAL('clicked()'), self.sign)
        QtCore.QObject.connect(self.ui.pb_trans, QtCore.SIGNAL('clicked()'), self.trans)

    def get_token(self):
        logging.info('开始获取token...')
        # 获取token
        baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
        grant_type = "client_credentials"
        client_id = "up7sdaBHdk09sbMk1l6ijszx"
        client_secret = "XmoFEcE4i8ErqBbnuSlgWb2B81AKXard"

        # 拼url
        url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
        res = requests.post(url)
        token = json.loads(res.text)["access_token"]
        return token
    def audio_baidu(self,filename):
        with open(filename, "rb") as f:
            speech = base64.b64encode(f.read()).decode('utf-8')
        size = os.path.getsize(filename)
        token = self.get_token()
        headers = {'Content-Type': 'application/json'}
        url = "https://vop.baidu.com/server_api"
        data = {
            "format": "wav",
            "rate": "16000",
            "dev_pid": "1536",
            "speech": speech,
            "cuid": "TEDxPY",
            "len": size,
            "channel": 1,
            "token": token,
        }

        req = requests.post(url, json.dumps(data), headers)
        result = json.loads(req.text)

        if result["err_msg"] == "success.":
            print(result['result'])
            return result['result']
        else:
            print("内容获取失败，退出语音识别")
            return -1


    def sign(self):
        self.ui.label.setText("")
        text = ""
        r = sr.Recognizer()

        with sr.Microphone(sample_rate=48000,
                           chunk_size=65536) as source:
            r.adjust_for_ambient_noise(source)
            print("请说：")

            audio = r.listen(source)
        with open("000.wav", "wb") as f:
            # 将麦克风录到的声音保存为wav文件
            f.write(audio.get_wav_data(convert_rate=16000))
        target = self.audio_baidu("000.wav")
        try:
            # text = r.recognize_google(audio,language='zh-cn')
            str1=str(target).strip('[]')
            self.ui.te.setText(str1)
            translator = Translator(from_lang="chinese", to_lang="english")
            str1 = translator.translate(str1)
            str1 = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", '', str1)
            for i in str1:
                if i == " ":
                    continue
                img = cv2.imread("./Letters/" + str(i).upper() + ".PNG")
                if img is None:
                    print(":" + i)
                height, width = img.shape[:2]
                img = cv2.resize(img, (int(width * 2), int(height * 2)), interpolation=cv2.INTER_AREA)
                cv2.imshow('image', img)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()

            pass
        except sr.UnknownValueError:
            self.ui.label.setText("不能理解")
            return False
        except sr.RequestError as e:
            self.ui.label.setText("不能连接网络")
            return False
        self.ui.label.setText("")

    def trans(self):
        str1=str(self.ui.te.toPlainText())
        translator = Translator(from_lang="chinese", to_lang="english")
        str1 = translator.translate(str1)
        str1 = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", '', str1)
        for i in str1:
            if i == " ":
                continue
            img = cv2.imread("./Letters/" + str(i).upper() + ".PNG")
            if img is None:
                print(":" + i)
            height, width = img.shape[:2]
            img = cv2.resize(img, (int(width * 2), int(height * 2)), interpolation=cv2.INTER_AREA)
            cv2.imshow('image', img)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    myapp = Sign()
    myapp.show()
    sys.exit(app.exec_())
