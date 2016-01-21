#include <pebble.h>
#include "JavascriptInterface.h"

void outbox_sent_callback(DictionaryIterator *iterator, void *context) 
{
  APP_LOG(APP_LOG_LEVEL_INFO, "Outbox send success!");
}

void outbox_failed_callback(DictionaryIterator *iterator, AppMessageResult reason, void *context) 
{
  APP_LOG(APP_LOG_LEVEL_ERROR, "Outbox send failed!");
}

void sendScore(int score)
{
  // Begin dictionary
  DictionaryIterator *iter;
  app_message_outbox_begin(&iter);
  
  // Add a key-value pair
  dict_write_uint8(iter, 0, score);

  // Send the message!
  app_message_outbox_send();
  
}

