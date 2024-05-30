import random

suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
cards = []
for suit in suits:
    for rank in ranks:
        cards.append([rank, suit])

def shuffle():
    random.shuffle(cards)
def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
        return cards_dealt

shuffle()
cards_dealt = deal(2)
cards = cards_dealt[0]
rank = cards[1]

if rank =="A":
    value = 11
elif rank == "j" or rank == "q" or rank == "k":
    value = 10  
else:
      value= rank
print(rank, value)      
print(cards_dealt)    
    

     