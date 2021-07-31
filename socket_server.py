from flask import Flask
from flask_socketio import SocketIO, join_room
import eventlet

eventlet.monkey_patch()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('join')
def on_join(user):
    join_room(user)


@socketio.on('multiplication_table_server')
def listen(data=None):
    if data:
        socketio.emit('multiplication_table_client', data['data'], room=data['room'])

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3030)
