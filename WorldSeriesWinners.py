
def main():
    infile = open('WorldSeriesWinners.txt', 'r')
    winner = infile.readlines()
    infile.close()
    team =input('Enter the name of the team: ')
    counter = 0 
    
    for team in winner:
        if team == winner:
            result  = counter + 1

            if result == 1:
                print('The', team, "won the world series", result, "times between 1903 and 2009")
            elif result > 1:
                print('The', team, "won the world series", result, "times between 1903 and 2009")
            else:
                print('The', team, 'never won the world series')

main() 

def make_dictionary(infile):
    champions = []
    line = infile.readline().rstrip('\n')

    for i in range(1903,2008):
        champions[i] = line 
        line = infile.readline().rstrip('\n')
    
    print(champions, '\n')

    number = []
    for i in range (1903,2008):
        team = champions[i]
        if not team in number:
            number[team] =1 
        else: 
            number[team] += 1
    
    print(number, '\n')
    return champions, number