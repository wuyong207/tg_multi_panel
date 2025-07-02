import asyncio
from telethon import TelegramClient
import yaml

async def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    clients = []
    for account in config['accounts']:
        client = TelegramClient(account['session'], config['api_id'], config['api_hash'])
        await client.start(phone=account['phone'])
        clients.append(client)
        print(f"已登录账号：{account['phone']}")

    for client in clients:
        me = await client.get_me()
        await client.send_message('me', '群控系统测试消息')
        print(f"账号 {me.username} 发送测试消息成功")

    for client in clients:
        await client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

