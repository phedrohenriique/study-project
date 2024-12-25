def tournamentWinner(competitions, results):
    # Write your code here.
    # always winner and loser no ties
    # always home team and away team
    # 1 home team won and 0 away team won
    # [ hometeam, awayteam]
    # use graphs bfs or dfs
    winner_hash = {}
    points = 0
    winner = ''
    for c, r in zip(competitions, results):
        # print(f'competitors:{c} and results:{r}')
        
        if r == 1:
            winner = c[0]
            winner_hash[winner] = winner_hash.get(winner,0) + 3
            
        elif r ==0:
            winner = c[1]
            winner_hash[winner] = winner_hash.get(winner,0) + 3
        
    for w, p in winner_hash.items():
        
        if p > points:
            winner = w
            points = p
        
    return winner