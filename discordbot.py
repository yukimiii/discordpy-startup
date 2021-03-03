from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_reaction_add(reaction,user):
	if reaction.emoji=="📧":
		embed = discord.Embed(description=reaction.message.content)
		embed.set_author(name=reaction.message.author.display_name,icon_url=reaction.message.author.avatar_url)
		# ファイルがある場合
		if reaction.message.attachments:
			for attachment in reaction.message.attachments:
				# Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
				if attachment.url.endswith(("png", "jpg", "jpeg","JPG")):
					embed.set_image(url=attachment.url)
		await user.send(embed=embed)
		# await user.send(reaction.message.content)

bot.run(token)
