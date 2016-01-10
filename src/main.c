#include <pebble.h>

Window *my_window;
static GBitmap *s_bitmap;
static BitmapLayer *s_bitmap_layer;

void handle_init(void) {
  my_window = window_create();

  GRect windowBounds = GRect(0, 0, 144, 168);
  
  // Load the resource
  s_bitmap = gbitmap_create_with_resource(RESOURCE_ID_IMAGE_BG);

  // Create the BitmapLayer
  window_set_background_color(my_window,GColorLimerick);
  s_bitmap_layer = bitmap_layer_create(GRect(0, 168-51, 144, 51));
  // Set the correct compositing mode
  bitmap_layer_set_compositing_mode(s_bitmap_layer, GCompOpSet);
  
  bitmap_layer_set_bitmap(s_bitmap_layer, s_bitmap);

  // Add to the Window
  layer_add_child(window_get_root_layer(my_window), bitmap_layer_get_layer(s_bitmap_layer));

  
  window_stack_push(my_window, true);
}

void handle_deinit(void) {
  window_destroy(my_window);
  gbitmap_destroy(s_bitmap);
  bitmap_layer_destroy(s_bitmap_layer);
}

int main(void) {
  handle_init();
  app_event_loop();
  handle_deinit();
}
