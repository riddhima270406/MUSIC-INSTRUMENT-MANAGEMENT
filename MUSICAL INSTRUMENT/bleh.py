import tkinter as tk
from PIL import ImageTk, Image
import io
import requests

def display_image_from_url(image_url):
    response = requests.get(image_url)
    img_data = response.content
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((300, 300))  # Adjust the size as needed
    img_tk = ImageTk.PhotoImage(img)
    image_label.configure(image=img_tk)
    image_label.image = img_tk

# Create the main window
window = tk.Tk()
window.geometry("400x400")

# Set the background color
window.configure(bg="#D6C7B7")

# Example URL of an image
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTprz-O7pxUNX2tvh-kbUh6tvbHIyD026vWTEj2w7v4-a8epS6rEfwQLgaZMgbuHLe3awo&usqp=CAU"

# Create a button to display the image
button = tk.Button(window, text="Display Image", command=lambda: display_image_from_url(image_url))
button.pack()

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Start the main event loop
window.mainloop()
