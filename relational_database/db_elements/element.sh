#!/bin/bash

PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

if [[ $1 ]]
then
  ELEMENT=$1
  ATOMIC_NUMBER=20
  # if input is a number
  if [[ $ELEMENT =~ ^[0-9]+$ ]]
  then
    ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE atomic_number = $ELEMENT;")
  else
    # if input is a two letter long
    if [[ $ELEMENT =~ ^[a-zA-Z]{1,2}$ ]]
    then
      ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE symbol = '$ELEMENT';")
    else
      ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE name = '$ELEMENT';")
    fi
  fi

  if [[ -z $ATOMIC_NUMBER ]]
  then
    echo -e "I could not find that element in the database."
  else
    ELEMENT_INFO=$($PSQL "SELECT atomic_number, name, symbol, type, atomic_mass,
                              melting_point_celsius, boiling_point_celsius
                          FROM properties
                            INNER JOIN elements USING(atomic_number)
                            INNER JOIN types USING(type_id)
                          WHERE atomic_number = $ATOMIC_NUMBER;")
                          
    echo "$ELEMENT_INFO" | while read AT_NUMBER BAR ELEMENT_NAME BAR ELEMENT_SYMBOL BAR ELEMENT_TYPE BAR ELEMENT_MASS BAR MELTING_POINT BAR BOILING_POINT
    do
       echo "The element with atomic number $AT_NUMBER is $ELEMENT_NAME ($ELEMENT_SYMBOL). It's a $ELEMENT_TYPE, with a mass of $ELEMENT_MASS amu. $ELEMENT_NAME has a melting point of $MELTING_POINT celsius and a boiling point of $BOILING_POINT celsius."
    done

  fi

else
  echo "Please provide an element as an argument."
fi
