Introduction
============

A python library to work with the [Pesapal](https://www.pesapal.com) payment API.

Usage
=====

To generate the payment page URL

    import pesapal

    consumer_key ='lhiP9QWtQQsXWU+G5HdFHEUr41COHMiI' #Demo key. Replace with your own, provided by Pesapal
    consumer_secret = '5k6xJ7E0G5JFgUowlc+13SFEfkY=' #Demo consumer secret. Replace with your own.
    callback='http://example.com' #The URL the user will be redirected to after making a payment

    direct_order = pesapal.DirectOrder(consumer_key, consumer_secret, callback)

    print direct_order.url #This is the URL for the payment page

Roadmap
=======

Implement the remaining api methods, namely

`QueryPaymentStatus`
`QueryPaymentDetails`

License
=======

Pesapal.py is Open Source Software, released under the terms of the [MIT License](http://www.opensource.org/licenses/mit-license.php).

&copy; [Okal Otieno](https://twitter.com/okalotieno), 2012.
