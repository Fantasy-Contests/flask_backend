import os
from datetime import datetime
from dotenv import load_dotenv
from .espn_api_submodule.espn_api.football.league import League

#load environment variables
load_dotenv()
LEAGUE_ID = os.getenv('LEAGUE_ID')
ESPN_S2 = os.getenv('ESPN_S2')
SWID = os.getenv('SWID')

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