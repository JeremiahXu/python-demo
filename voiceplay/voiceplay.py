#!/usr/bin/python3
# coding=utf-8
import pyttsx3
import random
from playsound import playsound
import time


def play(delay_s):
    volume_list = ["dou","re","mi","fa","so","拉","see"]
    voice=pyttsx3.init()

    #voice.say("开始播报七音节")
    #voice.runAndWait()

    voice.say("别闹，重置系统就变笨了！就没人喜欢了")
    voice.runAndWait()
    
    # for i in range(10000):
    #     voice.say(volume_list[random.randint(0,len(volume_list)-1)])
    #     voice.runAndWait()
    #     #time.sleep(0.1)
    #     #voice.say(volume_list[random.randint(0,len(volume_list)-1)])
    #     #voice.runAndWait()
    #     time.sleep(delay_s)
        

if __name__ == '__main__':
    play(4)
