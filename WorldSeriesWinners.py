

outfile = open('WorldSeriesWinners.txt')
year = 1903 
year_winner = []
team_wins = []

for game in outfile:
    x = x.strip('\n')
    if year != 1904 and year != 1994:
        year_winner[year] = x
        if x not in team_wins.keys():
            team_wins[x] = 1 
        else:
            team_wins[x] = team_wins[x] + 1 
    if year == 1903 or year == 1993:
        year = year + 2
    else: 
        year = year + 1 


input_year = int(input('Enter a year from 1903-2009: '))
if(input_year != 1904 and input_year != 1994) and input_year in year_winner.keys():
    print('The team that won the world series in [0] is the []'.format(input_year, year_winner[input_year]))
    print('They won the world series [0] times'.format(team_wins[year_winner[input_year]]))
elif input_year == 1904 or input_year ==1994:
    print('The world series was not played in the year [0]'.format(input_year))
else:
    print('Data for year [0] is not available in input file'. format(input_year))


outfile.close()