from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import config as cfg
import os

# baseurl = 'https://bacthailand.sharepoint.com'
# basesite = '/sites/ConsultingTeam' # every share point has a home.
# siteurl = baseurl + basesite
#
# localpath = './Dashboard 10.png'
# remotepath = 'test/file.txt' # existing folder path under sharepoint site.
#
# ctx_auth = AuthenticationContext(siteurl)
# ctx_auth.acquire_token_for_user(cfg.userMS, cfg.passMS)
# ctx = ClientContext(siteurl, ctx_auth) # make sure you auth to the siteurl.
#
# with open(localpath, 'rb') as content_file:
#     file_content = content_file.read()
#
# dir, name = os.path.split(remotepath)
# file = ctx.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()

import requests
from shareplum import Office365

# Set Login Info
username = cfg.userMS
password = cfg.passMS
site_name = 'ConsultingTeam'
base_path = 'https://bacthailand.sharepoint.com'
doc_library = 'Shared%20Documents'
nested_folder = 'Shared%20Documents/General/Test' #if you want to upload in nested folders else nested_folder = doc_library
file_name = "Dashboard 10.png" #when your file in the same directory

# Obtain auth cookie
authcookie = Office365(base_path, username=username, password=password).GetCookies()
session = requests.Session()
session.cookies = authcookie
session.headers.update({'user-agent': 'python_bite/v1'})
session.headers.update({'accept': 'application/json;odata=verbose'})

session.headers.update({'X-RequestDigest': 'FormDigestValue'})
response = session.post(url=base_path + "/sites/" + site_name + "/_api/web/GetFolderByServerRelativeUrl('" + doc_library + "')/Files/add(url='a.txt',overwrite=true)",
                         data="")
session.headers.update({'X-RequestDigest': response.headers['X-RequestDigest']})

# Upload file
with open(file_name, 'rb') as file_input:
    try:
        response = session.post(
            url=base_path + "/sites/" + site_name + f"/_api/web/GetFolderByServerRelativeUrl('" + nested_folder + "')/Files/add(url='"
            + file_name + "',overwrite=true)",

            data=file_input)
        print("response: ", response.status_code) #it returns 200
        if response.status_code == '200':
            print("File uploaded successfully")
    except Exception as err:
        print("Something went wrong: " + str(err))

print('File Uploaded Successfully')