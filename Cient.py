import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

ResumeButton=Button(window,text="Resume", width=10,bd='SkyBlue',font = ("Calibri",10))
ResumeButton.place(x=30,y=250)

PauseButton=Button(window,text="Pause", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10))
PauseButton.place(x=200,y=250)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

ResumeButton=Button(window,text="Resume", width=10,bd='SkyBlue',font = ("Calibri",10),command = resume)
ResumeButton.place(x=30,y=250)

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_file/'+song_selected)
    mixer.music.pause()

PauseButton=Button(window,text="Pause", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10),command = pause)
PauseButton.place(x=200,y=250)