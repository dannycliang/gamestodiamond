# An API that allows me to query a user's gameplay data
from riotwatcher import RiotWatcher

# My API key
w = RiotWatcher("RGAPI-c7263f5c-424f-4c7d-9e8f-321db7bd5185")



""" Function that queries the RiotWatcher API for the relevant details of the user based on its username. Parses and cleans the response and returns it for use"""
def get_info(username):
    try:
        user = w.get_summoner(name=username)
        my_ranked_stats = w.get_league_entry([user['id']])
        for stat in my_ranked_stats:
            rank = my_ranked_stats[stat][0][u'tier'][:1] + my_ranked_stats[stat][0][u'tier'][1:].lower()
            division = my_ranked_stats[stat][0][u'entries'][0][u'division']
            LP = my_ranked_stats[stat][0][u'entries'][0][u'leaguePoints']
            winrate = round((my_ranked_stats[stat][0][u'entries'][0][u'wins'] * 100 + 0.0)/ (my_ranked_stats[stat][0][u'entries'][0][u'wins'] + my_ranked_stats[stat][0][u'entries'][0][u'losses']), 2)
            result = [rank + " " + division, LP, winrate, 20 + (winrate - 50) / 2]
        return result
    except:
        return ["No summoner by that name"]
