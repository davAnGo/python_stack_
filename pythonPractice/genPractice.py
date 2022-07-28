
class Carrier: # Define your class here
    # Class variable: list that will hold your carriers - this is 
    # how we can access individual Carriers when we cannot
    # otherwise do so
    all_carriers = [] 
    overseer = "FAA" # Class variable

    def __init__(self, year, name, city):
        self.year = year
        self.name = name
        self.city = city
        self.flights = [] # List of flights
        self.total_workers = 0 # Workforce for this carrier
        Carrier.all_carriers.append(self) # Add this carrier
        # self here is used to hold the info on this new carrier

    def rename_overseer(any_string):
            Carrier.overseer = any_string
            print(Carrier.overseer)

    Carrier.rename_overseer()