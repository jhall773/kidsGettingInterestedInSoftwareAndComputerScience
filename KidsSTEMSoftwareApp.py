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
        self.image3 = app.image3
        self.image4 = app.image4

        # field options
        options = {'padx': 5, 'pady': 0}

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.main_menu()
    

    def main_menu(self): #Button that repeats the "Main_Menu" buttons above after every Software/Computer Engineering & Computer Science Discipline Activity is Over
        #Starter button
        self.convert_button_software_start = ttk.Button(self, text='Software/Object-Oriented-Programming')
        self.convert_button_software_start.grid(column=1, row=0, sticky='w')
        self.convert_button_software_start.configure(command=self.convert_from_starter_software)

        #Starter button
        self.convert_button_hardware_start = ttk.Button(self, text='Binary & Logic Design')
        self.convert_button_hardware_start.grid(column=1, row=2, sticky='w')
        self.convert_button_hardware_start.configure(command=self.convert_from_starter_Logic)

        #Starter button
        self.convert_button_physical_start = ttk.Button(self, text='Instruction Set Arcitecture')
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
                    case ("type" | "brew" | "flavor"):
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
                sub_button.destroy()
                hint_button.destroy()
                name_label.destroy()
                name_entry.destroy()
                Pic_Type.destroy()
                Pic_Size.destroy()
                Pic_Price.destroy()
                self.CONTINUE2()

        #Creates the messagebox for the hint after you press the hint button.
        def hint():
            messagebox.showinfo(message="Here are your hints for these attributes:\n1. Think about it. All coffee drinks aren't the same. So each coffee item must have a certain t___\n2. Think about any store or shop. You can't buy it unless you know the ___\n3. When your at any food place that sells drinks, you may get a small, medium, or large cup. This attribute starts with an \"s\"")

        # creating a label for 'name' entry box using widget Label (so user can type in their attribute guess)
        name_label = tk.Label(self, text = 'Welcome to Object-Oriented-Programming!\nPlease type an attribute/feature of a coffee shop coffee drink\n(One example could be "size", since most coffee shops\nlet customers order small, medium, or large coffee drinks. You will need to find 3 different attributes):', font=('calibre',10, 'bold'))
 
        # creating a entry box for input 'name' using widget Entry (so user can type in their attribute guess)
        name_entry = tk.Entry(self,textvariable = attribute_var, font=('calibre',10,'normal'))


        # creating a button using the widget 
        # Button that will call the submit function 
        sub_button=tk.Button(self, text = 'Submit', command = submit)

        #Button that will give the user a hint
        hint_button=tk.Button(self, text= 'Click here for hints on the attributes', command = hint, wraplength=50)


        #Button that will give the user a hint
        Pic_Type=tk.Label(self, image=self.image)
        Pic_Type.grid(row=20, column=0)

        #Button that will give the user a hint
        Pic_Size=tk.Label(self, image=self.image2)
        Pic_Size.grid(row=20, column=1)

        #Button that will give the user a hint
        Pic_Price=tk.Label(self, image=self.image3)
        Pic_Price.grid(row=400, column=1)



        # placing the label and entry in the required position using grid method
        name_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1)
        hint_button.grid(row=4, column=1)
        sub_button.grid(row=2,column=1)

        
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


        def store_coffee_names(): #Function that handles storing the three coffee objects the user makes by giving a coffee name/type and a price for each.
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

        # This allows the user to create three coffee items by entering into a text box (with the Entry() object) a name/brew type and price for each. 
        coffee_label= tk.Label(self, text="Enter a coffee type/brew to create a coffee object\n(One example may be \"Espresso\", \"Mocha\", or \"Cappuccino\" or any other name you desire.): ", font=('calibre',10, 'bold'))
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
        #Variables used to store the randomly generated order a customer makes, and the code that would create that order.
        self.totalp = 0
        self.order = ""
        self.order_code = ""

        # Functions called when users press the buttons to navigate the activity after the create_order() function creates an order.
        def item_info():
            messagebox.showinfo(message=f"Coffee Type1: {self.coffee_name1}, small price: {self.coffee_price1}\nCoffee Type2: {self.coffee_name2}, small price: {self.coffee_price2}\nCoffee Type3: {self.coffee_name3}, small price: {self.coffee_price3}")

        def order_code():
            messagebox.showinfo(message=f"Code Used to Create Order Items:\n\n{self.order_code}")

        def order_ticket_example():
            example ="""
                        Code (in Python):
                        item_1 = w(price_small=0.00, brew_type="w", size="medium")
                        item_2 = x(price_small=0.00, brew_type="x", size="large")
                        item_3 = x(price_small=0.00, brew_type="x", size="small")
                        
                        Customer Order:
                        1. Coffee: w, Size: medium, Price: $0.50
                        2. Coffee: x, Size: large, Price: $0.75
                        3. Coffee: x, Size: small, Price: $0.00
                        Total: 1.25
                     """
            messagebox.showinfo(title=f"Order Ticket Example", message=example)
        
        def order_ticket_answer():
            messagebox.showinfo(message=f"Order Ticket Answer:\n{self.order}")
        
        def instructions():
            messagebox.showinfo(message="Based on the code used to create three coffee items for a random customer order and the print statements in the place_order() function above it (view the 'Code Snippet' on the lefthand side), write the customer's original order ticket [see 'Order Ticket Example' for the format. An example is also shown in the output terminal of the 'Code Snippet'].)\nNote: The 'medium_coffee' prices is your small_coffee price + .50 and the 'large_coffee' prices is your small coffee price + .75")

        #Order is created based on user input mixed with syntax I created for the Coffee Shop Drinks in the KidsSTEMSoftwareApp.py
        def create_order():
            loop=1
            while(loop < 4):
                t = random.randrange(1, 4)
                s = random.randrange(1, 4)

                match t, s:
                    case 1, 1:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name1}, Size: small, Price: ${self.coffee_price1:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1:.2f}, brew_type=\"{self.coffee_name1}\", size=\"small\")\n"
                        self.totalp = round(self.totalp + self.coffee_price1, 2)
                    case 1, 2:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name1}, Size: medium, Price: ${self.coffee_price1+0.50:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1:.2f}, brew_type=\"{self.coffee_name1}\", size=\"medium\")\n"
                        self.totalp = round(self.totalp + self.coffee_price1+.50, 2)
                    case 1, 3:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name1}, Size: large, Price: ${self.coffee_price1+0.75:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name1}(price_small={self.coffee_price1:.2f}, brew_type=\"{self.coffee_name1}\", size=\"large\")\n"
                        self.totalp = round(self.totalp + self.coffee_price1+0.75, 2)
            
                    case 2, 1:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name2}, Size: small, Price: ${self.coffee_price2:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2:.2f}, brew_type=\"{self.coffee_name2}\", size=\"small\")\n"
                        self.totalp = round(self.totalp + self.coffee_price2, 2)
                    case 2, 2:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name2}, Size: medium, Price: ${self.coffee_price2+0.5:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2:.2f}, brew_type=\"{self.coffee_name2}\", size=\"medium\")\n"
                        self.totalp = round(self.totalp + self.coffee_price2+.5, 2)
                    case 2, 3:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name2}, Size: large, Price: ${self.coffee_price2+0.75:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name2}(price_small={self.coffee_price2:.2f}, brew_type=\"{self.coffee_name2}\", size=\"large\")\n"
                        self.totalp = round(self.totalp + self.coffee_price2+.75, 2)
            
                    case 3, 1:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name3}, Size: small, Price: ${self.coffee_price3:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3:.2f}, brew_type=\"{self.coffee_name3}\", size=\"small\")\n"
                        self.totalp = round(self.totalp + self.coffee_price3, 2)
                    case 3, 2:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name3}, Size: medium, Price: ${self.coffee_price3+0.5:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3:.2f}, brew_type=\"{self.coffee_name3}\", size=\"medium\")\n"
                        self.totalp = round(self.totalp + self.coffee_price3+.5, 2)
                    case 3, 3:
                        self.order = self.order + f"{loop}. Coffee: {self.coffee_name3}, Size: large, Price: ${self.coffee_price3+0.75:.2f}\n"
                        self.order_code = self.order_code + f"item_{loop} = {self.coffee_name3}(price_small={self.coffee_price3:.2f}, brew_type=\"{self.coffee_name3}\", size=\"large\")\n"
                        self.totalp = round(self.totalp + self.coffee_price3+.75, 2)
                loop = loop +1
            self.order = self.order + f"Total: ${self.totalp:.2f}"
            print(self.order)
            print(self.order_code)

        def check():  #Checks to see if the user's answer code entered into the answer Textbox matches the correctly generated answer code
            answer = answer_entry.get(1.0, 'end-1c')
            print("Code:\n", self.order_code)
            print("Answer:\n", answer)
            if(answer.rstrip() == (self.order).rstrip()):
                messagebox.showinfo(message="That is correct! Hope you learned something new!")
                answer_label.destroy()
                answer_entry.destroy()
                order_example.destroy()
                code_pic.destroy()
                customer_order.destroy()
                My_shop.destroy()
                give_up.destroy()
                submitFinal.destroy()
                repeat_instruction.destroy()
                self.main_menu()
            else:
                messagebox.showinfo(message="Unforteunately, this answer is not correct. Please try again or press the \"See the answer\" button.")
           
        # placing the label and entry in
        # the required position using grid
        # method
        
        create_order() # Fuction is called to create the order here.

        messagebox.showinfo(message="Based on the code used to create three coffee items for a random customer order and the print statements in the place_order() function above it (view the 'Code Snippet' on the lefthand side), write the customer's original order ticket [see 'Order Ticket Example' for the format. An example is also shown in the output terminal of the 'Code Snippet'].)\nNote: The 'medium_coffee' prices is your small_coffee price + .50 and the 'large_coffee' price is your small coffee price + .75")

        #Textbox to type answer code
        answer_label= tk.Label(text="Type Customer Order:", font=('calibre', 20, 'bold'))
        answer_entry= tk.Text(height=10, width=50)
        answer_label.grid(row=0, column=0)
        answer_entry.grid(row=0, column=1)

        submitFinal = tk.Button(text="submit order ticket answer", command=check)
        submitFinal.grid(row=0, column=3)

        #Label box that shows a customer order ticket example based on order_code
        code_pic = tk.Label(image=self.image4)
        code_pic.grid(row=1, column=0)

        #Button to show order ticket example based on order code
        order_example = tk.Button(text="Order Ticket Example", command=order_ticket_example)
        order_example.grid(row=50, column=1)

        #Button to review the customer order_code
        customer_order = tk.Button(text="Order Code", command=order_code)
        customer_order.grid(row=100, column=1)

        #Button to review your coffee items
        My_shop = tk.Button(text="My Shop items", command=item_info)
        My_shop.grid(row=100, column=3)

        #Button to repeat the instructions
        repeat_instruction = tk.Button(text="Instructions", command=instructions)
        repeat_instruction.grid(row=100, column=5)

        #Button to see the order_ticket answer
        give_up = tk.Button(text="See the answer.", command=order_ticket_answer)
        give_up.grid(row=100, column=7)


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
    










    def convert_from_starter_Logic(self, event=None):
        #Handle startbutton click event
        self.convert_button_software_start.destroy()
        self.convert_button_hardware_start.destroy()
        self.convert_button_physical_start.destroy()

        introduction = tk.Label(self, text='Welcome to Binary & Logic Design!\n\nYou may have been told before that binary in its most basic form is just a combination of 0\'s and 1\'s.\nIn logic and design, 0 usually represents something being \'OFF\' or \'False\' in a computer program or logic circuit,\nwhile 1 usually represents something being \'ON\' or \'True\'. So, what if we could make some logic tables,\nin order to help us solve problems for a wide range of systems.\n\nDoesn\'t sound fun, yet?! Well how about I put you in one of those systems!\nAn escape house?! Use the right combonations of levers, buttons, and switches to escape (using logic tables of course)!')
        introduction.grid(row=10, column=10)

        def DELETE_CONTINUE():
            introduction.destroy()
            next_page.destroy()
            self.CONTINUE_LOGIC()

        next_page = tk.Button(text="NEXT", command=DELETE_CONTINUE)
        next_page.grid(row=10, column=100)
        

    
    def CONTINUE_LOGIC(self):
        intro_example = tk.Label(self, text="Before we start, let me give an example. Let's say I have 4 keys for four different doors respectively (one wooden door, the next metal, the next one glass, and the last one ceramic) next to each other in a row.\nIf the door I need to go through is not on either end (meaning not the first or the last door), and the door is not made of glass, which key do I use?\nIt's probably obvious that you use the 2nd key becuase the only option left is the metal door, but let's show that in a binary table.")
        intro_example.grid(row=10, column=10)

        def showTable():
            Table=f"""\tWood\tMetal\tGlass\tCeramic
                    0\t     0 \t    0 \t       0
                    0\t     0 \t    0 \t       1
                    0\t     0 \t    1 \t       0
                    0\t     0 \t    1 \t       1
                    0\t     1 \t    0 \t       0
                    0\t     1 \t    0 \t       1
                    0\t     1 \t    1 \t       0
                    0\t     1 \t    1 \t       1   
                    1\t     0 \t    0 \t       0
                   """
            messagebox.showinfo(message=f"{Table}\n\nBased on this table, can you tell which line/row resembles our successful scenario? Note: '0' represents a 'INCORRECT/INVALID' door while '1' is the 'CORRECT_DOOR'.")
            DELETE_CONTINUE2()

        next_page = tk.Button(text="Binary Table", command=showTable)
        next_page.grid(row=20, column=10)

        def DELETE_CONTINUE2():
            intro_example.destroy()
            next_page.destroy()
            self.CONTINUE_LOGIC2()

    def CONTINUE_LOGIC2(self):
        more_stuff=""












































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

        self.image = tk.PhotoImage(file='./Coffee_Types.png',width=300, height=200)
        self.image2 = tk.PhotoImage(file='./Coffee_Sizes.png', width=200,height=274)
        self.image3 = tk.PhotoImage(file='./Price.png', width=200, height=200)
        self.image4 = tk.PhotoImage(file='./Coffee_Shop_Code.png', width=600, height=251)

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()
