import asyncio
import discord

client = discord.Client()


token = "NTA0MDE1MjI0MTk4OTIyMjcw.XZTpNA.4ryrh1KpM07BSPb8h_kR_JWT4mo"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("밥")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("노예남아"):
        await message.channel.send("내. 주인님.")
    if message.content.startswith("밥 줘"):
        await message.channel.send("냅! 10첩 반상으로 올릴게요 주인님^^♥")
    if message.content.startswith("밥줘"):
        await message.channel.send("냅! 10첩 반상으로 올릴게요 주인님^^♥")        
    if message.content.startswith("너 후장 얼마야?"):
        await message.channel.send("냅!!! 주인님 제 후장은 10원입니다^ㅇ^!!")
    if message.content.startswith("노예남 뭐해"):
        await message.channel.send("냅!! 밥하고 있슴다ㅎㅎ♥")
    if message.content.startswith("씨앙넘아"):
        await message.channel.send("냅! 저 부르셨나용'ㅁ'?")
    if message.content.startswith("창놈새끼"):
        await message.channel.send("힝ㅠ 저 총각인데..!ㅠㅠ")
    if message.content.startswith("돈 내놔"):
        await message.channel.send("냅! 계좌 알려주세용~^^ 헿♥♥♥")
    if message.content.startswith("자르셋"):
        await message.channel.send("힘 조~!!! 꽉꽉 채우는 중~~>_<!")
    if message.content.startswith("노예남 재기해"):
        await message.channel.send("냅ㅠ 주인님 바용가~ (폴짝!)")
    if message.content.startswith("노예남 신청"):
        await message.channel.send("넣고 싶은 명령어가 있으면 hyun님께 신청 넣어주세용 ^ㅇ^~♥")
    if message.content.startswith("노예남 신음"):
        await message.channel.send("엉어어어어어엉엉어엉엉 엉!엉!엉!엉!엉! 엉!응! 엉 엉 앙 앙 앙 앙 앙 흐아어엉~~!")
    if message.content.startswith("노예남 들어와"):
        await message.channel.send("냅!!! ~summon을 입력하시면 바로 들어갈게요!")
    if message.content.startswith("창놈"):
        await message.channel.send("저 찾으셨나요 ?ㅅ?")
    if message.content.startswith("창놈아"):
        await message.channel.send("내.주인님♥")
    if message.content.startswith("낸하"):
        await message.channel.send("노예남은 주인님께 다 드립니당")
    if message.content.startswith("걸레새끼"):
        await message.channel.send("ㅠㅠㅠㅠㅠㅠ...")
    if message.content.startswith("배고파"):
        await message.channel.send("냅!!! 제가 바로 집밥 차려드릴게요 (>_<)9!!")
    if message.content.startswith("노예남 자기소개"):
        await message.channel.send("현부양부가 꿈입니다♥ 취미는 요리 특기는 재기예요 헿")
        


        
client.run("NTA0MDE1MjI0MTk4OTIyMjcw.XZTpNA.4ryrh1KpM07BSPb8h_kR_JWT4mo")
