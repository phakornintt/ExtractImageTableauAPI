# Import
import config as cfg
from shareplum import Office365
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent)


line_bot_api = LineBotApi(cfg.channelAccTkn)

# # ImageSendMessage
#
image_message = ImageSendMessage(
    original_content_url='https://bacthailand-my.sharepoint.com/:i:/g/personal/phakorn_bac_co_th/EeYRemEvvx5DuBbxpg-VkzYBOJ3uEvwmCXAfcaxttfj77g?e=q8ArFx',
    preview_image_url='https://bacthailand-my.sharepoint.com/:i:/g/personal/phakorn_bac_co_th/EeYRemEvvx5DuBbxpg-VkzYBOJ3uEvwmCXAfcaxttfj77g?e=q8ArFx'
    )
# Line_bot_api.push_message(to, ImagesendMessage)
line_bot_api.push_message('U4c7765f803509b5e226de11fdf8f4879', image_message)