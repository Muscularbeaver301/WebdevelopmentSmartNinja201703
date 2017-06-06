class Vehicle(object):
    def __init__(self, brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

    def show(self):
        print "{} {} {} {}".format(self.brand, self.model, self.km, self.service_date)


if __name__ == '__main__':
    All_Vehicles = [
        Vehicle("Audi", "A5", "14000", "2017.01.01"),
        Vehicle("Renault", "Espace", "32000", "2017.03.01")
    ]

    while True:
        answer = raw_input("Please select an option.\n"
                           "(1) Show vehicles\n"
                           "(2) Edit vehicle\n"
                           "(3) Add vehicles\n"
                           "(q) Quit Program\n")

        if answer.lower() == "q":
            # todo: save cars list to file
            print "Exiting program..."
            break

        elif answer == "1":
            print "Showing all vehicles..."
            for vehicle in All_Vehicles:

                vehicle.show
                print vehicle.brand, vehicle.model, vehicle.km, vehicle.service_date

        elif answer == "3":
            print "Adding Vehicle..."
            brand = raw_input("Please add the brand of the new vehicle.")
            model = raw_input("Please enter the model of the new vehicle.")
            km = raw_input("Please enter the km driven by the new vehicle.")
            service_date = raw_input("Please enter the last service_date of the new vehicle.")
            my_vehicle = Vehicle(brand, model, km, service_date)
            All_Vehicles.append(my_vehicle)
            print "Vehicle added to list"
        else:
            print "Please check your input, and try again.\n"



