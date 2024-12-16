#Assignment 1 
# Designing a smartphone class

class Smartphone:
    def __init__ (self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def make_call(self, number):
            return f"Dialing {number} using {self.brand} {self.model}."
        
    def send_message(self, number , message):
            return f"Sending message to {number}: {message}"
        
# Devired class/ Subclass/ Child class/
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, health_features):
        super().__init__(brand, model,price)
        self.health_features = health_features
    
    # Overriding the make_call method
    
    def track_health(self):
        # return f"Tracking heart rate using {self.brand} {self.model}."
        # the join function is used to join the elements of the list into a string
        return f"Tracking: {','.join(self.health_features)}"
    
    # Test the classes
    # Create an object of the Smartwatch class
phone = Smartphone("Samsung", "Galaxy S22", 1000)
watch = Smartwatch("Apple", "iWatch", 500, ["Heart Rate","Steps","Sleep"])

# Test the method make_call of the Smartphone class
print(phone.make_call("1234567890"))

# Test the send_message method of the Smartphone class
print(phone.send_message("1234567890", "Hello! How are you?"))

# Test the make_call method of the Smartwatch class
# this is an inherited method from the Smartphone class
print(watch.make_call("1234567890")) 

# test the track_health method of the Smartwatch class
print(watch.track_health())

        


