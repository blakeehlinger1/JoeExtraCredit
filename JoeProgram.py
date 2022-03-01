import CustomerClass as C
import CarClass as Ca
import ServiceQuote as S

def main():
    name = "Blake"
    address = "101 Ball St"
    phone = "832-555-1234"

    custom = C.Customer(name, address, phone)
    
    print("Name:", custom.get_name())
    print("Address:", custom.get_address())
    print("Phone:", custom.get_phone())

    custom.set_name("Blake")
    custom.set_address("101 Ball St")
    custom.set_phone("832-555-1234") 

    cars = Ca.Car("BMW","X5", "2021")
    print("Make:", cars.get_make())
    print("Model:", cars.get_model())
    print("Year:", cars.get_year())

    tires = S.Service(200,80)

    print("Parts Charge:", format(tires.get_parts_charges(), ',.2f'))
    print("Labor Charge:", format(tires.get_labor_charges(), ',.2f'))
    print("Sales Tax:", format(tires.get_sales_tax(), ',.2f'))
    print("Total:", format(tires.get_total_charges(), ',.2f'))


main()
