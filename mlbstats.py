import statsapi
import os 
# os.system("cls")
# stat = statsapi.get("team",{"teamId":137})
# stat = statsapi.get('schedule',{'sportId':1,'hydrate':'hydrations','fields':'hydrations'})
# name = stat["teams"][0]["name"]
def getGame():
	sched = statsapi.schedule(start_date='07/01/2018',end_date='07/31/2018',team=143,opponent=121)
	gameId = sched[0]["game_id"]
	scoredata = statsapi.boxscore_data(gameId)
	return scoredata


def getPlayer(playername):
	player = statsapi.lookup_player(playername,season = "2019")
	return player


def lookupid(teamname):
  team_id = statsapi.lookup_team(teamname)[0]["id"]
  return team_id

def getTeam(team_id):
  stat = statsapi.get("team",{"teamId":team_id}) # identify team throught teamId
  return stat

def get(endpoint,param):
	import ast
	param = ast.literal_eval(param.strip(" "))
	print(param)
	data = statsapi.get("team",param)

# # team = lookup_team("sf")
# # team_id = team[0]["id"]
# # game_id = next_game(team_id)
# # print(game_id)

# games=schedule(team = lookup_team(input("team name: "))[0]["id"],
#               start_date=input("start date (YYYY_MM_DD): "),
#               end_date=input("end date (YYYY_MM_DD): "))

# def simpleInfo(game_list):
#   """game_list is the json data from schedule function"""
#   stats2look4 = ["game_id","game_date","away_score","home_score","away_name","home_name"]

#   for game in game_list:
#     print("========================", game["game_date"], "===========================")

#     for stat in game:
#       if stat in stats2look4:
#         print(stat, ":", game[stat])
    
#     print("===========================================")

# def get_boxscore(game_list):
#   for game in game_list:
#     print(boxscore(game["game_id"]))

# get_boxscore(games)


# #main menu
# while 1:
#   team_name = input("Enter team name or help to list team: ")

#   if team_name=="help":
#     print("sf - San Francisco Giants \n la - Los Angeles Dodgers")
#   else:

#     try:
#       team = statsapi.lookup_team(team_name)
#       team_id = team[0]["id"]
#       # print(statsapi.team_leaders(team_id,"blownSaves",limit=10, season= 2019))
#     except IndexError:
#       print("Cannot find that team name")
#       continue
  

#   #stats look up menu
#   while 1:
#     stat = input("What kind of stats do you want to look up for this team, type help for a list of different stats you want to look up? [format: stat_name,season_year,limit]: ")
#     stat = stat.split(",")
#     if stat[0] == "help":
#       system("clear")
#       cat = statsapi.meta("leagueLeaderTypes")
#       for i in cat:
#         print(i["displayName"])
#       continue
    
#     try:
#       print(statsapi.team_leaders(team_id, stat[0], season = int(stat[1]),limit = int(stat[2])))

#     except ValueError:
#       print("That stat may not exist or is no longer working")
#       continue
    
#     input("press enter to continue")
#     system("clear")

  
