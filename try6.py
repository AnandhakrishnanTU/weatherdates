from atexit import register
from tkinter import *
import tkinter
from unicodedata import name
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector

root=tkinter.Tk()
root.state('zoomed')

def btn_clicked():
    print("Button Clicked")

#############   frames    ###########

homepage = tkinter.Frame(root)
weatherpage = tkinter.Frame(root)
loginpage = tkinter.Frame(root)
mappage=tkinter.Frame(root)
alertpage=tkinter.Frame(root)
newspage=tkinter.Frame(root)
signuppage=tkinter.Frame(root)
deletepage=tkinter.Frame(root)

######    weather details   #######
rain=PhotoImage(file="rain_alert.png")
summer=PhotoImage(file="summer_alert.png")
winter=PhotoImage(file="winter_alert.png")
good=PhotoImage(file="good_alert.png")


###### getweather ######


def getWeather():
    try:
        city=entry0.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT TIME")

                
        #latitude&longitude

        loc = Nominatim(user_agent="GetLoc")

        getLoc = loc.geocode(city)

        Latitude = getLoc.latitude
        Longitude = getLoc.longitude

        #map screenshot

        options = Options()
        #options.add_argument("--headless")
        options.headless = True
        driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
        zoom = 10
        s1 = "https://www.windy.com/"
        s2 = str(Latitude)
        s3 = "/"
        s4 = str(Longitude)
        s5 = "?rain,"
        s6 = ","
        s7 = str(zoom)
        url = s1+s2+s3+s4+s5+s2+s3+s4+s6+s7
        driver.get(url)
        driver.set_window_position(1600,700)
        time.sleep(2)
        driver.save_screenshot('image.png')
        driver.quit




        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1e159b5580645c327caf30a16228fcb3"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"),fg="#a10606")
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"),fg="#a10606")

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

        if temp>=30:
            label24=Label(alert_page,image=summer)
            label24.place(x=800,y=270)
        elif 25<=temp<30: 
            label25=Label(alert_page,image=good)
            label25.place(x=800,y=270)         
        elif 10<=temp<25:
            label26=Label(alert_page,image=rain)
            label26.place(x=800,y=270)
        else:
            label27=Label(alert_page,image=winter)
            label27.place(x=800,y=270)    

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")


#### getweather1 ######
        
def getWeather1():
    try:
        city=entry6.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock1.config(text=current_time)
        name1.config(text="CURRENT TIME")

                
        #latitude&longitude

        loc = Nominatim(user_agent="GetLoc")

        getLoc = loc.geocode(city)

        Latitude = getLoc.latitude
        Longitude = getLoc.longitude


        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1e159b5580645c327caf30a16228fcb3"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        a.config(text=(temp,"°"),fg="#a10606")
        b.config(text=(condition,"|","FEELS","LIKE",temp,"°"),fg="#a10606")

        q.config(text=wind)
        r.config(text=humidity)
        s.config(text=description)
        u.config(text=pressure)
           
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")        



def btn_clicked():
    print("Button Clicked")



def login_message():
    messagebox.showerror("error","please login to use this feature")



######  news fetching ######

def getNews():
    api_key = "ccc5ba067b6d47fbb293df808d78249c"
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]


    my_articles = []
    my_news = ''

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " +my_articles[i] + "\n" + "\n"
    label.config(text=my_news)

###### home page #######

