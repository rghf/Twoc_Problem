p1,p2,p3=list(map(int,input("Enter runs scored by 3 players in 60 balls").split()))
s1 = p1 * 100 / 60
s2 = p2 * 100 / 60
s3 = p3 * 100 / 60
print("\nStrike rate of player1 is:",s1,"\nStrike rate of player2 is:",s2,"\nStrike rate of player3 is:",s3)
print("\nAfter playing 60 more balls")
print("\nRuns scored by player 1", p1 * 2,"\nRuns scored by player 2", p2 * 2,"\nRuns scored by player 3", p3 * 2)
print("\nMaximum number of sixes")
print("\nPlayer 1 could hit =", p1 // 6,"\nPlayer 2 could hit =", p1 // 6,"\nPlayer 3 could hit =", p3 // 6)
