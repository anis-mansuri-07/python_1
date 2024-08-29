# Progran 1
# A card drawn at random from a deck of well suffeled cards. Find the probability of it being neither a king nor a spade.


Total_cards = 52                   # total cards in deck
black_cards = 13                   # Number of spade card in deck
Total_king = 4                     # Number of king's in deck
Black_king = 1                       # Number of spade card in deck which we have to remove

Prob = (Total_cards - ( Total_king + black_cards - Black_king))/Total_cards  #Formula
print("Probability of it being neither a king nor a spade is {:.2f}%".format(Prob))