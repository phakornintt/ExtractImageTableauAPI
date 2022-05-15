# Import Libralies
import tableauserverclient as TSC
import config as cfg

tableau_server = 'https://www.bac.co.th:8000/'
site_id = 'bacdemo'
tableau_auth = TSC.TableauAuth(cfg.username,cfg.password,site_id)

server = TSC.Server(tableau_server)
server.add_http_options({'verify': False})
server.use_server_version()
server.auth.sign_in(tableau_auth)
print("Logged on Tableau Server")
