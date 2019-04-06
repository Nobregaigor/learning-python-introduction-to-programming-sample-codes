from pprint import pprint
import math

cards = list(range(1,14))

nb_cards = 13
points = []

min1 = 10
min2 = 5
max = 32

length = nb_cards - 3
sz1 = (max - min1)/length
sz2 = (max - min2)/(length+1)

curr_max = min1
curr_min = min2

cards_names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
combs = {}
pairs = {}

for i in range(nb_cards-2):
    # print("current card = " + str(i+1))
    # print("curr min 2 = " + str(curr_min))
    # print("curr max = " + str(curr_max))
    counter = i
    array = []
    card_points = []
    length = nb_cards - i - 2
    step = (curr_max - curr_min) / length
    val = curr_min
    card1 = cards_names[i]

    Aval = curr_max + 3

    for j in range(counter,nb_cards-1):
        card2 = cards_names[j]
        comb = card1 + '_' + card2
        comb2 = card2 + '_' + card1
        comb3 = 'A' + '_' + card2
        comb4 = card2 + '_' + 'A'


        card_points.append(round(val))
        combs[comb] = round(val)
        combs[comb2] = round(val)
        combs[comb3] = round(Aval)
        combs[comb4] = round(Aval)
        array.append(cards[counter+1])
        counter += 1
        val += step

    # print(array)
    # print(card_points)

    points.append(card_points)

    curr_max += sz1
    curr_min += sz2


min3 = min2 + 3

for i in range(nb_cards):
    card1 = cards_names[i]
    pair = card1 + '_' + card1
    val = round(4.75*math.exp(0.18 * (i+1)) + 6)
    combs[pair] = val
    print(val)


pprint(combs)
