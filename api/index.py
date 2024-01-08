from flask import Flask, render_template
from threading import Thread
from dhooks import Webhook

hook=Webhook('https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx')
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'
    hook.send('hello')
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

def keep_alive():
  t1 = Thread(target=run)
  t1.start()
  


if __name__ == '__main__':
  keep_alive()
