from urllib.request import urlopen
from threadsafe_tkinter import *

def get_weather(city):
    page = urlopen('https://www.weather.go.kr/weather/observation/currentweather.jsp')
    text = page.read().decode('euckr') #한글로 open
    text = text[text.find(">"+city+"</a>"):] #  text중 .
    for i in range(5):
        text = text[text.find("<td>")+1:]
    start = 3
    end = text.find("</td>")#컬럼 하나씩 가져옴
    tempV.set(u'온도: '+text[start:end])
    print("{} : {}".format(city,text[start:end]))

def refresh(*args):
    get_weather(cities.get())

root = Tk()
root.title("현재 기온")
root.geometry("200x150+200+200")
Label(root, text="도시 : ").pack(side="left")
city_list=["서울","부산","대구","양산시","제주"]
cities = StringVar()
cities.set(city_list[0])
cities.trace("w",refresh)
OptionMenu(root, cities,*city_list).pack(side="right")
tempV=StringVar()
tempV.set("온도 : ")
Label(root, textvariable=tempV).pack(pady=40,side="top")
Button(root,text="Refresh",command = refresh).pack(pady=40, \
    side="bottom")

root.mainloop()
