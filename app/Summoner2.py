from riotwatcher import RiotWatcher

w = RiotWatcher('RGAPI-559eb27c-ba76-41f4-9bfc-1b85e2d90d1b')




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
        for item in result:
            print(item)
        return result
    except:
        return ["No summoner by that name"]
