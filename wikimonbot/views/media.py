"""
    Media download request views.

    Handles the media url messages with utilities classes for it.
"""
import hashlib
from .. import config
import subprocess
from ..utils import media_sender


class MediaViews():
    def __init__(self, interface_layer):
        """
            Creates the regex routes and callbacks to handle media messages
        """
        self.image_sender = media_sender.ImageSender(interface_layer)
        self.video_sender = media_sender.VideoSender(interface_layer)
        self.url_print_sender = media_sender.UrlPrintSender(interface_layer)
        self.tts_sender = media_sender.EspeakTtsSender(interface_layer)
        self.routes = [
            ("https?:\/\/(?:[\w\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:jpe?g|gif|png)($|\?[^\s]+$)", self.send_image),
            ("https?:\/\/(?:[\w\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:mp4|webm)($|\?[^\s]+$)", self.send_video),
            ("https?:\/\/[^$]+$", self.send_url_print),
            ("^/t(ts)?\s(?P<tts_text>[^$]+)$", self.send_tts)
        ]

    def send_video(self, message, match):
        self.video_sender.send_by_url(jid=message.getFrom(), file_url=message.getBody())

    def send_image(self, message, match):
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=message.getBody())

    def send_url_print(self, message, match):
        url = message.getBody()
        self.url_print_sender.send_by_url(jid=message.getFrom(), file_url=url)

    def send_tts(self, message, match):
        tts_text = match.group("tts_text")
        self.tts_sender.send(jid=message.getFrom(), text=tts_text)

