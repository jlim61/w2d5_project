# Brainstorm

# create ticket system:

# take ticket
#  allows user to pull from tickets
#  limited tickets
#  each time ticket pulled, parking spaces + tickets decreases

# pay for parking
#  ask for a payment amount (input function)
#  if payment variable is not empty, message - ticket has been paid and 15 min to leave
#  create list for tickets, list for parking spaces, current list should be dictionary
#  update current dicionary when a ticket has been paid. key value = paid, set it to True

class ParkingGarage:

    def __init__(self, tickets = [10], parking_spaces = [10], ticket_price = 12):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_tickets = {'ticket': 0}
        self.garage_status = True
        self.ticket_price = ticket_price    
# -----------------------------DRIVER-----------------------------------------------------------------------------------------------


    def driver(self):
        print(f"Garage ticket price is currently ${self.ticket_price} for all day")
        # setting a while loop so that this continues to run after each option
        while self.garage_status is True:
            # the input asks for an option. this value will be used to determin which method is used. .lower() added so that even if user inputs a capital letter, it will still work
            enter_input = input("Garage Operator: Are you looking to [t]ake a ticket, [p]ay for parking, or [l]eave?:  ").lower()
            # if user inputs a "t" to take a ticket, use take_ticket method
            if enter_input in ('t','take'):
                self.take_ticket()
            # if user inputs a "p" to take a ticket, use pay_for_parking method
            elif enter_input in ('p','pay'):
                self.pay_for_parking()
            # if user inputs a "l" to take a ticket, use leave_garage_method and then break out of loop
            elif enter_input in ('l','leave'):
                self.leave_garage()               
            # if user inputs is not a "t", "p", or "l", this runs telling them to enter something we want
            else:
                print("Please enter a valid option")

# -----------------------------TAKING TICKET METHOD-----------------------------------------------------------------------------------------------

    def take_ticket(self):
        tickets = self.tickets
        print(self.parking_spaces[-1], "parking spaces available")
        if tickets[-1] > 0:
            self.current_tickets['ticket'] += 1
            self.tickets[-1] -= 1
            self.parking_spaces[-1] -= 1
            print(f"Please grab your parking ticket\nYour ticket count is: {self.current_tickets['ticket']}")
            print(self.parking_spaces[-1], "parking spaces remaining")
        else:
            print("No parking spaces available left")



# -----------------------------PAY FOR PARKING METHOD-----------------------------------------------------------------------------------------------

    def pay_for_parking(self):
        if self.current_tickets['ticket'] > 0:
            while True:

                pay_input = input("Please enter your payment amount: ")
                if pay_input.isdigit():
                    self.current_tickets['ticket'] -= 1
                    self.tickets[-1] += 1
                    self.parking_spaces[-1] += 1
                    print(f"Thank you for your payment of ${pay_input}! You have 15 minutes to leave garage.")
                    break
                else:
                    print("Invalid Amount\nPlease Enter Valid amount: EX 12")
        else:
            print("No tickets to pay for.")


# -----------------------------LEAVE GARAGE METHOD-----------------------------------------------------------------------------------------------
    def leave_garage(self):
        if self.current_tickets['ticket'] > 0:
            print(f"You still have {self.current_tickets['ticket']} ticket(s) to pay for.")
        else:
            print(f"Thank you have a nice day!")
            self.garage_status is False
            
       


# -----------------------------MAKING INSTANCE/RUNNING-----------------------------------------------------------------------------------------------
my_garage = ParkingGarage()
my_garage.driver()