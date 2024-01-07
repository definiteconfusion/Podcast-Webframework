from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Route for the sound detection page
@app.route('/')
def sound_detection():
    return render_template('sound_detection.html')

# Route for the header display page
@app.route('/display-header')
def display_header():
    return render_template('display_header.html')

# WebSocket event handlers... (your previous WebSocket code)
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('custom_message')
def handle_custom_message(json):
    print('Received message:', json)
    socketio.emit('message_received', json)

@socketio.on('sound_detected')
def handle_sound_detection(data):
    if data['status']:
        socketio.emit('display_header', {'display': True})

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
