from tkinter import *


# program setup
window = Tk()
window.title("Miles to km converter")
window.config(bg="indigo", padx=50, pady=50)


def calculate():
    input_data = int(input.get())
    miles_to_km = input_data * 1.60934
    output_label["text"] = round(miles_to_km)


miles_label = Label(text="Miles", bg="indigo", fg="white", padx=20)
miles_label.grid(column=1, row=0)


is_equal_label = Label(text="is equal to", bg="indigo", fg="white", pady=20, font=('​Helvetica', 18, 'bold'))
is_equal_label.grid(column=0, row=1)


output_label = Label(text="", bg="indigo", fg="white", font=('​Helvetica', 14, 'bold'))
output_label.grid(column=1, row=1)


km_label = Label(text="Km", bg="indigo", fg="white", font=('​Helvetica', 14, 'bold'))
km_label.grid(column=2, row=1)



input = Entry(width=10, font=('​Helvetica', 14, 'bold'))
input.grid(column=0, row=0)


calculate_button = Button(text="Calculate", command=calculate, font=('​Helvetica', 14, 'bold'))
calculate_button.grid(column=0, row=3)


# run program
window.mainloop()