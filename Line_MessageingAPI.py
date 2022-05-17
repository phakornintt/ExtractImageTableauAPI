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
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

username = cfg.userMS
password = cfg.passMS
site_name = 'ConsultingTeam'
base_path = 'https://bacthailand.sharepoint.com'
site_url = base_path + '/sites/' + site_name

ctx = ClientContext(site_url).with_credentials(UserCredential(username, password))


 line_bot_api = LineBotApi(cfg.channelAccTkn)
 line_bot_api.push_message('U4c7765f803509b5e226de11fdf8f4879', image_message)

# # ImageSendMessage
#
# image_message = ImageSendMessage(
    original_content_url='https://bacthailand.sharepoint.com/:i:/s/ConsultingTeam/ETwZAtzosgdDk93DDu9sgCgBTtrKoiaL7grhp-7slqRe-w?e=j7IhqH',
    preview_image_url='https://bacthailand.sharepoint.com/:i:/s/ConsultingTeam/ETwZAtzosgdDk93DDu9sgCgBTtrKoiaL7grhp-7slqRe-w?e=j7IhqH'
#     )
# # Line_bot_api.push_message(to, ImagesendMessage)
# line_bot_api.push_message('U4c7765f803509b5e226de11fdf8f4879', image_message)