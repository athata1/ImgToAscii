from PIL import Image, ImageOps
import math
import os;
import tkinter as tk
from tkinter import filedialog


#convert from img to ascii
def img_to_ascii():
   if (filename == "" or (".jpg" not in filename and ".png" not in filename and ".jfif" not in filename)):
      return
   writer = open("Ascii.txt", "w");

   im = ImageOps.grayscale(Image.open(filename))
   col,row = im.size

   ratio = 1;
   row = row/2
   print("col:",col,"row",row);

   #increment ratio until bound is hit from lower or upper
   while(ratio*col <= 1024 and ratio*row <= 500):
      ratio = ratio + .01
      if(ratio*col > 1024 or ratio*row > 500):
         ratio = ratio - 0.01
         break;
         
   #increment ratio until bound is hit from upprr to lower
   while(ratio*col >= 1024 or ratio*row >= 500):
      ratio = ratio - .01
      if(ratio*col < 1024 and ratio*row < 500):
         break;
   col = int(col*ratio);
   row = int(row*ratio);

   print("col:",col,"row",row);
   im = im.rotate(0).resize((col,row))
   col,row = im.size;

   #chars = [" ", ".",":",">","#","&","%","@"]; #Use for black background
   #chars = ["@","%","&","#",">",":","."," "]; #Use for white background
   chars = ["@","%","G","B","&","#","\\","?",">","m","o","|",";",":","^","_","*","^","'","-",",","."," "] #more specific
    
   for y in range(row):
       for x in range(col):
         writer.write(chars[int(im.getpixel((x,y))/255*(len(chars)-1))])
       writer.write('\n');
   os.startfile("Ascii.txt")

def UploadAction(event=None):
    global filename;
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    
#make GUI
filename = ""
root = tk.Tk()
root.geometry('300x150')
root.title("IMGtoASCII");
button1 = tk.Button(root, text='Select Image File',width = 15, command=UploadAction)
button2 = tk.Button(root, text=' Create Text File ',width = 15, command=img_to_ascii)
button1.pack()
button2.pack()
button1.place(x=90,y=45)
button2.place(x=90,y=70)
root.mainloop()

