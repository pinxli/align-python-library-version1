from Align.Module import Module
from datetime import datetime, date, time
import sys, os, time

def main():
	mod = Module()

	create_product_data = {
		'product_name' 			: 'Python Lib Product 1',
		'product_description'	: 'Python Lib Product 1',
		'product_price' 		: 20,
		'product_shipping' 		: 10
	}
	# print mod.product('list')
	# print mod.product('info','c0wtkZonrfeXWTzayAHY')
	# print mod.product('create',create_product_data)

	create_invoice_data = {
		'checkout_type' : 'btc',
		'products' : [{
			'product_name' 		: 'Invoice prod1',
			'product_price' 	: '1',
			'quantity' 			: '1',
			'product_shipping' 	: '1'
		}]
		[],
		'buyer_info'	: {
			'first_name' : 'Invoice buyer1',
			'last_name'  : 'Invoice buyer1',
			'email'		 : 'invoicebuyer1@mail.com',
			'address_1'  : 'Invoice buyer1',
			'address_2'  : 'Invoice buyer1'
		}
	}
	# print type(create_invoice_data)
	# sys.exit()
	# print type(create_invoice_data)

	# print mod.invoice('list')
	# print mod.invoice('info','DkUph8nMYr4pySINqaDD')
	print mod.invoice('create',create_invoice_data)

if __name__ == "__main__":
    main()