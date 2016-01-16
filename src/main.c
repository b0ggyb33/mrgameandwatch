#include <pebble.h>
#include <src/Actors.h>
#include "main.h"

#ifdef PBL_COLOR
  #define BACKGROUND_COLOUR GColorLimerick
#else
  #define BACKGROUND_COLOUR GColorWhite  
#endif

Window *my_window;
static GBitmap *s_background;
static GBitmap *s_mgw_left, *s_mgw_middle, *s_mgw_right;
static GBitmap *s_crash_left, *s_crash_right;

static BitmapLayer *s_background_layer;
static BitmapLayer *s_mgw_layer;
static Layer *s_ball_layer;
static BitmapLayer *s_crash_layer;
static MrGameAndWatch* mgw;

static TextLayer *scoreLayer;
static TextLayer *highScoreLayer;

static int8_t delay = 50;
static int updateSpeedFrequency=150; //controls 'difficulty'

static int8_t gameInPlay = 1;
static int game_time = 0;
static int score=0;
static int highScore=20;
static char scoreString[10];
static char highScoreString[10];
static int8_t speed=30;
static int8_t crash=0;
static int timeOfLastUpdate=0;
static int timeOfLastSpeedIncrease=0;

  
static Ball *ball0,*ball1,*ball2;

static uint8_t positions0x[8] = {51,56,60,68,77,85,88,93};
static uint8_t positions0y[8] = {128,101,81,61,61,81,101,128};
static uint8_t positions1x[10] = {41,42,48,55,68,78,86,94,98,102};
static uint8_t positions1y[10] = {128,103,76,53,43,43,53,76,103,128};
static uint8_t positions2x[12] = {32,32,36,42,53,66,77,88,98,105,110,113};
static uint8_t positions2y[12] = {128,100,78,54,35,28,28,35,54,78,100,128};




void renderBalls(Layer* layer,GContext* ctx)
{
  GPoint ball0position = GPoint(positions0x[ball0->position],
                                positions0y[ball0->position]);
  GPoint ball1position = GPoint(positions1x[ball1->position],
                                positions1y[ball1->position]);
  GPoint ball2position = GPoint(positions2x[ball2->position],
                                positions2y[ball2->position]);
  
  graphics_fill_circle(ctx, ball0position, 3);
  graphics_fill_circle(ctx, ball1position, 3);
  graphics_fill_circle(ctx, ball2position, 3);
  
}

void renderCrash(int8_t direction)
{
  if (direction == DIRECTION_RIGHT)
  {
    bitmap_layer_set_bitmap(s_crash_layer, s_crash_right);
  }
  if (direction == DIRECTION_LEFT)
  {
    bitmap_layer_set_bitmap(s_crash_layer, s_crash_left);
  }
}

void updateScore()
{
  score += 10;
  snprintf(scoreString, 10,"%d", score);
  text_layer_set_text(scoreLayer, scoreString);
  
  if (score>=highScore)
  {
    highScore=score;
    text_layer_set_text(highScoreLayer, scoreString);
  }
}

void collisionEvent(Ball* object)
{
  updateScore();
  changeDirection(object);
  object->hasBeenScored = 1;
}

void handleBallCollision(Ball* object)
{
  if (object->hasBeenScored == 0 && atLimit(object) == 1 )
  {
    switch(object->track)
    {
      case 0:
        if ( (mgw->position == mgw->lowerLimit && object->position == object->upperLimit)
          || (mgw->position == mgw->upperLimit && object->position == object->lowerLimit)
           )
        {
          collisionEvent(object);
        }
      break;
      
      case 1:
        if (mgw->position != mgw->lowerLimit && mgw->position != mgw->upperLimit)
        {
          collisionEvent(object);
        }
      break;
      
      case 2:
        if ( (mgw->position == mgw->upperLimit && object->position == object->upperLimit)
          || (mgw->position == mgw->lowerLimit && object->position == object->lowerLimit)
           )
        {
          collisionEvent(object);
        }
      break;
    }
  }
}

void triggerEndGame(Ball* object)
{
  
  crash=object->velocity;
  gameInPlay=0;
  persist_write_int(0, highScore);
  renderCrash(crash);
  
}

void updateWorld()
{
  if (!gameInPlay)
    return;
  
  //update time
  game_time += 1;
  
  //ignoring keypress as event driven
  
  //update ball updates
  if (game_time - timeOfLastUpdate >= speed)
  {
    update(ball0);
    update(ball1);
    update(ball2);
    layer_mark_dirty(s_ball_layer); //render changes
    
    timeOfLastUpdate = game_time;
  }
  
  //handle collisions
  handleBallCollision(ball0);
  handleBallCollision(ball1);
  handleBallCollision(ball2);
  
  //handle speed increases
  if ( (game_time - timeOfLastSpeedIncrease >= updateSpeedFrequency)  && speed >= 1 )
  {
    speed -= 1;
    timeOfLastSpeedIncrease = game_time;
  } 
  
  //handle game end
  if (!ball0->live)
  {
    triggerEndGame(ball0);
  }
  if (!ball1->live)
  {
    triggerEndGame(ball1);
  }
  if (!ball2->live)
  {
    triggerEndGame(ball2);
  }
  
  app_timer_register(delay, updateWorld, NULL); 
  
}

