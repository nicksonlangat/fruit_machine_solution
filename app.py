import random

def check_colors(selected_colors):
    has_won = True
    for random_color in selected_colors:
        if random_color != selected_colors[0]:
            has_won = False
    return has_won

def check_adjacent_slots(random_colors):
    has_won = False
    index = 1
    while index < len(random_colors):
        if random_colors[index] == random_colors[index - 1]:
            has_won = True
            break
        else:
            index += 1
    return has_won

def virtual_fruit_machine():
    start = input('Enter play or quit: ')
    
    if start.lower() == 'play':
        available_balance = 2000

        colors = ['black', 'white', 'green', 'yellow']

        random_colors = []

        for i in range(len(colors)):
            random_color = random.choice(colors)
            random_colors.append(random_color)

        print([random_color for random_color in random_colors])

        #check if user has won the JP
        check = check_colors(random_colors)

        #let's check if two or more ADJACENTR slots contain same color
        check_adjacent = check_adjacent_slots(random_colors)

        if check:
            print(f'You won the jackpot of KES {available_balance}')
        elif check_adjacent:
            print(f'Similar adjacent colors found! You won KES {available_balance * 5}')
        else:
            #each slot has a different colour then the machine should pay out half the current money in the machine
            payout = available_balance/2
            print(f'Slots did not match. Payout is {payout}')
    else:
        print('Thanks for stopping by.')


if __name__ == '__main__':
    virtual_fruit_machine()









