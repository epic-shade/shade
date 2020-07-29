import discord
from random import choice
from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n

from typing import List


_ = Translator("shade", __file__)

shade: List[str] = [
    _("Cancel my subscription because I’m done with your issues!"),
    _("Don't stand too close to the heater. Plastic melts!"),
    _("Don’t test me. I have screenshots."),
    _("He's the kind of guy a woman has to marry to get rid of."),
    _("I don't know what's more unfortunate, your grammar or your face!"),
    _("I don't suffer from insanity. I enjoy every minute of it!"),
    _("I love the sound you make when you shut up!"),
    _("I prefer not to think when I speak. I like being as surprised as everyone else with what comes out of my mouth."),
    _("I want two things from you: silence and distance!"),
    _("I would say I'd be your boss someday, but I don't plan on being a pimp!"),
    _("I'm not saying she's a slut but if she walks into a sperm bank, her spit would be accepted."),
    _("I’d like to see things from your point of view but I can’t seem to get my head that far up my ass."),
    _("I’m glad to see you’re not letting your education get in the way of your ignorance."),
    _("If you can't recognize a queen from a pawn, stick to checkers!"),
    _("If you're going to keep talking, I'm going to get my wine...and Ambien."),
    _("Just realized my life turned out better than yours. Checkmate, bitch!"),
    _("Light travels faster than sound. This is why some people appear bright until you hear them speak."),
    _("Maybe you should eat some makeup so you can be pretty on the inside, too."),
    _("My best relationship advice: make sure you're the crazy one!"),
    _("People say I act like I don't care. It's not an act!"),
    _("Scientists are trying to figure out how long human can live without a brain. You can tell them your age!"),
    _("You can't put a crown on a clown and expect a king!"),
    _("You have two parts of the brain, ‘left’ and ‘right’. In the left side, there’s nothing right. In the right side, there’s nothing left."),
    _("You're like the first slice of bread. Everybody touches you but nobody really wants you."),
    _("Your family tree must be a cactus because everybody on it is a prick."),
]


@cog_i18n(_)
class Shade(commands.Cog):
    """Shade users because it's fun!"""

    __author__ = ["Airen", "JennJenn", "TrustyJAID", "Evolve"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
            Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    @commands.command()
    async def shade(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """
            Shade the user
            `user` the user you would like to shade
        """
        msg = " "
        if user:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                bot_msg: List[str] = [
                    _("Hey, I appreciate the shade! :rofl:"),
                    _("No ***YOU'RE*** awesome! :smile:"),
                ]
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}")

            else:
                await ctx.send(user.mention + msg + choice(shade))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(shade))
