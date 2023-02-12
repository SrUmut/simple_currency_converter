import requests
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.title("Currency Converter")

# if you want transparent window, uncomment the line below
root.attributes('-alpha',0.9)

currencies = ['CNY', 'EUR', 'GBP', 'INR', 'JPY', 'RUB', 'TRY', 'USD']
result_label = None


def convert():
    if amount.get().isnumeric():
        global result_label
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to.get()}&from={base.get()}&amount={amount.get()}"

        payload = {}
        headers = {"apikey": "TBlYlSeBbnU9yK428YL6lZj1PdU0R2xn"}

        response = requests.request("GET", url, headers=headers, data = payload)
        result = response.json()["result"]
        # in first convert
        if not result_label:
            result_label = Label(main_frame, text=f"{amount.get()} {base.get()} = {result} {to.get()}")
            result_label.pack()
        # when it's not first convert
        else:
            result_label.destroy()
            result_label = Label(main_frame, text=f"{amount.get()} {base.get()} = {result} {to.get()}")
            result_label.pack()
    else:
        messagebox.showwarning("Amount must be a number!", "Amount must be a number!")


main_frame = LabelFrame(root, borderwidth=0)
main_frame.pack(expand=Y)

# first row
first_row = LabelFrame(main_frame, borderwidth=0)
first_row.pack()

Label(first_row, text="From").grid(row=0, column=0)

base = StringVar()
base.set(currencies[-1])
OptionMenu(first_row, base, *currencies).grid(row=0, column=1)

Label(first_row, text="to").grid(row=0, column=2)

to = StringVar()
to.set(currencies[-2])
OptionMenu(first_row, to, *currencies).grid(row=0, column=3)

# second row
second_row = LabelFrame(main_frame, borderwidth=0)
second_row.pack()

Label(second_row, text="Amount:").grid(row=0, column=0)
amount = Entry(second_row, width=15)
amount.grid(row=0, column=1)

# third_row
Button(main_frame, text="Convert", command=convert).pack()

root.mainloop()
