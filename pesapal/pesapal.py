"""
MIT License

Copyright 2012 Okal Otieno

A library to interact with the Pesapal API from python applications.
"""


class DirectOrder(object):
    """
    Generate the oauth link for the payment page
    """
    import oauth
    from cgi import escape

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        token=None,
        params=None,
        products=None,
        callback=None):

        api_endpoint = 'https://www.pesapal.com/api/PostPesapalDirectOrderV4'
        consumer_key = consumer_key
        consumer_secret = consumer_secret
        signature_method = oauth.OauthSignatureMethod_HMAC_SHA1()
        consumer = oauth.OauthConsumer(consumer_key, consumer_secet)
        url = oauth.OauthRequest.from_consumer_and_token(
            consumer,
            http_url=api_endpoint,
            http_method='GET',
            parameters=params)
        url.set_parameter('oauth_callback', callback)
        url.set_parameter('pesapal_request_data', post_xml)
