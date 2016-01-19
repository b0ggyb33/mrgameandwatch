#include <pebble.h>
#include "Game.h"

void initialiseGameState(GameState* state)
{
  state->gameInPlay = 1;
  state->game_time = 0;
  state->score=0;
  state->speed=30;
  state->crash=0;
  state->timeOfLastUpdate=0;
  state->timeOfLastSpeedIncrease=0;
  state->delay = 50;
  state->updateSpeedFrequency=150; //controls 'difficulty'
  
  if (persist_exists(0)) //persist 0 is key for high score
  {
    state->highScore = persist_read_int(0);
  }
  else
  {
    state->highScore=0;
  }
  
}