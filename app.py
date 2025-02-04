import discord
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

secretTokenSideBot = os.getenv('SECRET_TOKEN_SIDE') #Used for testing purposes
token = os.getenv('TOKEN')
clientId = os.getenv('CLIENT_ID')
secretTokenMainBot = os.getenv('SECRET_TOKEN_MAIN') # used for scraping with the main bot
secretToken = secretTokenMainBot

serverName = os.getenv('SERVER_NAME')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def add_message_to_df(message, df): # Adds a message to a dataframe
    df = df._append({'message': message.content, 'author': message.author, 'authorID' : message.author.id, 'channel': message.channel, 'messageId' : message.id, 'timestamp' : message.created_at}, ignore_index=True)
    return df

def get_server(): # Returns the server object of the server with the name serverName
    servers = client.guilds
    for server in servers:
        if server.name == serverName:
            return server

def get_text_channels(server): # Returns all text channels in a server
    channels = server.text_channels
    print (server.name, ' has the following text channels:')
    for channel in channels:
        print(channel)
    return channels

async def write_channel_messages_to_file(channel): # Writes all messages from a channel to a csv file
    df = pd.DataFrame(columns=['message', 'author','authorID', 'channel', 'messageId', 'timestamp'])
    messages = channel.history(limit=None)
    async for message in messages:
        df = add_message_to_df(message, df)
    df.to_csv(str(channel.name) + '_Channel_messages.csv')
    print('Messages from ', channel.name, ' written to file')


@client.event
async def on_ready(): # Scrapes all messages from all channels in the server immidiately after logging in
    print(f'We have logged in as {client.user}')
    server = get_server()
    channels = get_text_channels(server)
    for channel in channels:
        await write_channel_messages_to_file(channel)

@client.event # Test function to see if the bot is working
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(secretToken)
