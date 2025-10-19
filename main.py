import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Medical Imaging Edge Detection")
root.geometry("800x600")

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root, image=photo)
        label.image = photo
        label.pack()
        
ttk.Button(root, text = "Upload Image", command = upload_image).pack()
root.mainloop()