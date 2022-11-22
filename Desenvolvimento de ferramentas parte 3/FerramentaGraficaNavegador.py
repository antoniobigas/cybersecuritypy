import webbrowser
from tkinter import *


###################
def Browser():
    root = Tk()

    root.title('Abrir Browser')
    root.geometry('300x300')
    Label1 = Label(root, text="Click para abrir a página",
                   font=("Helvetica", 14, "bold"), fg="blue").pack()

    def google():
        webbrowser.open('www.google.com')

    def wikipedia():
        webbrowser.open('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia')

    def flickr():
        webbrowser.open('www.flickr.com/photos/')

    def tkinter():
        webbrowser.open('https://docs.python.org/3/library/tkinter.html')

    def new():
        webbrowser.open('')

    def home():
        webbrowser.open('file:///home/')

    dict_command = {'Google': google, 'Wikipedia': wikipedia, 'Flickr': flickr, 'Tkinter': tkinter}
    list_name = list(dict_command.keys())
    list_color = ['yellow', 'green', 'red', '#D3D3D3']

    for i in range(len(list_name)):
        Button(root, text=list_name[i], command=dict_command[list_name[i]],
               bg=list_color[i], fg='black').pack(pady=12)

    Button(root, text='Nova Janela', command=new,
           bg='black', fg='white').pack(side=RIGHT, padx=5, pady=10)

    Button(root, text='home', command=home,
           bg='black', fg='white').pack(side=LEFT, padx=5, pady=0)

    root.mainloop()


###################
Browser()
###################
# sudo apt-get install python3-tk
###################