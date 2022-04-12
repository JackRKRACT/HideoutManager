
class requirement:

    def __init__(self, req_json, req_name):
        self.req_source = req_json
        self.req_name = req_name
        self.image_location = req_json.get("image_location", "No image location")
        self.required = req_json.get("required", 0)
        self.purchase_price_d = req_json.get("purchase_price_d",0)
        self.purchase_price_r = req_json.get("purchase_price_r", 0)
        self.purchase_price_eur = req_json.get("purchase_price_eur", 0)
        self.cheapest_trader = req_json.get("cheapest_trader", "none")