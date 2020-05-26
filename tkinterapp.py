from tkinter import *

root = Tk()
#Label(tk, text='Hello World').pack()
root.title('Event test')
root.geometry('640x400+20+20') #넓이 높이 위치 위치

def callback():
    print('Event 발생!!')

button = Button(root, text='Click', \
    width=20, command=callback)
button.pack(padx=10,pady=10)
root.mainloop() #항상 밑에 있어야 함