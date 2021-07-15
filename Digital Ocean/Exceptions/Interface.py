import DigitalOcean


class Interface(DigitalOcean):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UnAuthorized(Interface):
    def __init__(self, url, *args, **kwargs):
        message = f"401 Unauthorized ({url})"
        super().__init__(message=message, *args, **kwargs)