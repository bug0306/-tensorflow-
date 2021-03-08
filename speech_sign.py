import speech_recognition as sr
import cv2
import numpy as np
from translate import Translator


def main():
    text = ""
    r = sr.Recognizer()
    #   device_index=1,
    with sr.Microphone(sample_rate=48000,
                       chunk_size=65536) as source:
        r.adjust_for_ambient_noise(source)
        print("请说一些话。")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='zh-cn')
            print("请你说： " + text)
            translator = Translator(from_lang="chinese", to_lang="english")
            text = translator.translate(str(text))
            pass
        except sr.UnknownValueError:
            print("我不能理解")
        except sr.RequestError as e:
            print("连接到网络")

    for i in text.rstrip():
        if i == " ":
            continue
        img = cv2.imread(".\Letters\\" + str(i).upper() + ".PNG")
        if img is None:
            print(":" + i)
        height, width = img.shape[:2]
        img = cv2.resize(img, (int(width * 2), int(height * 2)), interpolation=cv2.INTER_AREA)
        cv2.imshow('image', img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
