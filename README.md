# ExtractImageTableauAPI

The applications of this project are extract a dashboard in form of an image (.png) from Tableau server with Tableau Server REST API.
Afterward, push the dashboard image to Sharepoint by using Office365-REST-Python-Client

# Requirement
* Python 3.6+

* tableauserverclient 3.15

* Office365-REST-Pyhthon-Client

* SharePlum 0.5.1

# Installation
Use pip:

``` Ruby
pip install tableauserverclient
```
``` Ruby
pip install Office365-REST-Python-Client
```
``` Ruby
pip install SharePlum
```
# How to use
1. Create config.py following template before use
``` Ruby
username = 'TABLEAU SERVER USERNAME'
password = 'TABLEAU SERVER PASSWORD'
channelAccTkn = 'CHANNEL ACESS TOKEN (Messaging API)'
```
2. Open ngrok to use your localhost to online
``` 
ngrok http 5000
```
3. copy https address and replace endpoint in app.py. Then, excecute get_image.py, app.py respectively.
