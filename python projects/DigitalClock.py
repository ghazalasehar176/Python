import tkinter as tk
from time import strftime

# Main window
root = tk.Tk()
root.title("Digital Clock")

# Function to get & update time
def time():
    string = strftime('%H:%M:%S  %p \n %D')
    label.config(text=string)
    label.after(1000 , time)  

# Label design
label = tk.Label(root , font=('calibri' , 50 , 'bold') , background='black' , foreground='lime')
label.pack(anchor = 'center')

# Run time function
time()

# Keep window running
root.mainloop()

