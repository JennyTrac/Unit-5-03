# created by Jenny Trac
# created on Nov 13 2017
# program lets user play blackjack against the computer with a real deck of cards

import ui
from numpy import random


# constants and variables
user_card_counter = 2
deck_of_cards = ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks',
                 '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc',
                 '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd',
                 '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh']
#print(deck_of_cards)
user_total = 0
dealer_total = 0

def get_next_card():
    # generates next card randomly
    
    global deck_of_cards
    
    # choose card
    pick_card = random.randint(0, 52)
    new_card = deck_of_cards[pick_card]
    #print (new_card)
    
    # delete card from array
    deck_of_cards.remove(new_card)
    
    # return card value
    return new_card

def get_card_value(next_user_card):
    # converts card to a value
    
    if next_user_card == '1s':
        card_value = 1
    elif next_user_card == '2s':
        card_value = 2
    elif next_user_card == '3s':
        card_value = 3
    elif next_user_card == '4s':
        card_value = 4
    elif next_user_card == '5s':
        card_value = 5
    elif next_user_card == '6s':
        card_value = 6
    elif next_user_card == '7s':
        card_value = 7
    elif next_user_card == '8s':
        card_value = 8
    elif next_user_card == '9s':
        card_value = 9
    elif next_user_card == '10s':
        card_value = 10
    elif next_user_card == 'Js':
        card_value = 10
    elif next_user_card == 'Qs':
        card_value = 10
    elif next_user_card == 'Ks':
        card_value = 10
    elif next_user_card == '1c':
        card_value = 1
    elif next_user_card == '2c':
        card_value = 2
    elif next_user_card == '3c':
        card_value = 3
    elif next_user_card == '4c':
        card_value = 4
    elif next_user_card == '5c':
        card_value = 5
    elif next_user_card == '6c':
        card_value = 6
    elif next_user_card == '7c':
        card_value = 7
    elif next_user_card == '8c':
        card_value = 8
    elif next_user_card == '9c':
        card_value = 9
    elif next_user_card == '10c':
        card_value = 10
    elif next_user_card == 'Jc':
        card_value = 10
    elif next_user_card == 'Qc':
        card_value = 10
    elif next_user_card == 'Kc':
        card_value = 10
    elif next_user_card == '1d':
        card_value = 1
    elif next_user_card == '2d':
        card_value = 2
    elif next_user_card == '3d':
        card_value = 3
    elif next_user_card == '4d':
        card_value = 4
    elif next_user_card == '5d':
        card_value = 5
    elif next_user_card == '6d':
        card_value = 6
    elif next_user_card == '7d':
        card_value = 7
    elif next_user_card == '8d':
        card_value = 8
    elif next_user_card == '9d':
        card_value = 9
    elif next_user_card == '10d':
        card_value = 10
    elif next_user_card == 'Jd':
        card_value = 10
    elif next_user_card == 'Qd':
        card_value = 10
    elif next_user_card == 'Kd':
        card_value = 10
    elif next_user_card == '1h':
        card_value = 1
    elif next_user_card == '2h':
        card_value = 2
    elif next_user_card == '3h':
        card_value = 3
    elif next_user_card == '4h':
        card_value = 4
    elif next_user_card == '5h':
        card_value = 5
    elif next_user_card == '6h':
        card_value = 6
    elif next_user_card == '7h':
        card_value = 7
    elif next_user_card == '8h':
        card_value = 8
    elif next_user_card == '9h':
        card_value = 9
    elif next_user_card == '10h':
        card_value = 10
    elif next_user_card == 'Jh':
        card_value = 10
    elif next_user_card == 'Qh':
        card_value = 10
    elif next_user_card == 'Kh':
        card_value = 10
    
    return card_value
    
def show_card(the_card):
    # function to assign name for show card in GUI
    
    show_the_card = "Resources/" + str(the_card) + ".PNG"
    
    return show_the_card

