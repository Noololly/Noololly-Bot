import discord
import random
import praw

client = discord.Client()
reddit = praw.Reddit(client_id = "Wn07EJGAC60azPpkQk-JCw",
                     client_secret = "NHOPAG8Q8jxHuCAxxJVYDzAglJoG2A",
                     username = "NoolollyBot",
                     password = "PythonBot123",
                     user_agent = "pythonpraw",
                     check_for_async = False)
allPosts1 = []
s1 = reddit.subreddit("catpics")
t1 = s1.hot(limit = 100)
for submission in t1:
    allPosts1.append(submission)

allPosts2 = []
s2 = reddit.subreddit("memes")
t2 = s2.hot(limit = 100)
for submission in t2:
  allPosts2.append(t2)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.event
async def on_message(message):
    if message.content == "Hello!" or message.content == "Hi!":
        print("Message Received")
        x = random.randint(0,1)
        if x == 0:
            await message.channel.send(f"Hello, {message.author.name.split('#')[0]}!")
        else:
            await message.channel.send(f"Hi, {message.author.name.split('#')[0]}!")
    if message.content == "cat" or message.content == "Cat":
        global allPosts1
        random_post1 = random.choice(allPosts1)
        url1 = random_post1.url
        name1 = random_post1.title

        embed = discord.Embed(title = name1)
        embed.set_image(url = url1)
        embed.set_footer(text = "Developed by Noololly#4097")
        await message.channel.send(embed = embed)
        print(f'Cat Sent by {message.author.name}!')

    if "Meow" in message.content or "meow" in message.content:
        if message.author.name.split('#')[0] != "Noololly Bot":
            await message.channel.send(f"Yes, {message.author.name.split('#')[0]} meow!")
            print(f"Meow Sent by {message.author.name}!")
    
    if "gay" in message.content or "Gay" in message.content:
      await message.channel.send("Yes, Alex is gay!")

    if message.content == "Meme" or message.content == "meme":
      global allPosts2
      random_post2 = random.choice(allPosts2)
      url2 = random_post2.url
      name2 = random_post2.title
      embed = discord.Embed(title = name2)
      embed.set_image(url = url2)
      embed.set_footer("Developed by Noololly#4097")
    if message.content == "yeeeees":
        await message.channel.send(f"Well done {message.author.name.split('#')[0]}!")

client.run("OTEwOTQ4MjMxNTc4NTIxNjcy.YZaQpw.e2MiUYfFqApK7kVpz7tZOBcoJIU")
