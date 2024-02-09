from functools import wraps


class URI:
    """
    Injects a URI into a method. This is intended for usage with methods that invoke RPCs. To retrieve the RPC, you can
    use `locals()["uri"]`.
    :param uri: The URI to use.
    """

    def __init__(self, custom_uri):
        self.custom_uri = custom_uri

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            uri = self.custom_uri
            return func(*args, uri=uri, **kwargs)
        return wrapper
