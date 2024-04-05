#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

# Clean tables
echo $($PSQL "TRUNCATE TABLE games, teams;")

cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT W_GOALS O_GOALS
do
  if [[ $YEAR != "year" ]]
  then
    # get winner ID
    WINNER_ID=$($PSQL "SELECT team_id  FROM teams WHERE name = '$WINNER'")
    # if not found
    if [[ -z $WINNER_ID ]]
    then
      # insert team
      INSERT_WINNER_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$WINNER')")
      if [[ $INSERT_WINNER_RESULT == "INSERT 0 1" ]]
      then
        echo Inserted into teams, $WINNER
      fi
    fi

    # get opponent ID
    OPPONENT_ID=$($PSQL "SELECT team_id  FROM teams WHERE name = '$OPPONENT'")
    # if not found
    if [[ -z $OPPONENT_ID ]]
    then
      # insert team
      INSERT_OPPONENT_RESULT=$($PSQL "INSERT INTO teams(name) VALUES ('$OPPONENT')")
      if [[ $INSERT_OPPONENT_RESULT == "INSERT 0 1" ]]
      then
        echo Inserted into teams, $OPPONENT
      fi
    fi

    # get winner ID
    WINNER_ID=$($PSQL "SELECT team_id  FROM teams WHERE name = '$WINNER'")
    # get opponent ID
    OPPONENT_ID=$($PSQL "SELECT team_id  FROM teams WHERE name = '$OPPONENT'")

    INSERT_GAME_RESULT=$($PSQL "  INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals)
                                  VALUES ($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $W_GOALS, $O_GOALS);")
    if [[ $INSERT_GAME_RESULT == "INSERT 0 1" ]]
    then
      echo Inserted into games, $YEAR - $ROUND
    fi
  fi
done