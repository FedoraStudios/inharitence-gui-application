from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")

#Burger image:
BurgerImg = ImageTk.PhotoImage(Image.open("burger1.png"))
BurgerImgLabel = Label(root)
BurgerImgLabel["image"] = BurgerImg
BurgerImgLabel.place(relx = 0.7, rely = 0.5, anchor=CENTER)

#Heading:
LabelHeading = Label(root, text="Burgers R Us", font = ("times", 40, "bold"))
LabelHeading.place(relx = 0.12, rely = 0.1, anchor=CENTER)

#SelectDish:
LabelSelectDish = Label(root, text="Select Dish", font = ("times", 40, "bold"))
LabelSelectDish.place(relx = 0.76, rely = 0.2, anchor=CENTER)

#Combobox Main Dish:
Dishes = ["Burger", "Iced_Americano"]
DishCombobox = ttk.Combobox(root, state="readonly", values=Dishes)
DishCombobox.place(relx = 0.25, rely = 0.2, anchor=CENTER)

#SelectAddons:
LabelSelectAddons = Label(root, text="Select Addons", font = ("times", 40, "bold"))
LabelSelectAddons.place(relx = 0.08, rely = 0.5, anchor=CENTER)

#Combobox Addons:
Addons = []
AddonsCombobox = ttk.Combobox(root, state="readonly", values=Addons)
AddonsCombobox.place(relx = 0.25, rely = 0.5, anchor=CENTER)

#Price:
LabelPrice = Label(root, font = ("times", 15, "bold"))
LabelPrice.place(relx = 0.2, rely = 0.75)

#Parent Class:

class Parent():
    
    def __init__(self):
        print("Parent Class")
        
    def Menu(Dish):
        
        if Dish == "Burger":
            print("Add following addons")
            Addons = ["Cheese", "Letuce"]
            AddonsCombobox["values"] = Addons
            
        elif Dish == "Iced_Americano":
            print("Add following addons")
            Addons = ["Chocolete", "Caramel"]
            AddonsCombobox["values"] = Addons
        else:
            print("Please enter a valid dish.")
            
    def FinalAmmount(Dish, Addons):
        
        if Dish == "Burger" and Addons == "Cheese":
            LabelPrice["text"] = "Price: $2.99 USD"
            
        elif Dish == "Burger" and Addons == "Letuce":
            LabelPrice["text"] = "Price: $3.50 USD"
        
        elif Dish == "Iced_Americano" and Addons == "Chocolate":
            LabelPrice["text"] = "Price: $4.99 USD"
            
        elif Dish == "Iced_Americano" and Addons == "Caramel":
            LabelPrice["text"] = "Price: $5.10 USD"
            
            
class ChildOne(Parent):
    
    def __init__(self, Dish):
        self.NewDish = Dish
        
    def GetMenu(self):
        NewDish = DishCombobox.get()
        Parent.Menu(NewDish)
        
        
class ChildTwo(Parent):
    
    def __init__(self, Dish, Addons):
        self.NewDish = Dish
        self.NewAddons = Addons
        
    def GetFinalAmmount(self):
        NewDish = DishCombobox.get()
        NewAddons = AddonsCombobox.get()
        Parent.FinalAmmount(NewDish, NewAddons)
        
ChildOneObj = ChildOne(DishCombobox.get())

        
ChildTwoObj = ChildTwo(DishCombobox.get(), AddonsCombobox.get())


ButtonAdd = Button(root, text = "Check Addons", command=ChildOneObj.GetMenu(), bg = "royal blue", fg = "White", relief = FLAT)
ButtonAdd.place(relx = 0.06, rely = 0.3, anchor=CENTER)
        

#ButtonAmmount = Button(root, text = "Price", command=ChildTwoObj.GetFinalAmmount(), bg = "royal blue", fg = "White", relief = FLAT)
#ButtonAmmount.place(relx = 0.04, rely = 0.6, anchor=CENTER)


root.mainloop()