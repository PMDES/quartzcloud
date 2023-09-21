from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    def connect(self):
        # Perform any necessary connection setup here
        print("Connected")
        self.accept()

    def disconnect(self, close_code):
        # Perform any necessary cleanup here
        pass

    def receive(self, text_data):
        # Handle incoming WebSocket messages here
        pass
