  
from .shade import shade


def setup(bot):
    n = shade(bot)
    bot.add_cog(n)
