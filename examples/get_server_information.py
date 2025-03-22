from pprint import pprint

from clientapi_cpanel import ApiException
from clientapi_cpanel.cpanel import cPanel
from clientapi_cpanel.exceptions import UnauthorizedException

try:
    cpanel = cPanel(
        host="https://my-cpanel-server.hu:2083/execute",
        username="__token__",
        password="..."
    )
    serverinfo_api = cpanel.CPanelServerInformationApi()
    serverinfo = serverinfo_api.get_information()
    pprint(serverinfo)
except UnauthorizedException as e:
    pprint(e)
except ApiException as e:
    pprint(e)
except Exception as e:
    pprint(e)