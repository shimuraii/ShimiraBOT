import discord
import asyncio
# id = ################### (Macdonalds' ID)
# mongodb for database
messages= joined = 0
client = discord.Client()
# async def update_stats():
#     await client.wait_until_ready()
#     global messages, joined
#     while not client.is_closed():
#         try:
#             with open("stats.txt", "a") as f:
#                 f.write(f"Messsages: {messages}, Members Joined: {joined}.\n")
#             messages = 0
#             joined = 0
#             await asyncio.sleep(1000)
#         except Exception as e:
#             print(e)
#             await asyncio.sleep(1000)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("shimira") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Gae")
@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send(f"""Welcome to the server {member.mention}. Here we have one simple rule and it is to answer a question: Why are you gae?""")
@client.event
async def on_message(message):
    id = client.get_guild(305065527301242880)
    global messages
    messages += 1
    channels = ["bot-commands"] # include other channels with ["aa", "bb", "cc"]
    valid_users = ["shimuraii#6945", "ALZ_XD#7884", "jun#7664", "Pacoca#3074", "Vitaodofutebao#1823", "ShimiraBOT#8081"]
    bad_words = ["pacoca", "jun", "alvaro"]
    for word in bad_words:
        if message.content.count(word) > 0:
            print("Oh shoot")
            await message.channel.purge(limit=1)
    if message.content == "!shimira":
        embed = discord.Embed(title="Help, Shimira!", description="Commands of the BOT:")
        embed.add_field(name="!shimira", value="ShimiraBOT Commands")
        embed.add_field(name="'jun' 'pacoca' 'alvaro'", value="Get censored instantly")
        embed.add_field(name="!users", value="Return Member Count")
        await message.channel.send(content=None, embed=embed)
    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("gae") != -1:
            await message.channel.send("why")
        elif message.content == "!users":
            await message.channel.send(f"""This server has {id.member_count}# members""")
    else:
        print(f""""Filha da puta: {message.author} tried to do {message.content}, in channel {message.channel}""")
client.loop.create_task(update_stats())
client.run("id")
