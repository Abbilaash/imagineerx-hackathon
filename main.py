# Importing all needed modules
import customtkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector 
import os
import test as func
import pickle
import pandas as pd
import mplfinance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

window = customtkinter.CTk()
window.geometry('1550x1000')
window.state('zoomed')
window.resizable(0, 0)
window.title(" Fin Bot")
window.configure(fg_color="white")

global USER_DET
USER_DET = {}

# Starting the main App
def App():
    global app
    app = customtkinter.CTkFrame(master=window,fg_color="white")
    app.place(x=0,y=0,relheight=1,relwidth=1)

    def dashboard_func():
        global file_path
        file_path = os.path.dirname(os.path.realpath(__file__))
        
        dashFrame = customtkinter.CTkFrame(master=window,fg_color="white")
        dashFrame.place(x=0,y=0,relheight=1,relwidth=1)

        side_options_frame = Frame(dashFrame, bg="white",width=200,height=65)
        side_options_frame.place(x=0,y=0)
        side_options_frame.pack_propagate(False)
        top_line = Canvas(side_options_frame, height=1, bg="MediumPurple2", highlightthickness=0)
        top_line.place(x=0,y=59,relwidth=1)
        top_navbar = Frame(dashFrame, bg="white",height=60)
        top_navbar.place(x=200,y=0,relwidth=1)
        top_line1 = Canvas(top_navbar, height=1, bg="MediumPurple1", highlightthickness=0)
        top_line1.place(x=0,y=59,relwidth=1)

        UserLogo_logo = customtkinter.CTkImage(Image.open(file_path + "/src/assets/user-icon.png"),size=(30,30))
        UserLogo_set_lbl1 = customtkinter.CTkLabel(master=top_navbar,image=UserLogo_logo,text="")
        UserLogo_set_lbl1.place(x=1060,y=5)
        LoggedUserName_lbl = customtkinter.CTkLabel(master=top_navbar,text=USER_DET['NAME'],
                                                    font=("yu gothic ui", 19,"bold"),text_color="black")
        LoggedUserName_lbl.place(x=1100,y=5)

    
        SideOptions_frame = customtkinter.CTkFrame(master=dashFrame,width=200,border_width=1,
                                                   border_color="white",
                                                   fg_color="white")
        SideOptions_frame.place(x=5,y=50,relheight=0.9)

        top_line = Canvas(dashFrame, width=0, bg="MediumPurple1", highlightthickness=0)
        top_line.place(x=250,y=60,relheight=1)

        dashboard_btn_img = customtkinter.CTkImage(Image.open(file_path + "/src/assets/dashboard_icon.png"),size=(20,20))
        dashboard_btn = customtkinter.CTkButton(master=SideOptions_frame,command=home_func,anchor="sw",hover_color="MediumPurple2",image=dashboard_btn_img,fg_color="white",compound="left",height=40,text_color="black",font=("yu gothic ui", 19,"bold"),text="  Home",corner_radius=8)
        dashboard_btn.place(x=5,y=60,relwidth=0.95)

        youraccount_btn_img = customtkinter.CTkImage(Image.open(file_path + "/src/assets/user-icon.png"),size=(22,22))
        youraccount_btn = customtkinter.CTkButton(master=SideOptions_frame,command=my_account_func,anchor="sw",hover_color="MediumPurple2",image=youraccount_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  My Account",corner_radius=8)
        youraccount_btn.place(x=5,y=120,relwidth=0.95)

        # Create a function to view my account stat
        def my_account_func():
            pass

        # Designing the home screen
        def home_func():
            home_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            home_frame.place(x=210,y=50,relheight=1,relwidth=1)

            
            data = pd.read_csv('src/bitcoin data.csv', parse_dates=True, index_col=0)
            class CandlestickFrame(tk.Frame):
                def __init__(self, master=None, **kwargs):
                    super().__init__(master, **kwargs)
                    self.master = master
                    self.create_widgets()

                def create_widgets(self):
                    self.fig, self.ax = mpf.plot(data, type='candle', returnfig=True)
                    self.canvas = FigureCanvasTkAgg(self.fig, master=self)
                    self.canvas_widget = self.canvas.get_tk_widget()
                    self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                    toolbar = NavigationToolbar2Tk(self.canvas, self)
                    toolbar.update()
                    self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            candlestick_frame = CandlestickFrame(home_frame)
            candlestick_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        home_func()

    # Creating the register account function
    def register_func():
        '''data = {
            'USERNAME':'abbi',
            'NAME':'abbi',
            'PASSWORD':'abbi',
            'AADHAAR':'123456789011',
            'PHONE':'8667093591',
            'GMAIL':"abbilaashat@gmail.com"
        }
        with open("src/auth.bin", "wb") as file:
            pickle.dump(data, file)'''
        pass

    def LogIn_func():
        login_frame = customtkinter.CTkFrame(master=window,fg_color="white")
        login_frame.place(x=0,y=0,relheight=1,relwidth=1)
        img1=ImageTk.PhotoImage(Image.open("A:\\PROJECTS\\Coimbatore-smart-city-app\\Smart-city-app\\assets\\pattern.png"))
        l1=customtkinter.CTkLabel(master=login_frame,image=img1)
        l1.pack()
        frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15,bg_color='black')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        l2=customtkinter.CTkLabel(master=frame, text="Log into your Kovai smart \ncitizen app",font=('Century Gothic',20))
        l2.place(x=40, y=30)
        entry1=customtkinter.CTkEntry(master=frame, width=220,height=40, placeholder_text='Username')
        entry1.place(x=50, y=110)
        entry2=customtkinter.CTkEntry(master=frame, width=220,height=40, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)

        def login_btn():
            username = entry1.get()
            password = entry2.get()
            try:
                data = func.retreive_user_data(username,password)
                file = open('src/auth.bin','wb')
                dat = {
                    'USERNAME':data[0],
                    'NAME':data[1],
                    'PASSWORD':data[2],
                    'AADHAAR':data[3],
                    'PHONENUMBER':data[4],
                    'GMAIL':data[5]
                }
                with open("src/auth.bin", "wb") as file:
                    pickle.dump(dat, file)
                USER_DET["USERNAME"] = data[0]
                USER_DET["NAME"] = data[1]
                USER_DET['AADHAAR'] = data[3]
                USER_DET['PHONENUMBER'] = data[4]
                USER_DET['GMAIL'] = data[5]
                login_frame.destroy()
                dashboard_func()
            except:
                data = ()
                l5=customtkinter.CTkLabel(master=frame, text="No credentials found!",font=('Century Gothic',14))
                l5.place(x=85, y=320)
            if len(data)>0:
                print(data)
        button1 = customtkinter.CTkButton(master=frame, width=220,height=50, text="LOGIN", command=login_btn, corner_radius=6)
        button1.place(x=50, y=260)
    
    # here the data will be stored at 'auth.bin' and the uder details will be fed at UDER_DET
    def LogIn():
        if os.path.exists('src/auth.bin'):
            if os.path.getsize("src/auth.bin") > 0:
                auth_file = open('src/auth.bin','rb')
                data = pickle.load(auth_file)
                USER_DET["USERNAME"] = data['USERNAME']
                USER_DET["NAME"] = data['NAME']
                USER_DET['AADHAAR'] = data['AADHAAR']
                USER_DET['PHONENUMBER'] = data['PHONE']
                USER_DET['GMAIL'] = data['GMAIL']
                dashboard_func()
            else:
                LogIn_func()
        else:
            register_func()
    
    LogIn()

App()

window.mainloop()