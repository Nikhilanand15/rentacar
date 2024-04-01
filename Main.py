from CarRental import CarRental
from CarRental import Customer

def main():
    customer = Customer()
    rental_time = None
    rental_mode = None
    no_cars = None
    while True:
        print("******* Car Rental Service *******")
        choice = input(" Enter 1 for rent, 2 for return, or 3 for exit")
        
        if choice == "1":
            rental_time, rental_mode, no_cars = customer.req_rental()
        elif choice == "2":
        
            if rental_time:
                customer.return_rental(rental_time, rental_mode, no_cars)
                rental_time = None
                rental_mode = None
                no_cars = None
            else:
                print(" Rent a car first")
        elif choice == "3":
            print("thank you")
            break
        else:
            print("Invalid option")
            
if __name__ == "__main__":
    main()