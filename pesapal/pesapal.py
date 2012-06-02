"""
MIT License

Copyright 2012 Okal Otieno

A library to interact with the Pesapal API from python applications.
"""

import oauth
from cgi import escape


class CallbackNotFound(Exception):
    pass


class DirectOrder(object):
    """
    Generate the oauth link for the payment page.
    """

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        token=None,
        params=None,
        products=None,
        callback=None):

        if not callback:
            raise CallbackNotFound

        api_endpoint = 'https://www.pesapal.com/api/PostPesapalDirectOrderV4'
        consumer_key = consumer_key
        consumer_secret = consumer_secret
        signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
        consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
        post_xml = """
            <?xml version="1.0" encoding="utf-8"?>
                <PesapalDirectOrderInfo
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                    Amount="100.00"
                    Description="Order payment"
                    Type="MERCHANT"
                    Reference="12"
                    FirstName="Foo"
                    LastName="Bar"
                    Email="foo@bar.com"
                    xmlns="http://www.pesapal.com" />
        """
        post_xml = escape(post_xml.strip())

        url = oauth.OAuthRequest.from_consumer_and_token(
            consumer,
            http_url=api_endpoint,
            http_method='GET',
            parameters=params)
        url.set_parameter('oauth_callback', callback)
        url.set_parameter('pesapal_request_data', post_xml)
        url.sign_request(signature_method, consumer, token)
        self.url = url.to_url()
