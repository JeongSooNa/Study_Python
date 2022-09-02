# Tug of War

## Needs Object
## 1. Number of people
## 2. People's strength
## 3. Strategy
## 4. People's willpower

import TugOfWar_score as ts

team1 = ts.tw(1,1,1,1)
team2 = ts.tw(2,1,1,1)

if team1 > team2 : 
    print("team1 win!")
if team1 < team2 :
    print("team2 win!")
if team1 == team2 :
    print("draw")