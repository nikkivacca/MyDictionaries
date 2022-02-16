
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