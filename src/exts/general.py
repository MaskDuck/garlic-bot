from disnake import CommandInteraction
from disnake.ext.commands import Cog, slash_command

from src.impl.bot import Bot


class General(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="support", description="Get an invite link to the support server.")
    async def support(self, itr: CommandInteraction) -> None:
        await itr.send("Here's an invite to my support server: https://discord.gg/t5Bs4cXfv2", ephemeral=True)


def setup(bot: Bot) -> None:
    bot.add_cog(General(bot))