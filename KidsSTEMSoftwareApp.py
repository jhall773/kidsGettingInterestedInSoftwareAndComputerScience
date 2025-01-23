import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas
from tkinter.messagebox import showerror
import random

#The base of this code and its structure was adapted from the code at https://www.pythontutorial.net/tkinter/tkraise/

class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.image = app.image
        self.image2 = app.image2

        # field options
        options = {'padx': 5, 'pady': 0}

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        
        #Starter button
        self.convert_button_software_start = ttk.Button(self, text='Software/Coding')
        self.convert_button_software_start.grid(column=1, row=0, sticky='w')
        self.convert_button_software_start.configure(command=self.convert_from_starter_software)

        #Starter button
        self.convert_button_hardware_start = ttk.Button(self, text='Computer Hardware/Circuits')
        self.convert_button_hardware_start.grid(column=1, row=2, sticky='w')
        #self.convert_button_hardware_start.configure(command=self.convert_from_starter)

        #Starter button
        self.convert_button_physical_start = ttk.Button(self, text='Mechanical/Industrial & Physical Design')
        self.convert_button_physical_start.grid(column=2, row=2, sticky='w')
        #self.convert_button_physical_start.configure(command=self.convert_from_starter)


    def convert_from_starter_software(self, event=None):
        #Handle startbutton click event
        self.convert_button_software_start.destroy()
        self.convert_button_hardware_start.destroy()
        self.convert_button_physical_start.destroy()
        
        # declaring string variable for storing user input attribute guesses
        attribute_var=tk.StringVar()

        self.attribute_count = 3
        self.first_time_brew = 1
        self.first_time_price = 1
        self.first_time_size = 1
        # defining a function that will get student's guesses for good attributes and let them know if they were right.
        def submit():
            if(self.attribute_count > 0):
                attribute= (attribute_var.get()).lower()
                match attribute:
                    case ("type" | "brew"):
                        if(self.first_time_brew == 1):
                            self.attribute_count = self.attribute_count - 1
                            messagebox.showinfo(message= f"{attribute}: This attribute would definitely be needed! You still have {self.attribute_count} attributes left to type.")
                            self.first_time_brew = 0
                        else:
                            messagebox.showinfo(message="You typed this attribute already. Let's type the other ones.")

                    case ("price" | "cost"):
                        if(self.first_time_price==1):
                            self.attribute_count = self.attribute_count - 1
                            messagebox.showinfo(message= f"{attribute}: This attribute would definitely be needed! You still have {self.attribute_count} attributes left to type.")
                            self.first_time_price = 0
                        else:
                            messagebox.showinfo(message="You typed this attribute already. Let's type the other ones.")

                    case "size":
                        if(self.first_time_size==1):
                            self.attribute_count = self.attribute_count - 1
                            messagebox.showinfo(message= f"{attribute}: This attribute would definitely be needed! You still have {self.attribute_count} attributes left to type.")
                            self.first_time_size = 0
                        else:
                            messagebox.showinfo(message="You typed this attribute already. Let's type the other ones.")

                    case _:
                        messagebox.showerror(message= f"{attribute}: This attribute wasn't quite what I would look for! Try typing something else.")  
    
                attribute_var.set("")
            if(self.attribute_count <=0):
                sub_btn.destroy()
                hint_button.destroy()
                name_label.destroy()
                name_entry.destroy()
                self.CONTINUE2()
        #Creates the messagebox for the hint after you press the hint button.
        def hint():
            messagebox.showinfo(message="Here are your hints for these attributes:\n1. Think about it. All coffee drinks aren't the same. So each coffee item must have a certain t___\n2. Think about any store or shop. You can't buy it unless you know the ___\n3. When your at any food place that sells drinks, you may get a small, medium, or large cup. This attribute starts with an \"s\"")

        # creating a label for 
        # name using widget Label
        name_label = tk.Label(self, text = 'Please type an attribute/feature of a coffee shop coffee drink\n(One example could be "size", since most coffee shops\nlet customers order small, medium, or large coffee drinks. You will need to find 3 different attributes):', font=('calibre',10, 'bold'))
 
        # creating a entry for input
        # name using widget Entry
        name_entry = tk.Entry(self,textvariable = attribute_var, font=('calibre',10,'normal'))


        # creating a button using the widget 
        # Button that will call the submit function 
        sub_btn=tk.Button(self, text = 'Submit', command = submit)

        #Button that will give the user a hint
        hint_button=tk.Button(self, text= 'Click here for hints on the attributes', command = hint, wraplength=50)
 
        # placing the label and entry in
        # the required position using grid
        # method
        name_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1)
        hint_button.grid(row=4, column=1)
        sub_btn.grid(row=2,column=1)


    def store_coffee_names(self):
            coffee_name = self.coffee_name_var.get()
            count = count + 1
            match count:
                case 1:
                    self.coffee_name1 = coffee_name
                    messagebox(message= f"Your ")
                case 2:
                    self.coffee_name2 = coffee_name
                case 3:
                    self.coffee_name3 = coffee_name


        
    def CONTINUE2(self, event=None):
        # declaring string variable for storing user input attribute guesses
        coffee_name_var=tk.StringVar()
        coffee_price_var=tk.DoubleVar()

        self.coffee_name1 = ""
        self.coffee_price1 = 0.00
    
        self.coffee_name2 = ""
        self.coffee_price2 = 0.00

        self.coffee_name3 = ""
        self.coffee_price3 = 0.00

        self.coffee_name_count = 0
        self.name_count = 0

        def store_coffee_names():
            coffee_name = coffee_name_var.get()
            coffee_price = coffee_price_var.get()

            self.name_count = self.name_count + 1
            match self.name_count:
                case 1:
                    self.coffee_name1 = coffee_name
                    self.coffee_price1 = coffee_price
                    messagebox.showinfo(message=f"Coffee brew 1 of 3 entered! Price for a small is: $ {coffee_price}, Price for medium is: $ {coffee_price+.5}, Price for a large is: $ {coffee_price+.75}")
                case 2:
                    self.coffee_name2 = coffee_name
                    self.coffee_price2 = coffee_price
                    messagebox.showinfo(message=f"Coffee brew 2 of 3 entered! Price for a small is: $ {coffee_price}, Price for medium is: $ {coffee_price+.5}, Price for a large is: $ {coffee_price+.75}" )
                case 3:
                    self.coffee_name3 = coffee_name
                    self.coffee_price3 = coffee_price
                    messagebox.showinfo(message=f"Coffee brew 3 of 3 entered! Price for a small is: $ {coffee_price}, Price for medium is: $ {coffee_price+.5}, Price for a large is: $ {coffee_price+.75}" )
                    coffee_label.destroy()
                    coffee_entry.destroy()
                    coffee_label_price.destroy()
                    coffee_entry_price.destroy()
                    coffee_name_submit.destroy()
                    self.CONTINUE3()

        # placing the label and entry in
        # the required position using grid
        # method
        coffee_label= tk.Label(self, text="Enter a coffee type/brew to create a coffee object\n(One example may be \"Espresso\", \"Mocha\", or \"Cappuccino\"): ", font=('calibre',10, 'bold'))
        coffee_entry= tk.Entry(textvariable=coffee_name_var)
        coffee_label.grid(row=0,column=0)
        coffee_entry.grid(row=0,column=1)

        coffee_label_price= tk.Label(self, text="Enter a price for the coffee type/brew above: ", font=('calibre',10, 'bold'))
        coffee_entry_price= tk.Entry(textvariable=coffee_price_var)
        coffee_label_price.grid(row=2,column=0)
        coffee_entry_price.grid(row=2,column=1)

        coffee_name_submit = tk.Button(self, text="Submit", command=store_coffee_names)
        coffee_name_submit.grid(row=4,column=1)     
        
    
    def CONTINUE3(self):
        #quit()
        # declaring string variable for storing user input attribute guesses
        coffee_code_answer_var=tk.StringVar()
        self.totalp = 0
        self.order = "Here is your order:\n"
        self.order_code = ""

        
        def item_info():
            messagebox.showinfo(message=f"Coffee Type1: {self.coffee_name1}, small price: {self.coffee_price1}\nCoffee Type2: {self.coffee_name2}, small price: {self.coffee_price2}\nCoffee Type3: {self.coffee_name3}, small price: {self.coffee_price3}")

        def order_info():
            messagebox.showinfo(message=f"Order:\n{self.order}")
        
        def order_answer():
            messagebox.showinfo(message=f"Code:\n{self.order_code}")
        
        def instructions():
            messagebox.showinfo(message="Look at your given order by a random customer and create the three coffee items needed to place the order with the place_order() function in the example.\n(To do this write the exact same syntax as what is circled in red the example, but just change the brewtype, size, and price [either small_price, medium_price = small_price + .50, or large_price = small_price + .75] according to your specific customer order.)")

        
        def create_order():
            loop=1
            while(loop < 4):
                t = random.randrange(1, 4)
                s = random.randrange(1, 4)

                match t, s:
                    case 1, 1:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name1}, Size: small, Price: ${self.coffee_price1}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1}, brew_type=\"{self.coffee_name1}\", size=\"small\")\n"
                        self.totalp = self.totalp + self.coffee_price1
                    case 1, 2:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name1}, Size: medium, Price: ${self.coffee_price1+0.50}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1}, brew_type=\"{self.coffee_name1}\", size=\"medium\")\n"
                        self.totalp = self.totalp + self.coffee_price1+.50
                    case 1, 3:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name1}, Size: large, Price: ${self.coffee_price1+0.75}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1}, brew_type=\"{self.coffee_name1}\", size=\"large\")\n"
                        self.totalp = self.totalp + self.coffee_price1+0.75
            
                    case 2, 1:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name2}, Size: small, Price: ${self.coffee_price2}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2}, brew_type=\"{self.coffee_name2}\", size=\"small\")\n"
                        self.totalp = self.totalp + self.coffee_price2
                    case 2, 2:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name2}, Size: medium, Price: ${self.coffee_price2+0.5}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2}, brew_type=\"{self.coffee_name2}\", size=\"medium\")\n"
                        self.totalp = self.totalp + self.coffee_price2+.5
                    case 2, 3:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name2}, Size: large, Price: ${self.coffee_price2+0.75}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2}, brew_type=\"{self.coffee_name2}\", size=\"large\")\n"
                        self.totalp = self.totalp + self.coffee_price2+.75
            
                    case 3, 1:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name3}, Size: small, Price: ${self.coffee_price3}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3}, brew_type=\"{self.coffee_name3}\", size=\"small\")\n"
                        self.totalp = self.totalp + self.coffee_price3
                    case 3, 2:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name3}, Size: medium, Price: ${self.coffee_price3+0.5}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3}, brew_type=\"{self.coffee_name3}\", size=\"medium\")\n"
                        self.totalp = self.totalp + self.coffee_price3+.5
                    case 3, 3:
                        self.order = self.order + f"\n{loop}. Coffee: {self.coffee_name3}, Size: large, Price: ${self.coffee_price3+0.75}"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3}, brew_type=\"{self.coffee_name3}\", size=\"large\")\n"
                        self.totalp = self.totalp + self.coffee_price3+.75
                loop = loop +1
            self.order = self.order + f"\nTotal: {self.totalp}"
            print(self.order)
            print(self.order_code)

        def check():  
            answer = answer_entry.get(1.0, 'end-1c')
            print("Code:\n", self.order_code)
            print("Answer:\n", answer)
            if(answer.rstrip() == (self.order_code).rstrip()):
                messagebox.showinfo(message="That is correct! Hope you learned something new!")
                answer_label.destroy()
                answer_entry.destroy()
                code_class.destroy()
                customer_order.destroy()
                My_shop.destroy()
                give_up.destroy()
                submitFinal.destroy()
                repeat_instruction.destroy()
                self.CONTINUE_END()
            else:
                messagebox.showinfo(message="Unforteunately, this answer is not correct. Please try again or press the \"See the answer\" button.")
           
        # placing the label and entry in
        # the required position using grid
        # method
        
        create_order()

        messagebox.showinfo(message="Look at your given order by a random customer and create the threee coffee items needed to place the order with the place_order() function in the example. (To do this write the exact same syntax as what is circled in red the example, but just change the brewtype, size, and price [either small_price, medium_price = small_price + .50, or large_price = small_price + .75] according to your specific customer order.)")

        answer_label= tk.Label(text="Type Answer Code", font=('calibre',5, 'bold'))
        answer_entry= tk.Text(height=10, width=50)
        answer_label.grid(row=0, column=0)
        answer_entry.grid(row=0, column=1)

        submitFinal = tk.Button(text="submit answer code", command=check)
        submitFinal.grid(row=0, column=3)

        
        code_class= tk.Label(width=600, height=400, text="See Example!", image=self.image2)
        code_class.grid(row=1, column=0)

        customer_order = tk.Button(text="Customer Order", command=order_info)
        customer_order.grid(row=100, column=1)

        My_shop = tk.Button(text="My Shop items", command=item_info)
        My_shop.grid(row=100, column=3)

        repeat_instruction = tk.Button(text="Instructions", command=instructions)
        repeat_instruction.grid(row=100, column=5)

        give_up = tk.Button(text="See the answer.", command=order_answer)
        give_up.grid(row=100, column=7)

    def CONTINUE_END():
        def end():
            quit()
        
        tk.Button(text="END. Back to Main Menu.", command= end)


        """
        coffee_entry= tk.Entry(textvariable=coffee_name_var)
        coffee_label.grid(row=0,column=0)
        coffee_entry.grid(row=0,column=1)

        coffee_label_price= tk.Label(self, text="Enter a price for the coffee type/brew above: ", font=('calibre',10, 'bold'))
        coffee_entry_price= tk.Entry(textvariable=coffee_price_var)
        coffee_label_price.grid(row=2,column=0)
        coffee_entry_price.grid(row=2,column=1)

        coffee_name_submit = tk.Button(self, text="Submit", command=store_coffee_names)
        coffee_name_submit.grid(row=4,column=1)
        """

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # push buttons
        self.selected_value = tk.IntVar()


        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container)
        
        self.frames[1] = ConverterFrame(
            container)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        #frame.reset()
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Learning About STEM!')
        self.geometry('800x1200')
        self.resizable(False, False)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')
        self.geometry('800x1200')

        self.image = tk.PhotoImage(file='./Coffee_Item_Defined_2.png')
        self.image2 = tk.PhotoImage(file='./Coffee_Shop_Code.png', width=500, height=400)

"""
if __name__ == "__main__":
    app = App()
    app.mainloop()
"""

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()
