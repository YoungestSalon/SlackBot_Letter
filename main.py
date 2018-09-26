from rtmbot import RtmBot
from rtmbot.core import Plugin

# secret라는 module에 있는 SLACK_TOKEN을 불러오는 코드
import secret

# logic이라는 module에 있는 Reply의 logic pattern을 불러오는 코드
import logic

class HelloPlugin(Plugin):
    def process_message(self, data):
        answer = logic.reply(data["text"])
        if answer is None:
            pass
        else:
            self.outputs.append([data["channel"], answer])

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
