
class game_menus:

    def __init__(self, name, dir):
        self.name = name
        self.active_image = name + "_active.png"
        self.inactive_image = name + "_inactive.png"
        self.dir = dir