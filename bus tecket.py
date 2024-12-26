
def display_routes():
    print('\n 1. Dhaka to Khulna 600bdt') 
    print('\n 2. Dhaka to Chittagong 800bdt') 
    print('\n 3. Dhaka to Sylet 2000bdt')

def calculate_fare(route,tickets):
    fare_per_ticket={1:600,2:800,3:2000}
    return fare_per_ticket.get(route,0)*tickets
def book_tickets():
    display_routes()
    try:
        route=int(input("\nEnter the route number (1-3: )"))
        if route not in [1,2,3]:
            print("Invalid route selected.Please try again")
            return
        tickets=int(input("Enter the number of tickets:"))
        if tickets<=0:
            print("Numbers of tickets must be greater than zero")
            return
        total_fare=calculate_fare(route,tickets)
        print (f"\nBooking confirmed!!! Total fare: {total_fare}")
        print(" Thank you for booking with us ")
    except ValueError:
        print("Invalid input. Enter numbers only")
book_tickets()