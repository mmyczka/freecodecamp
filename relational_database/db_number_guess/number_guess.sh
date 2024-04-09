#!/bin/bash
PSQL="psql -X --username=freecodecamp --dbname=number_guess --tuples-only -c"

RANDOM_NUMBER=$((1 + RANDOM % 1000))
ATTEMPTS_COUNT=0


START_GAME(){
echo "Enter your username:"
read USERNAME

# get name of username from players
PLAYER_ID=$($PSQL "SELECT player_id FROM players WHERE name = '$USERNAME'")
if [[ -z $PLAYER_ID ]]
then
  echo -e "\nWelcome, $USERNAME! It looks like this is your first time here."
  INSERT_PLAYER_RESULT=$($PSQL "INSERT INTO players(name) VALUES ('$USERNAME');")
  PLAYER_ID=$($PSQL "SELECT player_id FROM players WHERE name = '$USERNAME'")
else
  PLAYER_STATS=$($PSQL "SELECT COUNT(game_id), MIN(guesses_number)
                        FROM games
                          INNER JOIN players USING (player_id)
                        WHERE player_id=$PLAYER_ID;")
  echo "$PLAYER_STATS" | while read GAME_COUNT BAR GAME_MIN
  do
    echo -e "\nWelcome back, $USERNAME! You have played $GAME_COUNT games, and your best game took $GAME_MIN guesses."
  done
fi

echo -e "\nGuess the secret number between 1 and 1000:"
NEXT_GUESS
}


NEXT_GUESS() {
read GUESS_ATTEMPT
((ATTEMPTS_COUNT++))

if [[ ! $GUESS_ATTEMPT =~ ^[0-9]+$ ]]
then
  echo -e "\nThat is not an integer, guess again:"
  NEXT_GUESS
else
  if (( GUESS_ATTEMPT > RANDOM_NUMBER ))
  then
    echo -e "\nIt's lower than that, guess again:"
    NEXT_GUESS
  elif (( GUESS_ATTEMPT < RANDOM_NUMBER ))
    then
    echo -e "\nIt's higher than that, guess again:"
    NEXT_GUESS
  else
    echo -e "You guessed it in $ATTEMPTS_COUNT tries. The secret number was $GUESS_ATTEMPT. Nice job!"
    INSERT_GAME_RESULT=$($PSQL "INSERT INTO games(guesses_number, player_id) VALUES ($ATTEMPTS_COUNT, $PLAYER_ID);")
  fi
fi
}


START_GAME