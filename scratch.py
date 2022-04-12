        top = tkinter.Tk()
        top.title("Manager_v2")
        top.iconbitmap("resources\gui_elements\hm.ico")
        frame = tkinter.Frame(top)
        frame.pack()
        craft_b = tkinter.Button(frame, text="New craft", command=self.test_callback)
        craft_b.pack(side = tkinter.LEFT)
        craft_b = tkinter.Button(frame, text="Edit crafts", command=self.test_callback)
        craft_b.pack(side = tkinter.LEFT)
        craft_b = tkinter.Button(frame, text="Start HideoutManger", command=self.test_callback)
        craft_b.pack(side = tkinter.LEFT)
        var = tkinter.StringVar()
        bottomframe = tkinter.Frame(top)
        bottomframe.pack( side = tkinter.BOTTOM )
        label = tkinter.Label(bottomframe, textvariable = var)
        var.set("Status : Idle")
        label.pack()
        top.mainloop()

        "image_location":"ex.png",
        "module":"workbench",
        "produced":1,
        "time_in_min":93,
        "sell_price":51111,

        Label(egui_frame, text="Item : ").grid()
        Entry(egui_frame, textvariable=item_name).grid()
        Label(egui_frame, text="Image location : ").grid()
        Entry(egui_frame, textvariable=img_location).grid()
        Label(egui_frame, text="Hideout Module : ").grid()
        Entry(egui_frame, textvariable=module).grid()
        Label(egui_frame, text="Amount per Production : ").grid()
        Entry(egui_frame, textvariable=amount_produced).grid()
        Label(egui_frame, text="Time (min) : ").grid()
        Entry(egui_frame, textvariable=time_in_min).grid()
        Label(egui_frame, text="Sell price (R) : ").grid()
        Entry(egui_frame, textvariable=sell_price).grid()
        Button(egui_frame, text="Update Craft", command=self.updateCraft).grid()


        elif (len(findImageScreen(bottom_bound)) != 0 or len(findImageScreen(top_bound)) != 0):
            # Found a bound. Changing directions!
            print("Found a bound. Changing dir")
            is_top = not is_top
        if (is_top):
            for x in range(10):
                pyautogui.scroll(-1)
            time.sleep(1)
        else:
            for x in range(10):
                pyautogui.scroll(1)
            time.sleep(1)


# Pass this the crafting region array, returns location array of required items
def getRequirements(craft_region):
    return
# Pass this the crafting region array, returns location of array of produced item
def getProduced(craft_region):
    return
# Pass this item location (as an array), moves mouse to target location and returns highlighted item image
def parseItem(item_location):
    return
# Pass this a cv_image and a directory, will write image out as 'name' to target directory.
def imageFile(cv_image, directory, name):
    return