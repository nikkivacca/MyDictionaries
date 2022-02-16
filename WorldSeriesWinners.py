

def main():
    infile = open('WorldSeriesWinners.txt', 'r')
    champions, number = make_dictionary(infile)
    questions(champions, number)
      
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


def questions(champions, number):
    year = int(input('Enter a year to know which team won the World Series in the year:'))
    if year > 1902 and year < 2010 and year != 1904 and year != 1994:
        print(champions[year], 'won in the year', number[champions[year]], 'times')
    elif year == 1904:
        print('World Series not played in 1904')
    elif year == 1994:
        print('Word Series not played in 1994')

