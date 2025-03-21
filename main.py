import pandas as pd

df = pd.read_csv("hotels.csv", encoding="ISO-8859-1", dtype={"id": str})

df_cards = pd.read_csv("cards.csv", encoding="ISO-8859-1", dtype=str).to_dict(orient="records")

df_card_security = pd.read_csv("card_security.csv", encoding="ISO-8859-1", dtype=str)

class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.hotel_id, "price"].squeeze()

    def view(self):
        pass

    def book(self):
        """Book a hotel and change its availability status"""
        df.loc[df["id"] == self.hotel_id, "available"]  = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the desired hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else: 
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation.
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        Price per night: ${float(self.hotel.price)}
        Total: ${float(self.hotel.price) * nights}

        Enjoy your stay!!!
        """
        return content
    

class CreditCard:
    
    def __init__(self, number):

        self.number = number

    def validate(self, expiration, holder, cvc):
        
        card_data = {"number":self.number, "expiration": expiration, 
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else: 
            return False
        

class SecureCreditCard(CreditCard): # inheritance

    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if str(password) == str(given_password):
            return True
        else:
            return False

print(df)

hotel_ID: str = input("Enter the id of the hotel: ")

hotel = Hotel(hotel_ID)

if hotel.available():

    credit_card = SecureCreditCard(number="1234")

    if credit_card.validate(expiration="12/26", holder="ALBERT BRICK", cvc="123"):
        user_pass = input("Enter your password: ")
        if credit_card.authenticate(given_password=str(user_pass)):

            hotel.book()

            nights = int(input("How long would you like to stay(nights)? : "))
            name = input("What is your name? : ")

            ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(ticket.generate())
        else:
            print("Password incorrect.")
    else:
        print("Invalid card data.")

else:
    print("Hotel not avalable")


