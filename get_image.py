# Import Libralies
from datetime import date
import tableauserverclient as TSC
import config as cfg
import urllib3
urllib3.disable_warnings()

# Set Up Connection
tableau_server = 'https://www.bac.co.th:8000/'
site_id = 'bacdemo'
tableau_auth = TSC.TableauAuth(cfg.username,cfg.password,site_id)

# Test Server Connection
server = TSC.Server(tableau_server)
server.add_http_options({'verify': False})
server.use_server_version()
server.auth.sign_in(tableau_auth)
print("Logged on Tableau Server")

target_view = 'Dashboard 10'

def getViewItem(username,password,site_id,target_view):
    tableau_auth = TSC.TableauAuth(username, password, site_id)
    with server.auth.sign_in(tableau_auth):
        all_views = {}
        for view in TSC.Pager(server.views):
            all_views[view.name] = view
        print(all_views)
    return all_views[target_view]

# Export File To Local
viewItem = getViewItem(cfg.username,cfg.password,site_id,target_view)
with server.auth.sign_in(tableau_auth):
    server.views.populate_image(viewItem)
    with open('./static/images/{}.png'.format(target_view + '_' + str(date.today())),'wb') as v:
        v.write(viewItem.image)