home_page = Canvas(
    homepage,
    bg = 'white',
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
home_page.place(x = 0, y = 0)

home_background = PhotoImage(file="weather_background_1.png")
background = home_page.create_image(766, 398,image=home_background)


entry6_img = PhotoImage(file = f"textbox.png")
entry6_bg = home_page.create_image(
    488, 420,
    image = entry6_img)

entry6 = Entry(homepage,font=("poppins",23,"bold"),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry6.place(
    x = 345, y = 401,
    width = 283.0,
    height = 37)


img7 = PhotoImage(file = f"login.png")
b25 = Button(homepage,
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: [print("button_2 clicked"),homepage.place_forget(),loginpage.place(x=0,y=0,height=1080,width=1920)],
    relief = "flat")

b25.place(
    x = 700, y = 60,
    width = 69,
    height = 26)

img8 = PhotoImage(file = f"weather.png")
b26 = Button(homepage,
    image = img8,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b26.place(
    x = 950, y = 55,
    width = 86,
    height = 20)

img9 = PhotoImage(file = f"alerts.png")
b27 = Button(homepage,
    image = img9,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = login_message,
    relief = "flat")

b27.place(
    x = 1100, y = 55,
    width = 59,
    height = 22)

img10 = PhotoImage(file = f"map.png")
b28 = Button(homepage,
    image = img10,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = login_message,
    relief = "flat")

b28.place(
    x = 1250, y = 55,
    width = 46,
    height = 20)

img11 = PhotoImage(file = f"news.png")
b29 = Button(homepage,
    image = img11,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = login_message,
    relief = "flat")

b29.place(
    x = 1400, y = 55,
    width = 55,
    height = 20)

img12 = PhotoImage(file = f"search_lens.png")
b30 = Button(homepage,
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = getWeather1,
    relief = "flat")

b30.place(
    x = 602, y = 407,
    width = 24,
    height = 24)


#time
name1=Label(homepage,font=("arial",15,"bold"),fg="black",bg="white")
name1.place(x=1300,y=150)
clock1=Label(homepage,font=("Helvetica",20),fg="black",bg="white")
clock1.place(x=1300,y=190)

#data
label16=Label(homepage,text="WIND               :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label16.place(x=940,y=284)

label17=Label(homepage,text="HUMIDITY        :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label17.place(x=940,y=344)

label8=Label(homepage,text="DESCRIPTION :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label8.place(x=940,y=404)

label9=Label(homepage,text="PRESSURE     :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label9.place(x=940,y=464)

a=Label(homepage,font=("arial",70,"bold"),fg="#a10606",bg="white")
a.place(x=1320,y=262)
b=Label(homepage,font=("arial",12,'bold'),bg="white")
b.place(x=1320,y=382)

q=Label(homepage,text="...",font=("arial",20,"bold"),bg="white")
q.place(x=1100,y=280)

r=Label(homepage,text="...",font=("arial",20,"bold"),bg="white")
r.place(x=1100,y=340)

s=Label(homepage,text="...",font=("arial",20,"bold"),bg="white")
s.place(x=1100,y=400)

u=Label(homepage,text="...",font=("arial",20,"bold"),bg="white")
u.place(x=1100,y=460)

###### weather page    ########

def delete():
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="weatherdates",autocommit=True)
    mycur=mydb.cursor()
    val=(entry1.get(),entry2.get())
    url4=("delete from reglist where uname = %s and pass =%s")
    mycur.execute(url4,val)
    messagebox.showinfo("success","Account has been deleted Successfully!!!")
    weatherpage.place_forget(),loginpage.place(x=0,y=0,height=1080,width=1920)       

    mydb.close()


weather_page = Canvas(
    weatherpage,
    bg = 'white',
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
weather_page.place(x = 0, y = 0)

weather_background = PhotoImage(file="weather_background_1.png")
background = weather_page.create_image(766, 398,image=weather_background)

entry0_img = PhotoImage(file = f"textbox.png")
entry0_bg = weather_page.create_image(
    488, 420,
    image = entry0_img)

entry0 = Entry(weatherpage,font=("poppins",23,"bold"),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 345, y = 401,
    width = 283.0,
    height = 37)


b0 = Button(weatherpage,
    text = "Logout",font=("poppnis",14),fg="white",bg="#1f1e1d",
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: [print("button_2 clicked"),weatherpage.place_forget(),homepage.place(x=0,y=0,height=1080,width=1920)],
    relief = "flat")

b0.place(
    x = 700, y = 730,
    width = 69,
    height = 26)

b20 = Button(weatherpage,text="Delete Account",font=("poppins",14),fg="white",bg="#1f1e1d",
    borderwidth=0,highlightthickness=0,command=delete,relief="flat")

b20.place(x=45,y=730,width=150,height=26)    

img1 = PhotoImage(file = f"weather.png")
b1 = Button(weatherpage,
    image = img1,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 950, y = 55,
    width = 86,
    height = 20)

img2 = PhotoImage(file = f"alerts.png")
b2 = Button(weatherpage,
    image = img2,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = lambda:[weatherpage.place_forget(),alertpage.place(x=0,y=0,height=1080,width=1920)],
    relief = "flat")

b2.place(
    x = 1100, y = 55,
    width = 59,
    height = 22)

img3 = PhotoImage(file = f"map.png")
b3 = Button(weatherpage,
    image = img3,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = lambda: [print("button_2 clicked"),weatherpage.place_forget(),mappage.place(x=0,y=0,height=1080,width=1920)],
    relief = "flat")

b3.place(
    x = 1250, y = 55,
    width = 46,
    height = 20)

img4 = PhotoImage(file = f"news.png")
b4 = Button(weatherpage,
    image = img4,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = lambda:[weatherpage.place_forget(),newspage.place(x=0,y=0,height=1080,width=1920)],
    relief = "flat")

b4.place(
    x = 1400, y = 55,
    width = 55,
    height = 20)

img5 = PhotoImage(file = f"search_lens.png")
b5 = Button(weatherpage,
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = getWeather,
    relief = "flat")

b5.place(
    x = 602, y = 407,
    width = 24,
    height = 24)

#time
name=Label(weatherpage,font=("arial",15,"bold"),fg="black",bg="white")
name.place(x=1300,y=150)
clock=Label(weatherpage,font=("Helvetica",20),fg="black",bg="white")
clock.place(x=1300,y=190)

#data
label1=Label(weatherpage,text="WIND               :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label1.place(x=940,y=284)

label2=Label(weatherpage,text="HUMIDITY        :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label2.place(x=940,y=344)

label3=Label(weatherpage,text="DESCRIPTION :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label3.place(x=940,y=404)

label4=Label(weatherpage,text="PRESSURE     :",font=("Helvetica",15,'bold'),fg="black",bg="white")
label4.place(x=940,y=464)

t=Label(weatherpage,font=("arial",70,"bold"),fg="#a10606",bg="white")
t.place(x=1320,y=262)
c=Label(weatherpage,font=("arial",12,'bold'),bg="white")
c.place(x=1320,y=382)

w=Label(weatherpage,text="...",font=("arial",20,"bold"),bg="white")
w.place(x=1100,y=280)

h=Label(weatherpage,text="...",font=("arial",20,"bold"),bg="white")
h.place(x=1100,y=340)

d=Label(weatherpage,text="...",font=("arial",20,"bold"),bg="white")
d.place(x=1100,y=400)

p=Label(weatherpage,text="...",font=("arial",20,"bold"),bg="white")
p.place(x=1100,y=460)



###### login page #######

def userlogin():

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="weatherdates",autocommit=True)
    mycur=mydb.cursor()
    if entry1.get()=='' or entry2.get()=='':
        messagebox.showerror("Error","all field required")
        
    url3=("select * from reglist;")
    mycur.execute(url3)
    datas=mycur.fetchall()
    flag1=0
    flag2=0
    if entry1.get():
           
        #print(datas)
        #print(datas[1][1])
        for i in range(len(datas)):
            if datas[int(i)][0]==entry1.get():   
                flag1=1
                break
                    
        if flag1==0:
            messagebox.showerror("Error","user Doesnt  exists !!!")
    if entry2.get() and flag1:
        url4=("select pass from reglist where uname=%s;")
        #print(logentry0.get())
        pass2=[entry1.get()]
        #print(pass2)
        mycur.execute(url4,pass2)
        uname1=mycur.fetchone()
        #print(uname1)
        #print(datas[1][1])
        if uname1[0]==entry2.get():
            flag2=1
                    
        if flag2==0:
            messagebox.showerror("Error","Invalid password !!!")        
        else:
            loginpage.place_forget(),weatherpage.place(x=0,y=0,height=1080,width=1920)
    
login_page = Canvas(loginpage,height=1080,width=1920,bg="white",bd=0,highlightthickness=0,relief="ridge")
login_page.place(x=0,y=0)

login_background = PhotoImage(file = "login_Background.png")
background = login_page.create_image(
    1200, 380,
    image=login_background)

label5=Label(loginpage,text="LOGIN",font=("poppins",50,'bold'),fg="black",bg="white")
label5.place(x=100,y=150)

label6=Label(loginpage,text="Username*",font=("times new roman",18),fg="black",bg="white")
label6.place(x=150,y=300)

b7=Button(loginpage,text="Home",font=("poppins",16,"bold"),borderwidth=0,bg="white",highlightthickness=0,
    command=lambda: [print("button_2 clicked"),loginpage.place_forget(),homepage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b7.place(x=500,y=62,height=50,width=100)

label8=Label(loginpage,text="Not registered yet ?",font=("poppins",12),fg="black",bg="white")
label8.place(x=150,y=550)

b8=Button(loginpage,text="Create an account",font=("poppnis",12),borderwidth=0,fg="blue",bg="white",
    highlightthickness=0,relief="flat",command=lambda:[loginpage.place_forget(),signuppage.place(x=0,y=0,height=1080,
        width=1920)])
b8.place(x=300,y=550)


entry1_img = PhotoImage(file = "textbox.png")
entry1_bg = login_page.create_image(
    290, 360,
    image = entry1_img)

entry1 = Entry(loginpage,font=("poppins",15),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 190, y = 345,
    width = 210,
    height = 28)


label7=Label(loginpage,text="Password*",font=("times new roman",18),fg="black",bg="white")
label7.place(x=150,y=400)

logo_image=PhotoImage(file="logo.png")
myimage=Label(loginpage,image=logo_image,bg="white")
myimage.place(x=100,y=60)

weatherdates=PhotoImage(file="weatherdates.png")
weather_image=Label(loginpage,image=weatherdates,bg="white")
weather_image.place(x=160,y=75)


entry2_img = PhotoImage(file = "textbox.png")
entry2_bg = login_page.create_image(
    290, 460,
    image = entry2_img)


entry2 = Entry(loginpage,font=("poppins",15),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 190, y = 445,
    width = 210,
    height = 28)    

img6 = PhotoImage(file = f"login_button.png")
b6 = Button(loginpage,
    image = img6,
    borderwidth = 0,bg="white",
    highlightthickness = 0,
    command = userlogin,
    relief = "flat")

b6.place(
    x = 170, y = 500,
    width = 250,
    height = 40)



######## signup page #########

def register():
    
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="weatherdates",autocommit=True)
            mycur=mydb.cursor()
            if entry3.get()=='' or entry4.get()=='' or entry5.get()=='':
                messagebox.showerror("Error","all field required")
            
            fmail=0
            funame=0
            fpass=0

            if entry3.get():
                url=("select * from reglist;")
                mycur.execute(url)
                datas=mycur.fetchall()
                #print(datas)
                #print(datas[1][1])
                for i in range(len(datas)):
                    if datas[int(i)][0]==entry3.get():
                        messagebox.showerror("Error","user already exist")
                    else:
                        funame=1
            if entry4.get():
                flag1=0
                for i in entry4.get():
                    if i=="@":
                        flag1 =1
                if flag1==0:
                    messagebox.showerror("Error","Invalid email!!!")
                else:
                    fmail=1
            if entry5.get():
                paschk=entry5.get()
                l=int(0)
                u=int(0)
                d=int(0)
                p=int(0)
                if (len(paschk) >= 8):
                    for i in paschk:
            
                        # counting lowercase alphabets
                        if (i.islower()):
                            l+=1           
                
                        # counting uppercase alphabets
                        if (i.isupper()):
                            u+=1           
                
                        # counting digits
                        if (i.isdigit()):
                            d+=1           
                
                        # counting the mentioned special characters
                        if(i=='!'or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='(' or i==')' or i=='_' or i=='-' or i=='+' or i=='=' or i=='[' or i==']' or i=='{' or i=='}' or i==';' or i==':' or i=='"' or i=='/' or i==' \ ' or i=='?' or i=='>' or i=='<' or i=='.' or i==',') or i=='|':
                            p+=1          
                        
                if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(paschk)):
                        fpass=1
                else:
                        messagebox.showerror("Error","Invalid password format!!!")   
            if funame==1 and fmail==1 and fpass==1:
                val=(entry3.get(),entry4.get(),entry5.get())
                url1=("insert into reglist value(%s,%s,%s)")
                mycur.execute(url1,val)
                messagebox.showinfo("success","Account has been Created Successfully!!!")
            





            mydb.close()

signup_page = Canvas(signuppage,height=1080,width=1920,bg="white",bd=0,highlightthickness=0,relief="ridge")
signup_page.place(x=0,y=0)

signup_background=PhotoImage(file="signup_background.png")
background=signup_page.create_image(470,390,image=signup_background)

label9=Label(signuppage,text="SIGN UP",font=("poppins",50,"bold"),fg="black",bg="white")
label9.place(x=1100,y=100)


lable10=Label(signuppage,text="User Name*",font=("times new roman",18),fg="black",bg="white")
lable10.place(x=1000,y=200)

lable11=Label(signuppage,text="Email id*",font=("times new roman",18),fg="black",bg="white")
lable11.place(x=1000,y=320)

lable12=Label(signuppage,text="Password*",font=("times new roman",18),fg="black",bg="white")
lable12.place(x=1000,y=440)

entry3_img = PhotoImage(file = "textbox.png")
entry3_bg = signup_page.create_image(
    1200, 278,
    image = entry1_img)

entry3 = Entry(signuppage,font=("poppins",15),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 1055, y = 264,
    width = 280,
    height = 28)

entry4_img = PhotoImage(file = "textbox.png")
entry4_bg = signup_page.create_image(
    1200, 398,
    image = entry1_img)

entry4 = Entry(signuppage,font=("poppins",15),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 1055, y = 384,
    width = 280,
    height = 28)

entry5_img = PhotoImage(file = "textbox.png")
entry5_bg = signup_page.create_image(
    1200, 518,
    image = entry1_img)

entry5 = Entry(signuppage,font=("poppins",15),
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 1055, y = 504,
    width = 280,
    height = 28)

register_button=PhotoImage(file="register.png")
b10=Button(signuppage,image=register_button,bg="#bedff7",borderwidth=0,highlightthickness=0,relief="flat",command=register)
b10.place(x=1080,y=560)

label13=Label(signuppage,text="Already have an account ?",font=("times new roman",12),fg="black",bg="white")
label13.place(x=1080,y=600)

b11=Button(signuppage,text="Login",font=("times new roman",13,"bold"),bg="white",fg="blue",borderwidth=0,
    highlightthickness=0,relief="flat",
    command=lambda:[signuppage.place_forget(),loginpage.place(x=0,y=0,height=1080,width=1920)])
b11.place(x=1250,y=600) 

b12=Button(signuppage,text="Home",font=("poppins",16,"bold"),borderwidth=0,bg="white",highlightthickness=0,
    command=lambda: [print("button_2 clicked"),signuppage.place_forget(),homepage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b12.place(x=800,y=55,height=40,width=100)


label18=Label(signup_page,text="*password should contain uppercase alphabets,"+
    "\n"+"lowercase alphabets,numeric characters"+"\n"+"and special symbols",font=("poppins",12),fg="red",bg="white")
label18.place(x=1050,y=650)        

########## alert page   ##############

alert_page=Canvas(alertpage,height=1080,width=1920,bg="white",bd=0,highlightthickness=0,relief="ridge")
alert_page.place(x=0,y=0)

alert_background=PhotoImage(file="alert_background.png")
background = alert_page.create_image(384,395,image=alert_background)

b13=Button(alertpage,text="Weather",font=("poppins",16,"bold"),borderwidth=0,fg="black",bg="white",highlightthickness=0,
    command=lambda: [alertpage.place_forget(),weatherpage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b13.place(x=900,y=55,height=40,width=100)

b14=Button(alertpage,text="Alerts",font=("poppins",16,"bold"),borderwidth=0,fg="black",bg="white",highlightthickness=0,
    command=btn_clicked)
b14.place(x=1050,y=55,height=40,width=100)

b15=Button(alertpage,text="Map",font=("poppins",16,"bold"),borderwidth=0,fg="black",bg="white",highlightthickness=0,
    command=lambda: [alertpage.place_forget(),mappage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b15.place(x=1200,y=55,height=40,width=100)

b16=Button(alertpage,text="News",font=("poppins",16,"bold"),borderwidth=0,fg="black",bg="white",highlightthickness=0,
    command=lambda: [alertpage.place_forget(),newspage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b16.place(x=1350,y=55,height=40,width=100)

label14=Label(alertpage,text="The Only Weather Forecast You Need",font=("poppins",24),fg="white",bg="#1f1e1d")
label14.place(x=160,y=300)

label15=Label(alertpage,text="ALERTS",font=("poppins",50,"bold"),fg="black",bg="white")
label15.place(x=1000,y=180)


###############   mappage   ##############
map_window=Canvas(mappage,height=1080,width=1920,borderwidth=0,highlightthickness=0,relief="ridge")
map_window.place(x = 0, y = 0)

map_background=PhotoImage(file="news_background.png")
background=map_window.create_image(767,400,image=map_background)

b21=Button(mappage,text="Weather",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda: [mappage.place_forget(),weatherpage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b21.place(x=900,y=108,height=40,width=100)

b22=Button(mappage,text="Alerts",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda: [mappage.place_forget(),alertpage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b22.place(x=1050,y=108,height=40,width=100)

b23=Button(mappage,text="Map",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=btn_clicked)
b23.place(x=1200,y=108,height=40,width=100)

b24=Button(mappage,text="News",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda:[mappage.place_forget(),newspage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b24.place(x=1350,y=108,height=40,width=100)




background_img = Image.open("image.png")
resized = background_img.resize((1100,600), Image.Resampling.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)
background=map_window.create_image(755,455,image=new_pic)



######### News #################

news_page=Canvas(newspage,height=1080,width=1920,bg="white",bd=0,highlightthickness=0,relief="ridge")
news_page.place(x=0,y=0)

news_background=PhotoImage(file="news_background.png")
background = news_page.create_image(767,400,image=news_background)

b17=Button(newspage,text="Weather",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda: [newspage.place_forget(),weatherpage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b17.place(x=900,y=108,height=40,width=100)

b18=Button(newspage,text="Alerts",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda: [newspage.place_forget(),alertpage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b18.place(x=1050,y=108,height=40,width=100)

b19=Button(newspage,text="Map",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=lambda:[newspage.place_forget(),mappage.place(x=0,y=0,height=1080,width=1920)],relief="flat")
b19.place(x=1200,y=108,height=40,width=100)

b20=Button(newspage,text="News",font=("poppins",18,"bold"),borderwidth=0,fg="white",bg="#1f1e1d",highlightthickness=0,
    command=btn_clicked)
b20.place(x=1350,y=108,height=40,width=100)


button = tkinter.Button(news_page,font=24,text="reload",command=getNews)
button.place(x=750,y=700)

label = tkinter.Label(news_page,font=18,fg="black",justify="center",bg="white")
label.place(x=340,y=200)

getNews()

homepage.place(x=0,y=0,height=1080,width=1920)
root.mainloop()