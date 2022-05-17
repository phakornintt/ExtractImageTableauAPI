# from office365.runtime.auth.authentication_context import AuthenticationContext
# from office365.sharepoint.client_context import ClientContext
import config as cfg
import os
import requests
from shareplum import Office365
from datetime import date
import datetime

# Set Login Info
username = cfg.userMS
password = cfg.passMS
site_name = 'ConsultingTeam'
base_path = 'https://bacthailand.sharepoint.com'
doc_library = 'Shared%20Documents'
nested_folder = 'Shared%20Documents/General/Test' #if you want to upload in nested folders else nested_folder = doc_library
file_name = "Dashboard 10{}.png".format('_' + str(date.today())) #when your file in the same directory

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