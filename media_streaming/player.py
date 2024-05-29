from flask import Flask, Response, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <body>
            <h1>Video Streaming</h1>
            <video width="640" height="480" controls autoplay>
                <source src="/video_feed" type="video/mp4">
                Not supported
            </video>
        </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    # Directly use send_file to serve the video file
    return send_file('ubur_ubur.mp4', mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
