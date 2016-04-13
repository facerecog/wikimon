from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from req import getResponse
import re

def echo(message, match):
    print message.getBody()
    return TextMessageProtocolEntity("Echo: %s" % match.group("echo_message"), to=message.getFrom())


def ping(message, match):
    return TextMessageProtocolEntity("Pong!", to=message.getFrom())

def superbot(message, match):
    clean_bot_response = re.sub(r'(.)\1{3,}', '', message.getBody())
    bot_response = getResponse(clean_bot_response)
    string_bot_response = str(bot_response)
    string_bot_response = re.sub(r'(.)\1{3,}', '', string_bot_response)
    return TextMessageProtocolEntity(string_bot_response, to=message.getFrom())
