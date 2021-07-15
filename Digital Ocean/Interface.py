import requests

from Exceptions import UnAuthorized
from warnings import warn

class Interface:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def call(self, endpoint, method='GET', version=2, **kwargs):
        """
        Makes calls to Digital Ocean

        :param endpoint: The endpoint used to make the request
        :param method: The method used to make the request
        :param version: The API version to use
        :param kwargs: Any Arguments that requests.Session.request takes.
        :return: The response object as a result of the call from Digital Ocean
        """

        url = f"https://api.digitalocean.com/v{version}/{endpoint}"

        response = self.session.request(url=url, method=method, **kwargs)

        if response.status_code in range(200, 300):
            return response

        elif response.status_code == 401:
            raise UnAuthorized(url)

        else:
            warn("Non 200 OK Response.")