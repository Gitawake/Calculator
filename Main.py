#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)

        self.master = master
        self.pack()

        self.out_log = tk.Frame(self)
        self.out_log.pack()

        self.control = tk.Frame(self)
        self.control.pack()

        self.log = tk.Text(self.out_log, width=25, height=5)
        self.log.pack()

        self.ac = tk.Button(self.control, text="AC", width=5, command=self.all_delete)
        self.ac.grid(row=1, column=1)

        self.button_close = tk.Button(self.control, text="", width=5)
        self.button_close.grid(row=1, column=2)

        self.button_percentage = tk.Button(self.control, text="", width=5)
        self.button_percentage.grid(row=1, column=3)

        self.button_except = tk.Button(self.control, text="/", width=5, command=self.algorithm_except)
        self.button_except.grid(row=1, column=4)

        self.button_seven = tk.Button(self.control, text="7", width=5, command=self.button7)
        self.button_seven.grid(row=2, column=1)

        self.button_eight = tk.Button(self.control, text="8", width=5, command=self.button8)
        self.button_eight.grid(row=2, column=2)

        self.button_nine = tk.Button(self.control, text="9", width=5, command=self.button9)
        self.button_nine.grid(row=2, column=3)

        self.button_ride = tk.Button(self.control, text="*", width=5, command=self.algorithm_ride)
        self.button_ride.grid(row=2, column=4)

        self.button_four = tk.Button(self.control, text="4", width=5, command=self.button4)
        self.button_four.grid(row=3, column=1)

        self.button_five = tk.Button(self.control, text="5", width=5, command=self.button5)
        self.button_five.grid(row=3, column=2)

        self.button_six = tk.Button(self.control, text="6", width=5, command=self.button6)
        self.button_six.grid(row=3, column=3)

        self.button_reduce = tk.Button(self.control, text="-", width=5, command=self.algorithm_reduce)
        self.button_reduce.grid(row=3, column=4)

        self.button_one = tk.Button(self.control, text="1", width=5, command=self.button1)
        self.button_one.grid(row=4, column=1)

        self.button_two = tk.Button(self.control, text="2", width=5, command=self.button2)
        self.button_two.grid(row=4, column=2)

        self.button_three = tk.Button(self.control, text="3", width=5, command=self.button3)
        self.button_three.grid(row=4, column=3)

        self.button_plus = tk.Button(self.control, text="+", width=5, command=self.algorithm_plus)
        self.button_plus.grid(row=4, column=4)

        self.button_zero = tk.Button(self.control, text="0", width=5, command=self.button0)
        self.button_zero.grid(row=5, column=1)

        self.button_close = tk.Button(self.control, text="", width=5)
        self.button_close.grid(row=5, column=2)

        self.button_spot = tk.Button(self.control, text=".", width=5, command=self.button_d)
        self.button_spot.grid(row=5, column=3)

        self.button_to = tk.Button(self.control, text="=", width=5, command=self.settlement)
        self.button_to.grid(row=5, column=4)

        self.inx = None

        self.iny = None

        self.calculated_value = ''

        self.clear_input = False

    def inset_delete(self):
        self.log.configure(state='normal')
        self.log.delete('0.0', 'end')
        self.log.see('end')
        self.log.update()
        self.log.configure(state='disabled')

    def all_delete(self):
        self.inset_delete()
        self.inx = None
        self.iny = None
        self.calculated_value = ''

    def inset_ipt(self, index, chars):
        self.log.configure(state='normal')
        self.log.insert(index, chars)
        self.log.see('end')
        self.log.update()
        self.log.configure(state='disabled')

    def inset_add(self, index, chars):
        if self.clear_input:
            self.inset_delete()
            self.clear_input = False
        self.inset_ipt(index, chars)
        self.iny = self.log.get('0.0', 'end')

    def button1(self):
        self.inset_add('insert', '1')

    def button2(self):
        self.inset_add('insert', '2')

    def button3(self):
        self.inset_add('insert', '3')

    def button4(self):
        self.inset_add('insert', '4')

    def button5(self):
        self.inset_add('insert', '5')

    def button6(self):
        self.inset_add('insert', '6')

    def button7(self):
        self.inset_add('insert', '7')

    def button8(self):
        self.inset_add('insert', '8')

    def button9(self):
        self.inset_add('insert', '9')

    def button0(self):
        self.inset_add('insert', '0')

    def button_d(self):
        ipt = self.log.get('0.0', 'end')
        if len(ipt) == 1 or self.clear_input:
            self.inset_add('insert', '0.')
        elif ipt.find('.') == -1:
            self.inset_add('insert', '.')

    def algorithm(self, value):
        self.inx = self.log.get('0.0', 'end')
        self.calculated_value = value
        self.iny = self.inx
        self.clear_input = True

    def algorithm_plus(self):
        self.algorithm('+')

    def algorithm_reduce(self):
        self.algorithm('-')

    def algorithm_ride(self):
        self.algorithm('*')

    def algorithm_except(self):
        self.algorithm('/')

    def settlement(self):
        if self.inx is None:
            return

        if self.iny is None:
            return

        if type(self.inx) is str:
            try:
                self.inx = int(self.inx)
            except ValueError:
                try:
                    self.inx = float(self.inx)
                except ValueError:
                    self.inx = 0

        if type(self.iny) is str:
            try:
                self.iny = int(self.iny)
            except ValueError:
                try:
                    self.iny = float(self.iny)
                except ValueError:
                    self.inx = 0

        # print(self.inx, self.calculated_value, self.iny)

        if self.calculated_value == '':
            return
        elif self.calculated_value == '+':
            self.inx = self.inx + self.iny
        elif self.calculated_value == '-':
            self.inx = self.inx - self.iny
        elif self.calculated_value == '*':
            self.inx = self.inx * self.iny
        elif self.calculated_value == '/':
            self.inx = self.inx / self.iny

        self.inset_delete()
        self.inset_ipt('insert', self.inx)
        self.clear_input = True


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
