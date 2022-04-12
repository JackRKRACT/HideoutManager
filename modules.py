
class modules:

    def __init__(self, name, cv_img, dir):
        self.name = name
        self.active_image = name + "_active.png"
        self.inactive_image = name + "_inactive.png"
        self.image = cv_img
        self.dir = dir