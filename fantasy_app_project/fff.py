import os
from datetime import datetime
import os
from .espn_api_submodule.espn_api.football.league import League

#load environment variables
LEAGUE_ID = os.getenv('LEAGUE_ID')
ESPN_S2 = os.getenv('ESPN_S2')
SWID = os.getenv('SWID')

def hello11():
    return "Hellllooooooo"

# retrieve football year
def get_year():
    currentMonth = datetime.now().month
    if currentMonth > 7:
        currentYear = datetime.now().year
    else:
        currentYear = datetime.now().year - 1
    return currentYear

# create league instance
league = League(
    league_id=LEAGUE_ID,
    year=2021,
    espn_s2=ESPN_S2,
    swid=SWID
    )

def current_week():
    return league.current_week

def get_current_matchups():
    matchups = league.box_scores(current_week())
    return matchups

def get_lineups():
    matchups = get_current_matchups()
    #for matchup in 
def get_team_list():
    teams = league.teams
    return teams
#print(get_team_list()[1].roster[1].projected_points)

'''
for matchup in get_current_matchups():
    print(matchup)
'''

#print(league.box_scores(8)[0].home_lineup[19].stats)


def get_highest(position, stat, currentweek=0):
    if currentweek > 0:
        matchups = league.box_scores(currentweek)
    else:
        matchups =  get_current_matchups()
        currentweek = current_week()
    player_dict = {}
    for matchup_index, matchup in enumerate(matchups):
        away = matchup.away_lineup
        home = matchup.home_lineup
    
        for player_index, player in enumerate(away):
            if player.slot_position in position:
                team = matchup.away_team.team_name
                if team in player_dict:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team]['player'].update({(player.name): player.stats[currentweek]['breakdown'][stat]})
                        else:
                            player_dict[team]['player'].update({(player.name): 0})
                    else:
                        player_dict[team]['player'].update({(player.name): 0})
                else:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team] = {'player': {(player.name): player.stats[currentweek]['breakdown'][stat]}}
                        else:
                            player_dict[team] = {'player': {(player.name): 0}}
                    else:
                        player_dict[team] = {'player': {(player.name): 0}}

        for player_index, player in enumerate(home):
            if player.slot_position in position:
                team = matchup.home_team.team_name
                if team in player_dict:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team]['player'].update({(player.name): player.stats[currentweek]['breakdown'][stat]})
                        else:
                            player_dict[team]['player'].update({(player.name): 0})
                    else:
                        player_dict[team]['player'].update({(player.name): 0})
                else:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team] = {'player': {(player.name): player.stats[currentweek]['breakdown'][stat]}}
                        else:
                            player_dict[team] = {'player': {(player.name): 0}}
                    else:
                        player_dict[team] = {'player': {(player.name): 0}}

    return player_dict

def get_most_position_points(position, currentweek=0):
    if currentweek > 0:
        matchups = league.box_scores(currentweek)
    else:
        matchups =  get_current_matchups()
        currentweek = current_week()
    player_dict = {}

    for matchup in matchups:
        away = matchup.away_lineup
        home = matchup.home_lineup
        for player in away:
            if player.slot_position in position:
                if matchup.away_team.team_name in player_dict:
                    player_dict[matchup.away_team.team_name]['player'].update({(player.name): player.points})
                else:
                    player_dict[matchup.away_team.team_name] = {'player': {(player.name): player.points}}
        for player in home:
            if player.slot_position in position:
                if matchup.home_team.team_name in player_dict:
                    player_dict[matchup.home_team.team_name]['player'].update({(player.name): player.points})
                else:
                    player_dict[matchup.home_team.team_name] = {'player': {(player.name): player.points}}

    return player_dict

dict1 = get_most_position_points(['QB'], 8)

def order_positions_by_points(player_dict):

    for team, info in player_dict.items():
        player_dict[team].update({'total' : round(sum(info['player'].values()), 2)})
    result = list(sorted(player_dict.items(), key=lambda x: x[1]['total'], reverse=True))

    return result