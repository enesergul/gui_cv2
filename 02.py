import cv2
from tkinter import *
import numpy as np
import pyautogui

resolution = (1920,1080)
continueRecording = True
codec = cv2.VideoWriter_fourcc(*'XVID')
filename = "kayit.avi"
fps = 30
out = cv2.VideoWriter(filename,codec,fps,resolution)

def recordOneFrame():
    global continueRecording
    img = pyautogui.screenshot
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    if continueRecording:
        window.after(round(1/80.*1000),recordOneFrame)
window = Tk()
window.title("Screen Recorder")
window.geometry("400x500")
window.config(bg =  "pink")

def record_Screen():
    window.iconify()
    recordOneFrame()

def stop_Recording():
    global continueRecording 
    continueRecording = False
    window.iconify()
    window.destroy()
    out.release()





recordButton = Button(window,text ="Record(F9)",font=("Bell MT",20),width=20,command=record_Screen)
stopButton = Button(window,text="Stop(F10)", font=("Bell MT",20),width=20,command=stop_Recording)
recordButton.pack(pady=(10,0))
stopButton.pack(pady=(10,0))

mainloop()
cv2.destroyAllWindows()
out.release()

