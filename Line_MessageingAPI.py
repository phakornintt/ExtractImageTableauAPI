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

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

####inputs########
# This will be the URL that points to your sharepoint site.
# Make sure you change only the parts of the link that start with "Your"
url_shrpt = 'https://bacthailand.sharepoint.com/sites/ConsultingTeam'
username_shrpt = cfg.userMS
password_shrpt = cfg.passMS
folder_url_shrpt = '/sites/ConsultingTeam/Shared%20Documents/General/Test'

#######################



###Authentication###For authenticating into your sharepoint site###
ctx_auth = AuthenticationContext(url_shrpt)
if ctx_auth.acquire_token_for_user(username_shrpt, password_shrpt):
  ctx = ClientContext(url_shrpt, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print('Authenticated into sharepoint as: ',web.properties['Title'])

else:
  print(ctx_auth.get_last_error())
############################




####Function for extracting the file names of a folder in sharepoint###
###If you want to extract the folder names instead of file names, you have to change "sub_folders = folder.files" to "sub_folders = folder.folders" in the below function
global print_folder_contents
def print_folder_contents(ctx, folder_url):
    try:

        folder = ctx.web.get_folder_by_server_relative_url(folder_url)
        fold_names = []
        sub_folders = folder.files #Replace files with folders for getting list of folders
        ctx.load(sub_folders)
        ctx.execute_query()

        for s_folder in sub_folders:

            fold_names.append(s_folder.properties["Name"])

        return fold_names

    except Exception as e:
        print('Problem printing out library contents: ', e)
######################################################


# Call the function by giving your folder URL as input
filelist_shrpt=print_folder_contents(ctx,folder_url_shrpt)

#Print the list of files present in the folder
print(filelist_shrpt)

#Specify the URL of the sharepoint file. Remember to change only the the parts of the link that start with "Your"
file_url_shrpt = '/sites/ConsultingTeam/Shared%20Documents/General/Test/{}'.format(filelist_shrpt[0])

#Load the sharepoint file content to "response" variable
response = File.open_binary(ctx, file_url_shrpt)

#Save the file to your offline path
with open("./test {}".format(filelist_shrpt[0]), 'wb') as output_file:
    output_file.write(response.content)

print(response)
line_bot_api = LineBotApi(cfg.channelAccTkn)
# ImageSendMessage
image_message = ImageSendMessage(
     original_content_url = File.get_image_preview_url(ctx,file_url_shrpt,400,400),
     preview_image_url= File.get_image_preview_url(ctx,file_url_shrpt,400,400)
     )
#line_bot_api.push_message(to, ImagesendMessage)
line_bot_api.push_message('U4c7765f803509b5e226de11fdf8f4879', image_message)