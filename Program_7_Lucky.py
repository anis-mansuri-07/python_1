#Program 7
#To read a card as input and output if the card is lucky or not
Lucky_cards = ["HEART ACE","SPADE ACE","CLUB ACE","DIAMOND ACE"]
Card_in = input("eg:- Heart King\nEnter the card name ::").upper();
for i in Lucky_cards:
    if (i == Card_in):
         print("Card is lucky...")
         break
else:
    print("Card is not lucky..")
    