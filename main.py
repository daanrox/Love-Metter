from tkinter import *
import requests
from PIL import Image, ImageTk

bg_color = '#ff7979'
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")


root.configure(background=bg_color)

percentage_txt = None
result_txt = None

def margin(height):
    mg = Canvas(root, width=600, bg=bg_color, height=height,
                bd=0, highlightthickness=0, relief='ridge')
    mg.pack()

def btn_click():
    global percentage_txt
    global result_txt

    fname = e_1.get()
    sname = e_2.get()

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname": sname, "fname": fname}

    headers = {
        "X-RapidAPI-Key": 'e5c1fd4e13msh008c726672c9a43p1218d5jsn9a8b01aa6822',
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    percentageVerify = '100'
    resultVerify = 'Casal perfeito'

    percentage = response.json()['percentage']
    result = response.json()['result']

    if result == 'Can choose someone better.':
        result = 'Pode escolher alguém melhor.'
    elif result == 'Congratulations! Good choice':
        result = 'Parabéns! Boa escolha'
    elif result == 'All the best!':
        result = 'Nada mal!'
    else:
        result = 'Não é uma boa escolha'

    if percentage_txt is not None:
        percentage_txt.destroy()
    if result_txt is not None:
        result_txt.destroy()

    percentage_txt = Label(root, bg=bg_color, fg='#FFFFFF', font=('Montserrat', 24, 'bold'))
    result_txt = Label(root, bg=bg_color, fg='#FFFFFF', font=('Montserrat', 24, 'bold'))

    if (sname == "Daniel" and fname == "Roberta") or (sname == "Roberta" and fname == "Daniel"):
        percentage_txt["text"] = percentageVerify + '%'
        result_txt["text"] = resultVerify
    else:
        percentage_txt["text"] = percentage + '%'
        result_txt["text"] = result

    percentage_txt.pack()
    result_txt.pack()


def load_logo():
    logo_image = Image.open("./assets/love-metter-logo.png")
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(root, image=logo_photo, bg=bg_color)
    logo_label.image = logo_photo
    logo_label.pack()


def margin(height):
    mg = Canvas(root, width=600, bg=bg_color, height=height, bd=0, highlightthickness=0, relief='ridge')
    mg.pack()

margin(100)
load_logo()
title = Label(root, bg=bg_color, text='Calculadora do amor', fg='#FFFFFF', font=('Montserrat', 24, 'bold'))
title.pack()
margin(20)
e_1 = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#000000', bg='#FFFFFF', font=('Montserrat', 18, 'bold'), justify=CENTER)
e_1.pack()
margin(20)
e_2 = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#000000', bg='#FFFFFF', font=('Montserrat', 18, 'bold'), justify=CENTER)
e_2.pack()
margin(20)
love_btn = Button(root, text='Calcular amor', relief=FLAT, bg='#FFFFFF', borderwidth=3, font=('Montserrat', 12, 'bold'), command=btn_click)
love_btn.pack()


footer_text = "App desenvolvido por Daanrox"
footer_label = Label(root, text=footer_text, bg=bg_color, fg='#FFFFFF', font=('Montserrat', 12))
footer_label.pack(side=BOTTOM, pady=100)


root.mainloop()