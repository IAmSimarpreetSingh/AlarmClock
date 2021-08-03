from tkinter import *
from datetime import datetime
from playsound import playsound


def setAlarm():
    alarm_time = time.get("1.0", END)
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_period = alarm_time[6:8].upper()

    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_period = now.strftime("%p")
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    playsound('audio.mp3')
                    break


root = Tk()
root.geometry('400x110')
root.title('Alarm')
photo = PhotoImage(file = "Alarm-clock.png")
root.iconphoto(False, photo)
root.resizable(0, 0)

main_frame = Frame(root, width=400, height=120, bg='light green')
main_frame.pack(fill=X, side=TOP)

format_label = Label(main_frame, text='Time Format HH:MM:P', fg='red', bd=5, bg='light green' )
format_label.pack()

time = Text(main_frame, wrap=WORD, height=1, width=30, bd=2, fg='blue')
time.pack()

set_alarm = Button(main_frame, text='Set Alarm', activebackground='white',activeforeground='black', bg='black', fg='white', bd=2, relief=GROOVE, command=setAlarm)
set_alarm.pack()

info_label = Label(main_frame, text='HH-Hour | MM-Minute | P-Period(am/pm)', fg='black', bd=5, bg='light green')
info_label.pack()

root.mainloop()