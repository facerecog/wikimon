from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from req import getResponse

def echo(message, match):
    print message.getBody()
    return TextMessageProtocolEntity("Echo: %s" % match.group("echo_message"), to=message.getFrom())


def ping(message, match):
    return TextMessageProtocolEntity("Pong!", to=message.getFrom())

def superbot(message, match):
    bot_response = getResponse(message.getBody())
    string_bot_response = str(bot_response)
    return TextMessageProtocolEntity(string_bot_response, to=message.getFrom())
