import tkinter as tk
import requests

window = tk.Tk()
window.geometry("300x300")
window.title("meteorological")

lblNotFound = tk.Label(window)
lblTemp = tk.Label(window)
lblpressure = tk.Label(window)
lblhumidity = tk.Label(window)
lbldesc = tk.Label(window)

def show():

    cityName = entry.get()
    api_key = "908a628a1815decea0de4a816a516291"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    org_url = base_url + cityName + "&appid=" + api_key
    print(org_url)

    x = requests.get(org_url)
    y = x.json()

    if y["cod"] == "404":

        lblNotFound.config("city not found !")
        lblNotFound.pack()

    else:

        z = y["main"]
        t = z['temp']
        temp = t - 273.15
        lblTemp.config("temp = " + str(round(temp,2)) + " C")

        pressure = z['pressure']
        lblpressure.config("pressure = " + str(pressure) + " hpa")

        humidity = z['humidity']
        lblhumidity.config("humidity = " + str(humidity) + " %")

        desc = y['weather']
        descmain = desc[0]["description"]
        lbldesc.config("description = " + descmain)

        lblTemp.pack()
        lblpressure.pack()
        lblhumidity.pack()
        lbldesc.pack()


label = tk.Label(window,text="enter your city name : ")
label.pack()

entry = tk.Entry(window)
entry.pack()

btn1 = tk.Button(window,text = "show information",command=show)
btn1.pack()

window.mainloop()