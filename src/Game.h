#include <pebble.h>
#pragma once


typedef struct
{
  int8_t gameInPlay;
  int game_time;
  int score;
  int highScore;
  int8_t speed;
  int8_t crash;
  int timeOfLastUpdate;
  int timeOfLastSpeedIncrease;
  int8_t delay;
  int updateSpeedFrequency; //controls 'difficulty'
  
}GameState;

void initialiseGameState(GameState* state);