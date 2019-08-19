# invite link
# https://discordapp.com/oauth2/authorize?&client_id=612723457804861527&scope=bot&permissions=8
import discord

client = discord.Client()
token = "NjEyNzIzNDU3ODA0ODYxNTI3.XVn_hQ.6irIKOZaGBCi3InHT93hHN14-Yc"

cool_nums = ["69", "420", "1000", "1234", "2000", "3000", "4200", "6969", "10000", "100000"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == "counting":
        countingChannel = client.get_channel(message.channel.id)
        print(countingChannel.topic[12:])
        if message.content != countingChannel.topic[12:]:
            await message.delete()
        else:
            number = int(message.content) + 1
            await countingChannel.edit(topic = "Next Count: " + str(number))

        for num in cool_nums:
            if message.content == num:
                await message.pin()
    
@client.event
async def on_ready():  
    print('Joined Server as')
    print(client.user.name)
    print(client.user.id)
    print("------------------")

client.run(token)