def add_card_touch_up_inside(sender):
    # button to add card
    
    global user_card_counter
    global user_total
    new_card_value = 0
    
    # run get_next_card function and return next card
    new_user_card = get_next_card()
    #print("newcard: " + new_user_card)
    
    # get card value
    new_card_value = get_card_value(new_user_card)
    #print("newcardvalue: " + str(new_card_value))
    
    # add card to total
    user_total = user_total + new_card_value
    #print "user total: " + str(user_total)
    view['usertotal_label'].text = "Total: " + str(user_total)
    
    # show next card
    user_card_counter = user_card_counter + 1
    if user_card_counter <= 5:
        #print("cardcount: " + str(user_card_counter))
        if user_card_counter == 3:
            show_user_card3 = show_card(new_user_card)
            view['showusercard3_imageview'].image = ui.Image(show_user_card3)
        elif user_card_counter == 4:
            show_user_card4 = show_card(new_user_card)
            view['showusercard4_imageview'].image = ui.Image(show_user_card4)
        elif user_card_counter == 5:
            show_user_card5 = show_card(new_user_card)
            view['showusercard5_imageview'].image = ui.Image(show_user_card5)
    
        # disable add card button only after third click
        view['addcard_button'].enabled = True
    else:
        view['addcard_button'].enabled = False

def check_cards_touch_up_inside(sender):
    # button to check cards
    global user_total
    global dealer_total
    global dealer_card1
    global dealer_card2
    global dealer_card3
    global show_dealer_card1
    global show_dealer_card2
    global show_dealer_card3
    
    # show all dealers cards
    show_dealer_card1 = show_card(dealer_card1)
    show_dealer_card2 = show_card(dealer_card2)
    show_dealer_card3 = show_card(dealer_card3)
    view['showdealercard1_imageview'].image = ui.Image(show_dealer_card1)
    view['showdealercard2_imageview'].image = ui.Image(show_dealer_card2)
    view['showdealercard3_imageview'].image = ui.Image(show_dealer_card3)
    
    # show dealers total
    view['dealertotal_label'].text = "Total: " + str(dealer_total)
    
    if (user_total > 21 and dealer_total > 21) or (user_total == dealer_total):
        view['winner_label'].text = "You tied."
        
    elif (dealer_total <= 21 and user_total > 21) or (user_total < dealer_total and dealer_total <= 21):
        view['winner_label'].text = "You lose."
    
    else:
        view['winner_label'].text = "You win."
    
    # disable button
    view['addcard_button'].enabled = False
    view['checkcards_button'].enabled = False

view = ui.load_view()
view.present('sheet')

# get user and dealers starting cards
dealer_card1 = get_next_card()
dealer_card1_value = get_card_value(dealer_card1)
dealer_card2 = get_next_card()
dealer_card2_value = get_card_value(dealer_card2)
dealer_card3 = get_next_card()
dealer_card3_value = get_card_value(dealer_card3)
dealer_total = dealer_total + dealer_card1_value + dealer_card2_value + dealer_card3_value
user_card1 = get_next_card()
user_card1_value = get_card_value(user_card1)
user_card2 = get_next_card()
user_card2_value = get_card_value(user_card2)
user_total = user_total + user_card1_value + user_card2_value
view['usertotal_label'].text = "Total: " + str(user_total)
#print("card1:" + user_card1)
#print("card1value: " + str(user_card1_value))
#print("card2: "+ user_card2)
#print("card2value: " + str(user_card2_value))
#print ("usertotal:" + str(user_total))
#print("dc1: " + dealer_card1)
#print("dc2: " + dealer_card2)
#print("dc3: " + dealer_card3)
#print("dtotal: " + str(dealer_total))

# show cards
back_of_card = "Resources/cardback.PNG"
show_dealer_card1 = back_of_card
show_dealer_card2 = back_of_card
show_dealer_card3 = back_of_card

show_user_card1 = show_card(user_card1)
show_user_card2 = show_card(user_card2)

view['showdealercard1_imageview'].image = ui.Image(show_dealer_card1)
view['showdealercard2_imageview'].image = ui.Image(show_dealer_card2)
view['showdealercard3_imageview'].image = ui.Image(show_dealer_card3)
view['showusercard1_imageview'].image = ui.Image(show_user_card1)
view['showusercard2_imageview'].image = ui.Image(show_user_card2)
