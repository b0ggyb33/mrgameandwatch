#include <pebble.h>
#include <src/Actors.h>

Window *my_window;
static GBitmap *s_background;
static GBitmap *s_mgw_left, *s_mgw_middle, *s_mgw_right;

//static int currentPosition=1;
static BitmapLayer *s_background_layer;
static BitmapLayer *s_mgw_layer;
static MrGameAndWatch* mgw;

static int game_time = 0;
static int score=0;
static int8_t speed=30;
static int8_t crash=0;
static int timeOfLastUpdate=0;
static int8_t updateSpeedFrequency=200; //controls 'difficulty'
  
static Ball *ball0,*ball1,*ball2;



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

static void up_click_handler(ClickRecognizerRef recognizer, void *context) 
{
  move_MisterGameAndWatch(mgw, DIRECTION_RIGHT);
  render_MisterGameAndWatch(mgw);  
}

static void down_click_handler(ClickRecognizerRef recognizer, void *context) 
{
  move_MisterGameAndWatch(mgw, DIRECTION_LEFT);
  render_MisterGameAndWatch(mgw);
}

static void click_config_provider(void *context) 
{
  // Register the ClickHandlers
  window_single_click_subscribe(BUTTON_ID_UP, up_click_handler);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_click_handler);
}

void handle_init(void) {
  my_window = window_create();

  //GRect windowBounds = GRect(0, 0, 144, 168);
  
  // Load the resource
  s_background = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_BG);
  s_mgw_left = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_LEFT);
  s_mgw_middle = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_MIDDLE);
  s_mgw_right = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_MGW_RIGHT);
  
  // Create the BitmapLayer
  window_set_background_color(my_window,GColorLimerick);
  s_background_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
  s_mgw_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
  
  // Set the correct compositing mode
  bitmap_layer_set_compositing_mode(s_background_layer, GCompOpSet);
  bitmap_layer_set_compositing_mode(s_mgw_layer, GCompOpSet);
  
  bitmap_layer_set_bitmap(s_background_layer, s_background);
  
  
  //set mgw based on keys TODO
  bitmap_layer_set_bitmap(s_mgw_layer, s_mgw_middle);
   
  
  // Add to the Window
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_background_layer));
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_mgw_layer));

  
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
  
}

void handle_deinit(void) {
  window_destroy(my_window);
  gbitmap_destroy(s_background);
  gbitmap_destroy(s_mgw_middle);
  gbitmap_destroy(s_mgw_left);
  gbitmap_destroy(s_mgw_right);
  bitmap_layer_destroy(s_background_layer);
  bitmap_layer_destroy(s_mgw_layer);
  
  free(mgw);
  free(ball0);
  free(ball1);
  free(ball2);
}

int main(void) 
{
  handle_init();
  window_set_click_config_provider(my_window, click_config_provider);
  app_event_loop();
  handle_deinit();
}
