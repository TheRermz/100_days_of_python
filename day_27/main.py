import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=500)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label["text"] = "new Text"

# ENTRY

input = tkinter.Entry()
# input.pack()


# button
def button_clicked():
    # new_label = tkinter.Label(text="OLAR")
    # new_label.pack()
    my_label["text"] = "I GOT CLICKED"
    my_label["text"] = input.get()


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()

# place
new_label = tkinter.Label(text="Olar")
# new_label.place(x=12, y=12)

# grid
new_label.grid(column=0, row=0)


window.mainloop()
