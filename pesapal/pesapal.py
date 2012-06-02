"""
MIT License

Copyright 2012 Okal Otieno

A library to interact with the Pesapal API from python applications.
"""

import oauth
from xml.etree import ElementTree as ET
from cgi import escape


class IncompleteInformation(Exception):
    pass


class DirectOrder(object):
    """
    Generate the oauth link for the payment page.
    """

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        reference,
        description,
        amount,
        callback,
        email=None,
        phone_number=None,
        first_name=None,
        last_name=None,
        currency=None,
        token=None,
        params=None,
        products=None):

        if not email and not phone_number:
            raise IncompleteInformation('Supply either email or phone number')

        api_endpoint = 'https://www.pesapal.com/api/PostPesapalDirectOrderV4'

        consumer_key = consumer_key
        consumer_secret = consumer_secret
        signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
        consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)

        post_xml = ET.Element('PesapalDirectOrderInfo')

        post_xml.attrib['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
        post_xml.attrib['xmlns:xsd'] = "http://www.w3.org/2001/XMLSchema"
        post_xml.attrib['xmlns'] = "http://www.pesapal.com"
        post_xml.attrib['Type'] = 'MERCHANT'

        post_xml.attrib['Amount'] = str(amount)
        post_xml.attrib['Description'] = description
        post_xml.attrib['Reference'] = str(reference)

        if first_name:
            post_xml.attrib['FirstName'] = first_name

        if last_name:
            post_xml.attrib['LastName'] = last_name

        if currency:
            post_xml.attrib['Currency'] = currency #Currency ISO code

        if email:
            post_xml.attrib['Email'] = email

        if phone_number:
            post_xml.attrib['PhoneNumber'] = email

        post_xml = ET.tostring(post_xml)

        post_xml = escape(post_xml)

        url = oauth.OAuthRequest.from_consumer_and_token(
            consumer,
            http_url=api_endpoint,
            http_method='GET',
            parameters=params)
        url.set_parameter('oauth_callback', callback)
        url.set_parameter('pesapal_request_data', post_xml)
        url.sign_request(signature_method, consumer, token)
        self.url = url.to_url()
