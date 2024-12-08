import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f' your cards:{user_card},your score:{user_score}')
    print(f' computers first card:{computer_card[0]}')

    if user_score == 0 or computer_score == 0 or user_score>21:
        is_game_over = True
    else:
        user_should_deal = input("type 'y' to get another card,type 'n' to pass: ")
        if user_should_deal == 'y':
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score<17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)
    
def compare(user_score,computer_score):
    if user_score == computer_score:
        return 'draw'
    elif computer_score == 0:
        return 'you lose'
    elif user_score == 0:
        return 'you won'
    elif user_score > 21:
        return 'over ride,you lose'
    elif computer_score > 21:
        return 'over ride,you won'
    elif user_score>computer_score:
        return 'you won'
    else:
        return 'you lose'

print(f' your final hand:{user_card},your final score:{user_score} ')
print(f' computer final hand:{computer_card},computer final score:{computer_score} ')
print(compare(user_score,computer_score))
