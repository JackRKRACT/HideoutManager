from requirement import requirement
from tkinter import *
from tkinter import ttk
from json_handler import json_handler
import interaction as inta
# GUI to handle JSON / Crafts and Bot configuration & running

class hm_gui:

    def updateCraft(self, update_list, sub):
        root = self.json_crafts
        print("Probably will make a class here for crafts, seems way cleaner that way...")

    def attributeModule(self, frame, label, stringvar, type):
        if type == 0:
            sub_frame = Frame(frame)
            sub_frame.grid()
            Label(sub_frame, text=label).grid()
            Entry(sub_frame, textvariable=stringvar).grid()

    def editRequirement(self, current_item, requirements, frame):
        print("Editing requirement : " + current_item)
        
        edit_gui = Toplevel(frame)
        edit_gui.iconbitmap("resources\gui_elements\hm.ico")
        egui_frame = Frame(edit_gui)
        egui_frame.grid()

        # Attributes
        for req in requirements:
            if (req.req_name == current_item):
                item_name = StringVar(edit_gui, current_item)
                img_location = StringVar(edit_gui, req.image_location)
                required = StringVar(edit_gui, req.required)
                price_d = StringVar(edit_gui, req.purchase_price_d)
                price_r = StringVar(edit_gui, req.purchase_price_r)
                price_eur = StringVar(edit_gui, req.purchase_price_eur)
                trader = StringVar(edit_gui, req.cheapest_trader)

                self.attributeModule(egui_frame, "Item : ", item_name, 0)
                self.attributeModule(egui_frame, "Image location : ", img_location, 0)
                self.attributeModule(egui_frame, "Amount required : ", required, 0)
                self.attributeModule(egui_frame, "Price in Dollars : ", price_d, 0)
                self.attributeModule(egui_frame, "Price in Roubles : ", price_r, 0)
                self.attributeModule(egui_frame, "Price in Euros : ", price_eur, 0)
                self.attributeModule(egui_frame, "Cheapest Trader : ", trader, 0)
                
                Button(egui_frame, text="Update Craft", command=self.updateCraft).grid()

    def findCraft(self, craft_name, craft_list):
        for craft in craft_list:
            if craft_name == craft.craft_name:
                return craft

    # Some issue with double requirements?
    def editCraft(self, craft_name, craft_list):
        print("Editing selected craft")
        edit_gui = Toplevel(self.crafts)
        edit_gui.iconbitmap("resources\gui_elements\hm.ico")
        egui_frame = Frame(edit_gui)
        egui_frame.grid()
        curr_craft = self.findCraft(craft_name, craft_list)
        # Attributes
        requirements = curr_craft.req_list
        print("Req length of current craft : " + str(len(requirements)))
        req_names = []
        for req in requirements:
            req_names.append(req.req_name)
        items_var = StringVar(value=req_names)
        list = Listbox(egui_frame, height=10, listvariable=items_var)
        list.grid()
        edit_selected = Button(egui_frame, text="Edit Requirement", command=lambda: self.editRequirement(list.get(list.curselection()), requirements, edit_gui)).grid()

        item_name = StringVar(edit_gui, curr_craft.craft_name)
        img_location = StringVar(edit_gui, curr_craft.image_location)
        module = StringVar(edit_gui, curr_craft.module)
        amount_produced = StringVar(edit_gui, curr_craft.produced)
        time_in_min = StringVar(edit_gui, curr_craft.time_in_min)
        sell_price = StringVar(edit_gui, curr_craft.sell_price)

        self.attributeModule(egui_frame, "Item : ", item_name, 0)
        self.attributeModule(egui_frame, "Image location : ", img_location, 0)
        self.attributeModule(egui_frame, "Hideout Module : ", module, 0)
        self.attributeModule(egui_frame, "Amount per Production : ", amount_produced, 0)
        self.attributeModule(egui_frame, "Time (min) : ", time_in_min, 0)
        self.attributeModule(egui_frame, "Sell price (R) : ", sell_price, 0)

    def createCraft(self):
        print("Creating new craft")

    def selectJSON(self):
        print("Selecting new JSON file")

    def editCrafts(self):
        print("Opening crafts menu")
        self.crafts = Toplevel(self.root)
        self.crafts.iconbitmap("resources\gui_elements\hm.ico")
        crafts_frame = Frame(self.crafts)
        crafts_frame.grid()
        define = Label(crafts_frame, text="List of crafts").grid()
        items = []
        for item in self.json_handler.craft_list:
            items.append(item.craft_name)
            print("Checking insanity")
            print(len(item.req_list))
        items_var = StringVar(value=items)
        list = Listbox(crafts_frame, height=10, listvariable=items_var)
        list.grid()
        edit_selected = Button(crafts_frame, text="Edit Craft", command=lambda: self.editCraft(list.get(list.curselection()), self.json_handler.craft_list)).grid()
        attempt_craft = Button(crafts_frame, text="Attempt Craft", command=lambda: self.attemptCraft(list.get(list.curselection()), self.json_handler.craft_list)).grid()
        create_craft = Button(crafts_frame, text="Create Craft", command=self.createCraft).grid()
        select_json_file = Button(crafts_frame, text="Select Configuration File", command=self.selectJSON).grid()

    # Will probably remove later, or move to the button itself. Who knows.
    def attemptCraft(self, craft_name, craft_list):
        print("Attempting craft : " + craft_name)
        for craft in craft_list:
            if craft.craft_name == craft_name:
                inta.performCraft(craft, inta.getModule(craft.module, self.modules))

    def __init__(self):
        self.json_handler = json_handler("crafts.json")
        self.modules = inta.loadModules()
        self.root = Tk()
        self.root.title("Manager")
        self.root.iconbitmap("resources\gui_elements\hm.ico")
        b_frame = Frame(self.root)
        b_frame.pack()
        edit_crafts_b = Button(b_frame, text="Edit Crafts", command=self.editCrafts)
        edit_crafts_b.pack()
        self.root.mainloop()
    
