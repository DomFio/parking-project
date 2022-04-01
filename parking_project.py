from IPython.display import clear_output as clear

class Paid_parking:
    
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def take_ticket(self):
        if len(self.tickets) >= 1:
            ticket = self.tickets.pop(0)
            print(f"\nYour ticket number is {ticket}")
            self.parking_spaces.remove(ticket)
            self.currentTicket[ticket] = ''
        else:
            print("sorry garage is full")

    def payforParking(self):
        ticket_pay = input("What ticket number would you like to pay for?\n ")

        if ticket_pay.isnumeric():

            if self.currentTicket[int(ticket_pay)]:
                    print("Your ticket has been paid already. Just leave already...")
            else:
                payment = input("To pay for parking, type 'pay'\n ")
                if payment.lower() == 'pay':
                    self.currentTicket[int(ticket_pay)] = 'paid'
                    print(f"\nTicket {int(ticket_pay)} Has been paid for.")
                else:
                    if payment.lower() != 'pay':
                        print("invalid input. please type 'pay' ")
                        return self.payforParking()
        else:
            print('Invalid response')
            return self.payforParking()
    
    def leaveGarage(self):
        
        ticket_pay = int(input("insert ticket number\n "))
        if ticket_pay in self.currentTicket.keys() and self.currentTicket[ticket_pay] == 'paid':
            self.tickets.append(ticket_pay)
            print("Thank You! have a nice day! ")
            
        if self.currentTicket[ticket_pay] == '' and ticket_pay in self.currentTicket.keys():
            self.payforParking()     

        return self.currentTicket
              
    def run(self):
        while True:
            response = input("What would you like to do? (park, pay, leave, quit)\n ")
            clear()
            if response.lower() == 'quit':
                print("See you soon!")
                break

            elif response.lower() == 'park':
                self.take_ticket()
               
            elif response.lower() == 'pay':
                self.payforParking()
                            
            elif response.lower() == 'leave':
                self.leaveGarage()    
                
            else:
                print("Invalid response... pick from (park, pay, leave, quit) ")
        



parking = Paid_parking()
parking.run()