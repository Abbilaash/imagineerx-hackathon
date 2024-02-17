# Importing all needed modules
import customtkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import pickle
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import matplotlib.pyplot as plt
import yfinance as yf
import func

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

        # Create a function to view my account stat
        def my_account_func():
            myaccount_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            myaccount_frame.place(x=210,y=50,relheight=1,relwidth=1)

            account_Details = customtkinter.CTkFrame(master=myaccount_frame,width=1200,fg_color="gray95",height=300)
            account_Details.place(x=20,y=30)

            customtkinter.CTkLabel(master=account_Details,text="Account Details",font=("yu gothic ui", 25,"bold"),fg_color="gray95",bg_color="gray95",text_color="gray20").place(x=20,y=20)
            customtkinter.CTkLabel(master=account_Details,font=("yu gothic ui", 18,"bold"),text_color="gray25",text="Account Holder Name: "+USER_DET['NAME']).place(x=20,y=100)
            customtkinter.CTkLabel(master=account_Details,font=("yu gothic ui", 18,"bold"),text_color="gray25",text="Demat Account Number: "+USER_DET['ACCNO']).place(x=20,y=130)
            customtkinter.CTkLabel(master=account_Details,font=("yu gothic ui", 18,"bold"),text_color="gray25",text="Aadhaar Number: "+USER_DET['AADHAAR']).place(x=20,y=160)
            customtkinter.CTkLabel(master=account_Details,font=("yu gothic ui", 18,"bold"),text_color="gray25",text="Gmail ID: "+USER_DET['GMAIL']).place(x=20,y=190)

            transactionHistory_frame = customtkinter.CTkScrollableFrame(master=myaccount_frame,width=900,height=400,fg_color="gray95")
            transactionHistory_frame.place(x=20,y=370)
            StockHistory = func.Get_stock_history()[::-1]
            for dat in StockHistory:
                intFrame = customtkinter.CTkFrame(master=transactionHistory_frame,width=880,height=100,border_width=10,fg_color="gray70",border_color="gray95",corner_radius=25,bg_color="gray95")
                intFrame.pack()
                customtkinter.CTkLabel(master=intFrame,text="ID: "+dat[0],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=20,y=30)
                customtkinter.CTkLabel(master=intFrame,text=dat[1],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=80,y=30)
                customtkinter.CTkLabel(master=intFrame,text="Pruchased: "+dat[2],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=200,y=30)
                customtkinter.CTkLabel(master=intFrame,text="Quantity: "+dat[6],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=420,y=30)
                customtkinter.CTkLabel(master=intFrame,text="Type: "+dat[-1],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=530,y=30)
                if dat[3] != '':
                    customtkinter.CTkLabel(master=intFrame,text="Sold: "+dat[3],text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=680,y=30)
                else:
                    customtkinter.CTkLabel(master=intFrame,text="Sold: -",text_color="gray20",font=("yu gothic ui", 18,"bold")).place(x=680,y=30)


        # Designing the home screen
        def home_func():
            home_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            home_frame.place(x=210,y=50,relheight=1,relwidth=1)

            graph_frame = customtkinter.CTkFrame(master=home_frame,fg_color="gray",width=800,height=600)
            graph_frame.place(x=10,y=10)

            df=yf.download(tickers= 'BTC-USD',start='2023-10-01', end='2024-02-11')
            def graph_plot():            
                fig, ax = plt.subplots(figsize=(16, 5))
                open = df['Open']
                close = df['Close']
                high = df['High']
                plot1 = fig.add_subplot()
                plot1.plot(open,color="green")
                plot1.plot(close,color="red")
                plot1.plot(high,color="purple",linestyle='dashed')
                plot1.legend(['Open price','Close price','Highest price'],loc="lower right")
                ax.set_xlabel('Date')
                ax.set_ylabel('Price ($)')
                ax.set_title('Bitcoin price vs Date',fontsize=17)
                canvas = FigureCanvasTkAgg(fig,master = graph_frame)   
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side=tk.TOP, fill=tk.BOTH) 
                toolbar = NavigationToolbar2Tk(canvas, graph_frame) 
                toolbar.update() 
                canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                graph_frame.grid_rowconfigure(0, weight=1)
                graph_frame.grid_columnconfigure(0, weight=1)
            graph_plot()
<<<<<<< HEAD

=======
            
