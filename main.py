import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

root = tk.Tk()
root.title("Medical Imaging Edge Detection")
root.geometry("1200x600")

original_image = None
processed_image = None
current_image_path = None

def update_display():
    global original_image, processed_image
    frame_width = imageframe.winfo_width() // 2
    frame_height = imageframe.winfo_height()

    if original_image:
        img1 = scale_to_fit(original_image, (frame_width, frame_height))
        photo1 = ImageTk.PhotoImage(img1)
        label_original.configure(image=photo1, text = "Original Image", compound = 'bottom')
        label_original.image = photo1

    if processed_image:
        img2 = scale_to_fit(processed_image, (frame_width, frame_height))
        photo2 = ImageTk.PhotoImage(img2)
        label_processed.configure(image=photo2, text = "Processed Image", compound = 'bottom')
        label_processed.image = photo2

def update_image_processing(*args):
    global original_image, processed_image, current_image_path
    if current_image_path:
        image_cv = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

        blur = cv2.GaussianBlur(image_cv, (5, 5), 0)
        edges = cv2.Canny(blur, slider1.get(), slider2.get())
        image2 = Image.fromarray(edges)
        processed_image = image2.copy()
        update_display()

def window_resize(event):
    if current_image_path:
        update_display()

def scale_to_fit(image, max_size):
    if image.width > max_size[0] or image.height > max_size[1]:
        ratio = min((max_size[0] - 30) / image.width, (max_size[1] - 30) / image.height)
        new_size = (int(image.width * ratio), int(image.height * ratio))
    else:
        new_size = (image.width, image.height)
    return image.resize(new_size, Image.LANCZOS)
    
def upload_image():
    global original_image, processed_image, current_image_path
    file_path = filedialog.askopenfilename()
    if file_path:
        current_image_path = file_path

        image = Image.open(file_path)
        original_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label_original.configure(image=photo, text = "Original Image", compound = 'bottom')
        label_original.image = photo

        image_cv = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        blur = cv2.GaussianBlur(image_cv, (5, 5), 0)
        edges = cv2.Canny(blur, slider1.get(), slider2.get())
        image2 = Image.fromarray(edges)
        photo2 = ImageTk.PhotoImage(image2)
        processed_image = image2.copy()
        label_processed.configure(image=photo2, text = "Processed Image", compound = 'bottom')
        label_processed.image = photo2

        update_display()

imageframe = ttk.Frame(root)
imageframe.pack(expand=True, fill='both')

imageframe.columnconfigure(0, weight=1)
imageframe.columnconfigure(1, weight=1)

label_original = ttk.Label(imageframe, text="Original Image")
label_processed = ttk.Label(imageframe, text="Processed Image")
label_original.grid(row=0, column=0, padx=10, pady=10)
label_processed.grid(row=0, column=1, padx=10, pady=10)

sliderlabel1 = ttk.Label(root, text="Canny Threshold 1")
sliderlabel1.pack(padx=10, pady=5)
slider1 = ttk.Scale(root, from_=0, to=300, orient='horizontal', length=300, command=update_image_processing)
slider1.set(30)
slider1.pack(padx=10, pady=20)
slider2 = ttk.Scale(root, from_=0, to=300, orient='horizontal', length=300, command=update_image_processing)
slider2.set(150)
sliderlabel2 = ttk.Label(root, text="Canny Threshold 2")
sliderlabel2.pack(padx=10, pady=5)
slider2.pack(padx=10, pady=5)

ttk.Button(root, text = "Upload Image", command = upload_image).pack()

root.bind('<Configure>', window_resize)

root.mainloop()