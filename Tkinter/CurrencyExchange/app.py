import requests
import tkinter as tk
from tkinter import OptionMenu, Label


class ApplicationGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.grid(padx=(10, 20), pady=(20, 10))
        self.app_font = ('helvetica', 16, 'bold')
        self.parent = parent
        self.parent.title('Currency Exchange')
        self.parent.columnconfigure(0, weight=1)

        self.source_currency = tk.StringVar()
        self.source_currency.set('Source Currency')
        self.target_currency = tk.StringVar()
        self.target_currency.set('Target Currency')
        self.source_text = tk.StringVar()
        self.source_text.set('From:')
        self.target_text = tk.StringVar()
        self.target_text.set('To:')
        self.amount = tk.StringVar()
        self.amount.set('0')
        self.var_result = tk.StringVar()
        self.var_result.set('0')

        self.choice_from = tk.StringVar()
        self.choice_to = tk.StringVar()

        choices = {'EUR', 'USD', 'INR', 'GBP'}
        self.choice_from.set('EUR')
        self.choice_to.set('USD')

        lbl_source = tk.Label(self, textvariable=self.source_text, fg='black', font=self.app_font)
        lbl_source.grid(row=0, column=0, sticky='N')
        popupMenuFrom = OptionMenu(self, self.choice_from, *choices)
        popupMenuFrom.grid(row=0, column=1, sticky='W')

        lbl_target = tk.Label(self, textvariable=self.target_text, fg='black', font=self.app_font)
        lbl_target.grid(row=0, column=2, sticky='N')
        popupMenuTo = OptionMenu(self, self.choice_to, *choices)
        popupMenuTo.grid(row=0, column=3, sticky='W')

        lbl_result = tk.Label(self, textvariable=self.var_result, fg='black', font=self.app_font)
        lbl_result.grid(row=1, column=3, sticky='E')

        self.input_entry = tk.Entry(self, textvariable=self.amount, font=self.app_font, width=7)
        self.input_entry.grid(row=1, column=1)

        button_compute = tk.Button(self, text='compute', command=self.compute,
                                   bg='grey', fg='black', font=self.app_font)
        button_compute.grid(row=8, column=1, sticky='W')
        button_close = tk.Button(self, text='close', command=self.close, bg='grey', fg='black', font=self.app_font)
        button_close.grid(row=8, column=3, sticky='E')

    def compute(self):
        from_ = self.choice_from.get()
        to_ = self.choice_to.get()
        response = requests.get(f'https://api.exchangeratesapi.io/latest?base={from_}&symbols={to_}')
        data = response.json()
        exchange_rate = data['rates'][to_]
        #date = data['date']
        amount = float(self.input_entry.get())
        result = amount * exchange_rate
        result = format(result, '.2f')
        self.var_result.set(result)

    def close(self):
        self.parent.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    ApplicationGUI(root)
    root.mainloop()