"""Custom conversation handler for Confidence Builder."""
import subprocess
from lib.conversation import Conversation, ChatLine

_HELP = (
    "Commands: !wait (delay my first move), !name, !eval (spectators/self only), !queue, !who, !about"
)

_NOTIFY_SCRIPT = "/home/evan/projects/chess_engine/notify_human_game.sh"


class ConfidenceBuilderConversation(Conversation):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.game.opponent.is_bot:
            opponent = self.game.opponent
            rating = str(opponent.rating) if opponent.rating is not None else "?"
            msg = (
                f"{opponent.name} ({rating}) | "
                f"{self.game.time_str()} {self.game.perf_name} | "
                f"{self.game.url()}"
            )
            subprocess.Popen([_NOTIFY_SCRIPT, msg],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def command(self, line: ChatLine, cmd: str) -> None:
        if cmd in ("commands", "help"):
            self.send_reply(line, _HELP)
        elif cmd == "who":
            self.send_reply(line, "I was made by a half-decent programmer and very bad chess player @scarecrw.")
        elif cmd == "about":
            self.send_reply(line, "I'm a training engine that dynamically adjusts to play plausible moves but provide opportunities for you to win.")
        else:
            super().command(line, cmd)
