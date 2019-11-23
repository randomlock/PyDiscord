import os
import random

import discord
import mysql.connector
from discord.ext import commands
from dotenv import load_dotenv

from utils import search_google
from db import setup_database_and_table, create_search_history, get_search_history

load_dotenv()
bot = commands.Bot(command_prefix='!')


@bot.command(name='google', help='Return top five result from google search')
async def google_bot(ctx, *args):
    if not args:
        await ctx.send('Please enter search keyword')
    else:
        search_keyword = ' '.join(args)
        if len(search_keyword) > 255:
            await ctx.send('Search keyword should be less than 255 characters')
        create_search_history(search_keyword)
        results = search_google(search_keyword)
        if not results:
            await ctx.send('No result found. Please try some other search')
        for result in results:
            embed = discord.Embed(
                title=result.get('title'),
                url=result.get('link'),
                description=result.get('description'),
                color=0x00ff40,
            )
            await ctx.send(embed=embed)


@google_bot.error
async def info_error(ctx, error):
    await ctx.send('Something went wrong')


@bot.command(name='recent', help='Return top five related search history ')
async def search_history_bot(ctx, *args):
    if not args:
        await ctx.send('Please enter search keyword')
    else:
        search_keyword = ' '.join(args)
        if len(search_keyword) > 255:
            await ctx.send('Search keyword should be less than 255 characters')
        else:
            search_history = ['**Search history**']
            search_history += get_search_history(search_keyword) or ['No result']
            await ctx.send('\n'.join(search_history))


if __name__ == '__main__':
    setup_database_and_table()
    TOKEN = os.getenv('DISCORD_TOKEN')
    print(TOKEN)
    bot.run(TOKEN)
