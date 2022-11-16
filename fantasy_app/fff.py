import os
from datetime import datetime
from dotenv import load_dotenv
from .espn_api_submodule.espn_api.football.league import League

#load environment variables
#load_dotenv()
#LEAGUE_ID = os.getenv('LEAGUE_ID')
#ESPN_S2 = os.getenv('ESPN_S2')
#SWID = os.getenv('SWID')
LEAGUE_ID = 69192084
ESPN_S2 = 'AECtBC8t2p%2F1HWtD9xwcZTJbKZnmIy2jPmG6JJMKDE7WjJ0YmGBLZG7i%2FOkb5aGb%2F%2BpKL%2Bxe33dXnl%2F6MDJwDbrD2thKx0SwXDB2wRJF%2F0oompDwq04%2BoR9qoX0777%2Bksnn2Hr55WelNUxLArj4Ea2XCCDCTO4S%2BgW147eUAqFSf28q93COtLYtnFk1uxKRkm2awp2ZxVycaBI2TMGeC1UNYUoP2wJBw%2F9s%2F2BPJKUC6hz8NtlXO2lSauKcY4cGxfSHfrfnOf0kgfJIJephWMeXYox9Hb7e7MRmd1TwLuL%2FP2w%3D%3D'
SWID = '{832BF702-905D-40ED-ABF7-02905D90EDB1}'

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
    year=get_year(),
    espn_s2=ESPN_S2,
    swid=SWID
    )

def current_week():
    return league.current_week