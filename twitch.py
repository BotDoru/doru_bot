import discord
import requests
import asyncio
from json import loads
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
Token = os.environ["BOT_TOKEN"]

@client.event

async def on_ready(): 

    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------------------------')
    await client.change_presence(status=discord.Status.online)
    twitch = "twitchsummer030"
    #name = "여르미__"
    channel = client.get_channel(1011575939999735808)
    twitch_Client_ID = "rgdfpk99kre7h7o1zep21jutudnr4e"
    twitch_Client_secret = "gernxxi9zp73uglgfzx6bqdvn61ez4"
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Client_ID + "&client_secret=" + twitch_Client_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    print("-" + authorization)
    bang_on = 0
    while True:
        headers = {'Client-ID':twitch_Client_ID, 'Authorization': authorization}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and bang_on == 0:
                embed=discord.Embed(title="여르미 뱅온!", color=0x0c5aff)
                await channel.send(embed=embed)
                await channel.send("||@everyone||")
                bang_on = 1
        except:
            bang_on = 0
        await asyncio.sleep(3)
        
@client.event
async def on_member_join(member):
    print(member.name + "님이 입장했습니다.")
    channel = client.get_channel(1011574646841278536)
    await channel.send(member.mention + '님이 입장했습니다.')
    channel = client.get_channel(1011574646841278536)
    embed=discord.Embed(title="아쿠아리욺에 오신 것을 환영합니다!", description=f"{member.mention}님 어서오세요!", color=0x0c5aff)
    await channel.send(embed=embed)

client.run(Token)
