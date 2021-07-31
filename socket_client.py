from socketio import Client

socket = Client(logger=True, engineio_logger=True)
socket.connect('http://localhost:3030')

def send_message(event, data, room):
    try:
        data = {
            "data": data,
            "room": room
        }
        socket.emit(event, data)
    except:
        pass
