import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
from glob import glob
import os
import threading

#---------------define constants--------------------#
PRIMARY_COLOR = "#1C3879"
SECONDARY_COLOR = "#002B5B"
LABEL_TEXT_COLOR = "#DDD"
FONT = "Helvetica"


window = tk.Tk()
window.title("Better Image")
window.minsize(width=550,height=350)
window.config(bg=PRIMARY_COLOR,padx=25,pady=25)
window.resizable(0,0)

frame= tk.Frame(width=500,height=100,bg=SECONDARY_COLOR)
frame.place(relx=0.5,rely=0.5,anchor='center')

main_lbl = tk.Label(text="IMAGE OPTIMIZATION TOOL",font=(FONT,18),bg=PRIMARY_COLOR,fg=LABEL_TEXT_COLOR)
main_lbl.place(relx=0.5,rely=0.10,anchor='center')

by_lbl = tk.Label(text="- Sudheer Tammini", font=(FONT,8),bg=PRIMARY_COLOR,fg=LABEL_TEXT_COLOR)
by_lbl.place(relx=0.80,rely=0.97,anchor='nw')


msg = tk.Label(text="",bg=PRIMARY_COLOR,fg='#fff',font=(FONT,10))
msg.place(relx=0.5,rely=0.9,anchor='center')

def single_img_optimizer():
    file_name = fd.askopenfilename(initialdir="/",title='Please select your Image')
    img = Image.open(file_name)
    if img.size > (900,500): 
        img = img.resize((900,500))
    img.save(file_name,optimize=True,quality=90)
    msg.config(text= "Image optimized sucessfully..!!")


def multiple_img_optimizer():
    folder_path = fd.askdirectory(initialdir="/",title='Please select a directory')
    os.chdir(folder_path)
    file_names = glob("**/*.jpg",recursive=True) + glob("**/*.jpeg",recursive=True) + glob("**/*.png",recursive=True)
    for img_name in file_names:
        msg.config(text=f"Processing >> {img_name}")
        img = Image.open(img_name)
        if img.size > (900,500): 
            img = img.resize((900,500))
        img.save(img_name,optimize=True,quality=90)
    msg.config(text=f"Total {len(file_names)} images optimized successfully..!!")
        

def multiple():
    threading.Thread(target=multiple_img_optimizer).start()


def webp_format():
    file_name = fd.askopenfilename(initialdir="/",title='Please select your Image')
    img_name = file_name.split(".")[0]
    img = Image.open(file_name)
    img.save(img_name+".webp",'webp',optimize=True,quality=90)
    msg.config(text="Image conversion sucessfull..!!")


btn_single = tk.Button(frame,text="Single",bg=SECONDARY_COLOR,command=single_img_optimizer,width=6, fg=LABEL_TEXT_COLOR)
btn_single.place(relx=0.20,rely=0.45, anchor='center')
btn_single.configure(font=(FONT,12),padx=20,pady=6)

btn_multiple = tk.Button(frame,text="Multiple",bg=SECONDARY_COLOR,command= multiple,width=6, fg=LABEL_TEXT_COLOR)
btn_multiple.place(relx=0.45,rely=0.45, anchor='center')
btn_multiple.configure(font=(FONT,12),padx=20,pady=6)

btn_webp = tk.Button(frame,text="WebP Converter",bg=SECONDARY_COLOR,command=webp_format,width=10,fg=LABEL_TEXT_COLOR)
btn_webp.place(relx=0.75,rely=0.45, anchor='center')
btn_webp.configure(font=(FONT,12),padx=20,pady=6)


if __name__ == "__main__":
    window.mainloop()