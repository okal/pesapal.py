Introduction
============

A python library to work with the [Pesapal](https://www.pesapal.com) payment API.

Usage
=====

API Methods

1. PesapalDirectOrderV4

    import pesapal

    consumer_key ='lhiP9QWtQQsXWU+G5HdFHEUr41COHMiI'  # Demo key. Replace with your own, provided by Pesapal
    consumer_secret = '5k6xJ7E0G5JFgUowlc+13SFEfkY='  # Demo consumer secret. Replace with your own.

    reference = 123  # Order reference number
    description = 'An order'  # Order description
    amount = 1199.00  # The total cost of the order
    callback='http://example.com'  # The URL the user will be redirected to after making a payment

    email = 'email@example.com'  # You must supply at least one of either a phone number or email
    phone_number = '012345678'
    direct_order = pesapal.DirectOrder(
        consumer_key,
        consumer_secret,
        reference,
        description,
        amount,
        callback,
        email=email,
        phone_number=phone_number)

    print direct_order.url  # This is the URL for the payment page

2. QueryPaymentStatus

    import pesapal

    consumer_key ='lhiP9QWtQQsXWU+G5HdFHEUr41COHMiI'  # Demo key. Replace with your own, provided by Pesapal
    consumer_secret = '5k6xJ7E0G5JFgUowlc+13SFEfkY='  # Demo consumer secret. Replace with your own.

    oauth_consumer = pesapal.OAuthConsumer(consumer_key, consumer_secret)

    pesapal_merchant_reference = 1234  # Order reference number
    pesapal_transaction_tracking_id = '4321'  # Tracking id returned by Pesapal as callback param

    payment_status = pesapal.PaymentStatus(
        consumer,
        pesapal_merchant_reference,
        pesapal_transaction_tracking_id)

    print payment_status.message  # Message returned by API call. This requires urllib2

Roadmap
=======

Implement the remaining api methods, namely

`QueryPaymentStatus`
`QueryPaymentDetails`

License
=======

Pesapal.py is Open Source Software, released under the terms of the [MIT License](http://www.opensource.org/licenses/mit-license.php).

&copy; [Okal Otieno](https://twitter.com/okalotieno), 2012.
