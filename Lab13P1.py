# Nicole Thomas
# April 22, 2022
# Tax Calculator

import tkinter as tk


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Tax Calculator')
        self.main_window.geometry('250x125')

        self.line1_frame = tk.Frame(self.main_window)
        self.line2_frame = tk.Frame(self.main_window)
        self.line3_frame = tk.Frame(self.main_window)
        self.line4_frame = tk.Frame(self.main_window)
        self.line5_frame = tk.Frame(self.main_window)

        self.prompt_label = tk.Label(self.line1_frame, text='Total Purchase: ')
        self.purchase_entry = tk.Entry(self.line1_frame, width=10)
        self.prompt_label.pack(side='left')
        self.purchase_entry.pack(side='left')

        self.tax_label = tk.Label(self.line2_frame, text='Tax Rate')
        self.tax_entry = tk.Entry(self.line2_frame, width=10)
        self.tax_label.pack(side='left')
        self.tax_entry.pack(side='left')

        self.tax_label = tk.Label(self.line3_frame, text='Sales Tax ')
        self.tax_value = tk.StringVar()
        self.tax_result_label = tk.Label(self.line3_frame, textvariable=self.tax_value)
        self.tax_value.set('$0.00')
        self.tax_label.pack(side='left')
        self.tax_result_label.pack(side='left')

        self.amount_due_label = tk.Label(self.line4_frame, text='Amount Due ')
        self.amount_value = tk.StringVar()
        self.amount_due_label = tk.Label(self.line4_frame, textvariable=self.amount_value)
        self.amount_value.set('$0.00')
        self.amount_due_label.pack(side='left')

        self.calc_tax_button = tk.Button(self.line5_frame,
                                         text='Calculate',
                                         command=self.calculate)
        self.quit_Button = tk.Button(self.line5_frame,
                                     text='Quit',
                                     command=self.main_window.destroy)
        self.calc_tax_button.pack(side='left')
        self.quit_Button.pack(side='left')

        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        self.line5_frame.pack()

        tk.mainloop()

    def calculate(arg1)
        print("I printed, Boss!")

my_gui = MyGUI()
