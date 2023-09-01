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

    def __init__(self, tickets_and_parking = 10, current_tickets = {}, ticket_price = 12):
        self.tickets_and_parking = tickets_and_parking
        self.ticket_price = ticket_price

# -----------------------------DRIVER-----------------------------------------------------------------------------------------------

    def driver(self):
        print(f"Garage ticket price is currently ${self.ticket_price} for all day")
        # setting a while loop so that this continues to run after each option
        while True:
            # the input asks for an option. this value will be used to determin which method is used. .lower() added so that even if user inputs a capital letter, it will still work
            enter_input = input("Garage Operator: Are you looking to [t]ake a ticket, [p]ay for parking, or [l]eave?:  ").lower()
            # if user inputs a "t" to take a ticket, use take_ticket method
            if enter_input in ('t'):
                self.take_ticket()
            # if user inputs a "p" to take a ticket, use pay_for_parking method
            elif enter_input in ('p'):
                self.pay_for_parking()
            # if user inputs a "l" to take a ticket, use leave_garage_method and then break out of loop
            elif enter_input in ('l'):
                break
            # if user inputs is not a "t", "p", or "l", this runs telling them to enter something we want
            else:
                print("Please enter a valid option")

# -----------------------------TAKING TICKET METHOD-----------------------------------------------------------------------------------------------

    def take_ticket(self):
        tickets_left = self.tickets_and_parking
        print(self.tickets_and_parking, "parking spaces available")
        if tickets_left > 0:
            self.tickets_and_parking -= 1
            print("Please grab your parking ticket")
            print(self.tickets_and_parking, "parking spaces remaining")
        else:
            print("No parking spaces available left")



# -----------------------------PAY FOR PARKING METHOD-----------------------------------------------------------------------------------------------

    def pay_for_parking(self):
        pay_input = input("Please enter your payment amount: ")



# -----------------------------LEAVE GARAGE METHOD-----------------------------------------------------------------------------------------------
    def leave_garage(self):
        pass


# -----------------------------MAKING INSTANCE/RUNNING-----------------------------------------------------------------------------------------------
my_garage = ParkingGarage()
my_garage.driver()