"""Custom conversation handler for Confidence Builder."""
from lib.conversation import Conversation, ChatLine

_HELP = (
    "Commands: !wait (delay my first move), !name, !eval (spectators/self only), !queue, !who, !about"
)


class ConfidenceBuilderConversation(Conversation):

    def command(self, line: ChatLine, cmd: str) -> None:
        if cmd in ("commands", "help"):
            self.send_reply(line, _HELP)
        elif cmd == "who":
            self.send_reply(line, "I was made by a half-decent programmer and very bad chess player @scarecrw.")
        elif cmd == "about":
            self.send_reply(line, "I'm a training engine that dynamically adjusts to play plausible moves but provide opportunities for you to win.")
        else:
            super().command(line, cmd)
