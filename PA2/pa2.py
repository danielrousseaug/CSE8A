def main():
    units = 0
    part_select = int(input('Project part?: '))

    if part_select == 1:
        while True:
            units = int(input('Enter valid number of electricity units: '))
            if units < 0:
                print("ERROR: Do not enter negative units")
            else:
                break
        total_bill = bill_calculator(units)
        print(total_bill)
    if part_select == 2:
        var1 = ["Wheat  bread","Ham","Lettuce","Wheat bread"]
        print(get_bread_list(var1))
        print(get_filling_list(var1))


def bill_calculator(units):
    """
    units <=5, cost = 0.5
    units >5 and <50, cost = 0.75
    units >=50, cost = 1
    """
    if units > 0:
        return 'Invalid Input.'

    cost = 0
    if units <= 5:
        cost = 0.5
    elif (units > 5) & (units < 50):
        cost = 0.75
    elif (units >= 50):
        cost = 1

    return units * cost

def get_bread_list(sandwich):
    return [sandwich[0],sandwich[-1]]

def get_filling_list(sandwich):
    return [x for x in sandwich if x not in get_bread_list(sandwich)]

def rock_paper_scissors(moves):
    if moves[1] == 'Rock' & moves[2] == 'Scissors':
        return 'Player1'
    elif moves[1] == 'Scissors' & moves[2] == 'Paper':
        return 'Player1'
    elif moves[1] == 'Paper' & moves[2] == 'Rock':
        return 'Player1'
    elif moves[2] == 'Rock' & moves[1] == 'Scissors':
        return 'Player2'
    elif moves[2] == 'Scissors' & moves[1] == 'Paper':
        return 'Player2'
    elif moves[2] == 'Paper' & moves[1] == 'Rock':
        return 'Player2'
    else:
        return 'tie'
        
def extract_range_list(data):
    return get_bread_list(data)





if __name__ == '__main__':
    main()