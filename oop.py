#Assignment 1 
# Designing a smartphone class

class Smartphone:
    def __init__ (self, brand, model,price):
        self.brand= brand
        self.model= model
        self.price= price
        
        def make_call(self, number):
            return f"Dialing {number} using {self.brand} {self.model}."
        
        def send_message(self, number , message):
            return f"Sending message to {number}: {message}"
        
# Devired class/ Subclass/ Child class/
class Smartwatch(Smartphone):
    

