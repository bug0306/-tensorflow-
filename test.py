import speech_recognition as sr
import cv2
import numpy as np
text = ""
r = sr.Recognizer()

with sr.Microphone(device_index=1, sample_rate=48000,
                   chunk_size=2048) as source:
    r.adjust_for_ambient_noise(source)
    print("说一些话")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("你说： " + text)
        pass
    except sr.UnknownValueError:
        print("你好，我不能理解")
    except sr.RequestError as e:
        print("请连接网络")

for i in text.rstrip():
    if i == " ":
        continue
    img = cv2.imread(".\Letters\\"+str(i).upper()+".PNG")
    if img is None:
        print(":"+i)
    height, width = img.shape[:2]
    img = cv2.resize(img, (int(width*2),int(height*2)), interpolation=cv2.INTER_AREA)
    cv2.imshow('image', img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
