from channels.consumer import SyncConsumer
 
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": "Hello I got your messgae",
        })
    
    def websocket_disconnect(self, event):
        print("WebSocket disconnected")