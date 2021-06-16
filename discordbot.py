discordbot.py
# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンを定義する。
TOKEN = 'ODU0Njk1MzM1NTYxNjU4NDA4.YMnrDw.a8PSPTgKg9NicP0WInwwknZ1jUQ'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「猫の集い」が返る処理
    if message.content == '/neko':
        await message.channel.send('猫の集い')
    # 「/start」と発言したら「連携を開始します」が返る処理を追加。
    if message.content == '/start':
        await message.channel.send('連携を開始します')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
