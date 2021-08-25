import discord
from discord.ext import commands, tasks
from discord.utils import get

import os

class Pic2Url(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pic2url(self,ctx):
        fileNameList = os.listdir(f"./pic")
        newUrl = []
        for fileName in fileNameList:
            file = discord.File(f"./pic/{fileName}",)
            message = await ctx.send(file=file)
            imgURL = message.attachments[0].url
            newUrl.append(imgURL)
        with open(f"./pic/Urls.txt", "w") as txt:
            txt.write(str(newUrl))
        print(newUrl)

def setup(client):
    client.add_cog(Pic2Url(client))