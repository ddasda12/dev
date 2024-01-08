from dhooks import Webhook
import time
hook=Webhook('https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx')


while True:
    hook.send('hello')
    time.sleep(10)
