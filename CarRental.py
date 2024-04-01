from datetime import datetime

class CarRental:
    def __init__(self, stock):
        self.stock = stock
        
    def avail_cars(self):
        print(f"No of cars availbale is: {self.stock}")
    
    def rent_hourly(self, no_cars):
        return self.rent_cars(no_cars, "hourly")
    def rent_daily(self, no_cars):
        return self.rent_cars(no_cars, "daily")
    def rent_weekly(self, no_cars):
        return self.rent_cars(no_cars, "weekly")
    
    def rent_cars(self, no_cars ,rental_time):
        if no_cars > 0 and no_cars < self.stock:
            now = datetime.now()
            print( f"{no_cars} booked for time {rental_time} at {now}")
            self.stock = self.stock - no_cars
            return now
        else:
            print("Not enough Cars available")
            
    def return_car(self, rental_time , rental_mode ,no_cars):
        if rental_mode == "hourly":
            bill = self.cal_bill(rental_time, no_cars , 1)
        elif rental_mode == "daily":
            bill = self.cal_bill(rental_time, no_cars, 24)
        elif rental_mode == "weekly":
            bill = self.cal_bill(rental_time, no_cars, 24*7)
        else:
            return None
        
        self.stock = self.stock-no_cars
        return bill
    
    def cal_bill(self, start_time,no_cars,rental_period):
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds() /3600
        total_period = (total_time / rental_period)
        return(round(total_period*no_cars*50000 , 2 ))
            

        
class Customer:
    
    def __init__(self):
        self.car_rental = CarRental(50)
        
        
    def req_rental(self):
        self.car_rental.avail_cars()
        rent_choice = input("Rental choice: (hourly/daily/weekly)")
        no_cars = int(input("Enter no of cars:"))
        
        if rent_choice == "hourly":
            rent_time = self.car_rental.rent_hourly(no_cars)
        
        elif rent_choice == "daily":
            rent_time = self.car_rental.rent_daily(no_cars)
            
        elif rent_choice == "weekly":
            rent_time = self.car_rental.rent_weekly(no_cars)
            
        else:
            rent_time = None
                
        return rent_time, rent_choice , no_cars
    
    def return_rental(self, rental_time , rental_mode , no_cars ):
        bill = self.car_rental.return_car( rental_time,rental_mode,no_cars)
        if bill:
            print(f"Thank you for use of our service, your bill is {bill}")
        else:
            print("something went wrong.")
            
        
    