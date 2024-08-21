from PIL import Image, ImageTk
import tkinter as tk
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os

def main():

    folderpath = './Get Pokemon!'
    if os.path.isdir(folderpath):
        pass
    else:
        os.mkdir("Get Pokemon!")

    def download(num):
        try:
            web = requests.get(f'https://tw.portal-pokemon.com/play/pokedex/{num}')
            soup = BeautifulSoup(web.text, "html.parser")
            img = soup.select('meta[property="og:image"]')
            imgUrl = img[0]['content']
            imgFile = requests.get(imgUrl)
            f = open(f'./Get Pokemon!/{num}.png', 'wb')
            f.write(imgFile.content)
            f.close()
            print(num)
        except:
            print('error')
            pass

    num1 = int(E1.get())
    num2 = int(E2.get())
    numArr = [f'{j:04d}' for j in range(num1,num2+1)]

    executor = ThreadPoolExecutor()
    with ThreadPoolExecutor() as executor:
        executor.map(download, numArr)

# UI design
root = tk.Tk()
root.geometry("300x420+518+182")
root.title('Choose your Pokemon!')
root.configure(bg="lavenderblush")
root.iconbitmap('./pokemon.ico')

L0=tk.Label(root,text='Choose your Pokemon!',bg='lavenderblush',fg="mediumvioletred",
            font=("Viner Hand ITC",18,"bold"))

L0.pack(anchor='s',side='top',padx=10,pady=10)

image=Image.open("./760.jpg")
cover=ImageTk.PhotoImage(image)
text=tk.Label(root,image=cover)
text.pack(anchor='s',side='top',padx=10,pady=10)

L1=tk.Label(root,text='Start Number',bg='hotpink',fg="black",
            font=("Algerian",15,"bold"))
L2=tk.Label(root,text='End Number',bg='lightpink',fg="black",
            font=("Algerian",15,"bold"))
E1=tk.Entry(root)
E2=tk.Entry(root)

L1.pack(anchor='s',side='top',padx=10,pady=10)
E1.pack(anchor='s',side='top',padx=10,pady=10)
L2.pack(anchor='s',side='top',padx=10,pady=10)
E2.pack(anchor='s',side='top',padx=10,pady=10)

B1=tk.Button(root,text='Get Pokemon!',relief="ridge",
            activebackground='hotpink',
            activeforeground='#FFFFFF',
             state=tk.NORMAL,
             cursor='heart',
             command=main)
B1.pack(anchor='s',side='top',padx=10,pady=10)

root.mainloop()
