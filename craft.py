from requirement import requirement

# Provides craft image to 'interaction.py'
# Provides requirement images to 'interaction.py'
# Provides craft details to 'hm_gui.py'
class craft:

    # Takes in the isolated JSON code for itself and gets the resources for craft and requirements.
    def __init__(self, craft_json, craft_name):
        self.craft_name = craft_name
        self.craft_source = craft_json
        self.image_location = craft_json.get("image_location", "No location")
        self.module = craft_json.get("module", "No module")
        self.produced = craft_json.get("produced", 0)
        self.time_in_min = craft_json.get("time_in_min", 0)
        self.sell_price = craft_json.get("sell_price", 0)
        req_json = craft_json.get("requirements")
        self.req_list = self.getRequirements(req_json)
        
    # Produces images and whatnot for the craft's requirements.
    def getRequirements(self, req_json):
        keys = req_json.keys()
        req_list = []

        for req in keys:
            sub_json = req_json.get(req)
            req_list.append(requirement(sub_json, req))
        return req_list
        