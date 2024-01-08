from dhooks import Webhook
import time
from index import keep_alive
hook=Webhook('https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx')


while True:
    hook.send('hello')
    time.sleep(10)
    keep_alive()
