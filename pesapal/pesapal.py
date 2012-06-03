"""
MIT License

Copyright 2012 Okal Otieno

A library to interact with the Pesapal API from python applications.
"""

import oauth
from oauth import OAuthConsumer
from xml.etree import ElementTree as ET
from cgi import escape


class InvalidParameter(Exception):
    pass


class IncompleteInformation(Exception):
    pass


class DirectOrder(object):
    """
    Generate the oauth link for the payment page.
    """

    def __init__(
        self,
        oauth_consumer,
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

        signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
        consumer = oauth_consumer

        post_xml = ET.Element('PesapalDirectOrderInfo')

        post_xml.attrib['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
        post_xml.attrib['xmlns:xsd'] = 'http://www.w3.org/2001/XMLSchema'
        post_xml.attrib['xmlns'] = 'http://www.pesapal.com'
        post_xml.attrib['Type'] = 'MERCHANT'

        post_xml.attrib['Amount'] = str(amount)
        post_xml.attrib['Description'] = description
        post_xml.attrib['Reference'] = str(reference)

        if first_name:
            post_xml.attrib['FirstName'] = first_name

        if last_name:
            post_xml.attrib['LastName'] = last_name

        if currency:
            post_xml.attrib['Currency'] = currency  # Currency ISO code

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


class PaymentStatus(object):
    """
    Query the status of the Pesapal payment
    """
    def __init__(
        self,
        oauth_consumer,
        pesapal_merchant_reference,
        pesapal_transaction_tracking_id):

        signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
        api_endpoint = 'https://www.pesapal.com/API/QueryPaymentStatus'

        url = oauth.OAuthRequest.from_consumer_and_token(
            oauth_consumer,
            http_url=api_endpoint,
            http_method='GET')

        url.set_parameter(
            'pesapal_merchant_reference',
            pesapal_merchant_reference)

        url.set_parameter(
            'pesapal_transaction_tracking_id',
            pesapal_transaction_tracking_id)

        url.sign_request(signature_method, oauth_consumer, token=None)
        self.url = url.to_url()

    @property
    def message(self):
        """
        The status message returned by Pesapal.
        Possible values are <PENDING|COMPLETED|FAILED|INVALID>.
        Incorrect/invalid parameters result in an exception.
        """
        from urllib2 import urlopen

        f = urlopen(self.url)
        response = f.read()

        if response.startswith('Problem:'):
            raise InvalidParameter(response)
        else:
            return response