void render_MisterGameAndWatch(MrGameAndWatch* object)
{
  if (object->position==0)
  {
    bitmap_layer_set_bitmap(s_mgw_layer, s_mgw_left);
  }
  else if (object->position==1)
  {
    bitmap_layer_set_bitmap(s_mgw_layer, s_mgw_middle);
  }
  else if (object->position==2)
  {
    bitmap_layer_set_bitmap(s_mgw_layer, s_mgw_right);
  }
}

static void reset_game_handler(ClickRecognizerRef recognizer, void *context)
{
  if (!gameInPlay)
  {
    handle_deinit();
    
    gameInPlay = 1;
    game_time = 0;
    score=0;
    speed=30;
    crash=0;
    timeOfLastUpdate=0;
    timeOfLastSpeedIncrease=0;
    handle_init();
    updateWorld();
  }
}

static void up_click_handler(ClickRecognizerRef recognizer, void *context) 
{
  if (gameInPlay)
  {
    move_MisterGameAndWatch(mgw, DIRECTION_RIGHT);
    render_MisterGameAndWatch(mgw);
  }
}

static void down_click_handler(ClickRecognizerRef recognizer, void *context) 
{
  if (gameInPlay)
  {  
    move_MisterGameAndWatch(mgw, DIRECTION_LEFT);
    render_MisterGameAndWatch(mgw);
  }
}

static void click_config_provider(void *context) 
{
  // Register the ClickHandlers
  window_single_click_subscribe(BUTTON_ID_SELECT, up_click_handler);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_click_handler);
  //window_single_click_subscribe(BUTTON_ID_UP, reset_game_handler);
}

void handle_init(void) {
  my_window = window_create();

  if (persist_exists(0)) //persist 0 is key for high score
  {
    highScore = persist_read_int(0);
  }
  else
  {
    highScore=0;
  }
  
  
  //GRect windowBounds = GRect(0, 0, 144, 168);
  scoreLayer = text_layer_create(GRect(0,0,60,20));
  highScoreLayer = text_layer_create(GRect(144-30,0,30,20));  
  
  // Load the resource
  s_background = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_BG);
  s_mgw_left = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_LEFT);
  s_mgw_middle = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_MIDDLE);
  s_mgw_right = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_RIGHT);
  s_crash_left = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_CRASH_LEFT);
  s_crash_right = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_CRASH_RIGHT);
  
  // Create the BitmapLayer
  window_set_background_color(my_window,BACKGROUND_COLOUR);
  s_background_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
  s_ball_layer = layer_create(GRect(0, 0, 144, 168)); 
  s_mgw_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
  s_crash_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
    
  // Set the correct compositing mode
  bitmap_layer_set_compositing_mode(s_background_layer, GCompOpSet);
  bitmap_layer_set_compositing_mode(s_mgw_layer, GCompOpSet);
  bitmap_layer_set_compositing_mode(s_crash_layer, GCompOpSet);
  
  bitmap_layer_set_bitmap(s_background_layer, s_background);
  
  
  //set mgw based on keys TODO
  bitmap_layer_set_bitmap(s_mgw_layer, s_mgw_middle);
  
  text_layer_set_background_color(scoreLayer, GColorClear);
  text_layer_set_background_color(highScoreLayer, GColorClear);
  text_layer_set_text(scoreLayer, "0");
  snprintf(highScoreString, 10,"%d", highScore);
  text_layer_set_text(highScoreLayer, highScoreString);
  
  // Add to the Window
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_background_layer));
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_mgw_layer));
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_crash_layer));
  layer_add_child(window_get_root_layer(my_window), s_ball_layer);
  layer_add_child(window_get_root_layer(my_window), text_layer_get_layer(scoreLayer));
  layer_add_child(window_get_root_layer(my_window), text_layer_get_layer(highScoreLayer));
  layer_set_update_proc(s_ball_layer, renderBalls);

  
  window_stack_push(my_window, true);
  
  
  //initialise game objects
  mgw = malloc(sizeof(MrGameAndWatch));
  initialise_MisterGameAndWatch(mgw);
    
  ball0 = malloc(sizeof(Ball));
  ball1 = malloc(sizeof(Ball));
  ball2 = malloc(sizeof(Ball));
  
  initialise_Ball(ball0, (int8_t)0, (int8_t)7, DIRECTION_RIGHT, 0);
  initialise_Ball(ball1, (int8_t)0, (int8_t)9, DIRECTION_LEFT, 1);
  initialise_Ball(ball2, (int8_t)0, (int8_t)11, DIRECTION_RIGHT, 2);
  
  light_enable(true);
  
}

void handle_deinit(void) 
{
  window_destroy(my_window);
  gbitmap_destroy(s_background);
  gbitmap_destroy(s_mgw_middle);
  gbitmap_destroy(s_mgw_left);
  gbitmap_destroy(s_mgw_right);
  gbitmap_destroy(s_crash_left);
  gbitmap_destroy(s_crash_right);
  bitmap_layer_destroy(s_background_layer);
  bitmap_layer_destroy(s_mgw_layer);
  layer_destroy(s_ball_layer);
  bitmap_layer_destroy(s_crash_layer);
  text_layer_destroy(scoreLayer);
  text_layer_destroy(highScoreLayer);
    
  free(mgw);
  free(ball0);
  free(ball1);
  free(ball2);
  
  light_enable(false);
}

int main(void) 
{
  handle_init();
  window_set_click_config_provider(my_window, click_config_provider);
  app_timer_register(delay, updateWorld, NULL); 
  app_event_loop();
  handle_deinit();
}
