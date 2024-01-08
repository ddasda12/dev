from flask import Flask
from dhooks import Webhook
import schedule
import time

hook = Webhook(
    'https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx'
)

app = Flask(__name__)

@app.route('/')
def hello():
    hook.send('hello')
    return 'Hello, world'

def send_message():
    hook.send('Message sent every 5 minutes')

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    # Schedule the send_message function to be called every 5 minutes
    schedule.every(5).minutes.do(send_message)

    # Run the Flask app
    run()

    # Keep the program running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
