from flask import Flask
from dhooks import Webhook

hook = Webhook(
    'https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx'
)

app = Flask(__name__)


@app.route('/')
def hello():
  hook.send('hello')
  return 'Hello, world'


@app.route('/test')
def test():
  hook.send('hello')  # Moved this line before the return statement
  return 'Test'


def run():
  app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
  run()
