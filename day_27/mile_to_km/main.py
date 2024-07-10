import tkinter


def miles_to_km():
    miles = float(entry_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

entry_input = tkinter.Entry(width=5)
entry_input.grid(column=1, row=0)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = tkinter.Label(text="Is equals to")
is_equal_label.grid(column=0, row=1)


km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1)


km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)


calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
