import discord
from discord.ext import commands

import settings as discord_settings
from utils import search_google
from db import setup_db_table, create_search_history, get_search_history

bot = commands.Bot(command_prefix='!')


@bot.command(name='google', help='Return top five result from google search')
async def google_bot(ctx, *args):
    # validate user input
    if not args:
        await ctx.send(discord_settings.INPUT_REQUIRED_ERROR_MSG)
    else:
        search_keyword = ' '.join(args)
        # validate if input is less than or equal to 255 characters
        if len(search_keyword) > discord_settings.INPUT_MAX_LENGTH:
            await ctx.send(discord_settings.MAX_LENGTH_ERROR_MSG)
        else:
            # create entry in database
            create_search_history(search_keyword)
            # get result from google api
            results = search_google(search_keyword)
            if not results:
                await ctx.send(discord_settings.GOOGLE_NO_RESULT_MSG)
            for result in results:
                embed = discord.Embed(
                    title=result.get('title'),
                    url=result.get('link'),
                    description=result.get('description'),
                    color=discord_settings.EMBED_COLOR,
                )
                await ctx.send(embed=embed)


@bot.command(name='recent', help='Return top five related search history ')
async def search_history_bot(ctx, *args):
    # validate user input
    if not args:
        await ctx.send(discord_settings.INPUT_REQUIRED_ERROR_MSG)
    else:
        search_keyword = ' '.join(args)
        # validate if input is less than or equal to 255 characters
        if len(search_keyword) > discord_settings.INPUT_MAX_LENGTH:
            await ctx.send(discord_settings.INPUT_REQUIRED_ERROR_MSG)
        else:
            search_history = get_search_history(search_keyword)
            if search_history:
                search_history = ['**Search history**'] + search_history
            else:
                search_history = ['**No result found**']
            await ctx.send('\n'.join(search_history))


@google_bot.error
@search_history_bot.error
async def info_error(ctx, error):
    await ctx.send('Something went wrong. Error - {}'.format(error))


if __name__ == '__main__':
    setup_db_table()
    bot.run(discord_settings.TOKEN)