>>>>>>> 8dd535be85da91a1a1a7fb8c775c2accda103990

            # creating a frame for suggesting the user for more trades
            suggest_frame = customtkinter.CTkFrame(master=home_frame,width=600,height=300,fg_color="gray90")
            suggest_frame.place(x=10,y=500)
            customtkinter.CTkLabel(master=suggest_frame,text="FinBot's Suggestion",font=("yu gothic ui", 25,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray20").place(x=20,y=20)
            dataDisplayFrame = customtkinter.CTkFrame(master=suggest_frame,width=600,height=200,fg_color="gray90")
            dataDisplayFrame.place(x=0,y=100)

            BotSuggestions = func.SuggestBest()
<<<<<<< HEAD
=======

            sell1 = "DATE:"+str(func.convert_Date(BotSuggestions[0][0][0]))+"    "+"ACTION: BUY"+"      "+"PRED PRICE:"+str(BotSuggestions[0][0][1])
            sell2 = "DATE:"+str(func.convert_Date(BotSuggestions[0][1][1]))+"    "+"ACTION: BUY"+"      "+"PRED PRICE:"+str(BotSuggestions[0][1][1])
            buy1 = "DATE:"+str(func.convert_Date(BotSuggestions[1][0][0]))+"    "+"ACTION: SELL"+"      "+"PRED PRICE:"+str(BotSuggestions[1][0][1])
            buy2 = "DATE:"+str(func.convert_Date(BotSuggestions[1][1][1]))+"    "+"ACTION: SELL"+"      "+"PRED PRICE:"+str(BotSuggestions[1][1][1])

            customtkinter.CTkLabel(master=suggest_frame,text="According to the previous prices I can suggest to",font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=60)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=sell1,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=10)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=sell2,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=40)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=buy1,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=70)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=buy2,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=100)
            
>>>>>>> 8dd535be85da91a1a1a7fb8c775c2accda103990

            sell1 = "DATE:"+str(func.convert_Date(BotSuggestions[0][0][0]))+"    "+"ACTION: BUY"+"      "+"PRED PRICE:"+str(BotSuggestions[0][0][1])
            sell2 = "DATE:"+str(func.convert_Date(BotSuggestions[0][1][1]))+"    "+"ACTION: BUY"+"      "+"PRED PRICE:"+str(BotSuggestions[0][1][1])
            buy1 = "DATE:"+str(func.convert_Date(BotSuggestions[1][0][0]))+"    "+"ACTION: SELL"+"      "+"PRED PRICE:"+str(BotSuggestions[1][0][1])
            buy2 = "DATE:"+str(func.convert_Date(BotSuggestions[1][1][1]))+"    "+"ACTION: SELL"+"      "+"PRED PRICE:"+str(BotSuggestions[1][1][1])

            customtkinter.CTkLabel(master=suggest_frame,text="According to the previous prices I can suggest to",font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=60)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=sell1,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=10)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=sell2,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=40)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=buy1,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=70)
            customtkinter.CTkLabel(master=dataDisplayFrame,text=buy2,font=("yu gothic ui", 17,"bold"),fg_color="gray90",bg_color="gray90",text_color="gray25").place(x=20,y=100)
            

        home_func()

        dashboard_btn_img = customtkinter.CTkImage(Image.open(file_path + "/src/assets/dashboard_icon.png"),size=(20,20))
        dashboard_btn = customtkinter.CTkButton(master=SideOptions_frame,command=home_func,anchor="sw",hover_color="MediumPurple2",image=dashboard_btn_img,fg_color="white",compound="left",height=40,text_color="black",font=("yu gothic ui", 19,"bold"),text="  Home",corner_radius=8)
        dashboard_btn.place(x=5,y=60,relwidth=0.95)

        youraccount_btn_img = customtkinter.CTkImage(Image.open(file_path + "/src/assets/user-icon.png"),size=(22,22))
        youraccount_btn = customtkinter.CTkButton(master=SideOptions_frame,command=my_account_func,anchor="sw",hover_color="MediumPurple2",image=youraccount_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  My Account",corner_radius=8)
        youraccount_btn.place(x=5,y=120,relwidth=0.95)

    # Creating the register account function
    def register_func():
        pass

    def LogIn_func():
        pass
    
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
                USER_DET['ACCNO'] = data['ACCNO']
                dashboard_func()
            else:
                LogIn_func()
        else:
            register_func()
    
    LogIn()

App()

window.mainloop()