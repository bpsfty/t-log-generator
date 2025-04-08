from flask import Flask
import logging
import threading
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

def generate_logs():
    while True:
        logger.info("This is a log message.")
        time.sleep(300)  # Sleep for 5 minutes

@app.route('/')
def home():
    return "Log generator is running!"

if __name__ == '__main__':
    # Start the log generation in a separate thread
    log_thread = threading.Thread(target=generate_logs)
    log_thread.daemon = True
    log_thread.start()

    app.run(host='0.0.0.0', port=5000, debug=True)
