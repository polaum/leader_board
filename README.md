# Bouncing Crates Leaderboards API

Simple Api for the Bouncing Crates Mini Game


## API


**GET** `/getScore`


Get the top 10 leaderboard scores



**GET** `/isScoreEligible/<int:score>`

Check if a score is eligible for the top 10 list


**POST** `/addScore`

Body:
```
userName // String
score // Int 
itemsShot // Int
timePlayed // Float
```

