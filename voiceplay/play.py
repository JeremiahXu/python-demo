#!/usr/bin/python3
# coding=utf-8
import pyttsx3
import random
from playsound import playsound
import time


def play(delay_s):
    voice = pyttsx3.init()
    voice.say("别闹，重置系统就变笨了！就没人喜欢了")
    voice.say("别闹，重置系统就变笨了！就没人喜欢了")
    voice.runAndWait()


if __name__ == '__main__':
    play(4)
