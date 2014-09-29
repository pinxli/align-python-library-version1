from Align.Client import Client
from datetime import datetime, date, time
import sys, os, time

def main():
	cl = Client()

	""" List usage examples """

	print cl.buyer('list') 		
	print cl.invoice('list') 	
	print cl.product('product') 

	""" Info usage examples """
	print cl.buyer('info','<buyer_id>')
	print cl.invoice('info','<invoice_id>')
	print cl.product('info','<product_id>')

	""" Create/Update usage examples """
	create_invoice_data = {
		'checkout_type' : '<btc/bank_transfer>',
		'products' : [{
			'product_name' 		: '',
			'product_price' 	: '',
			'quantity' 			: '',
			'product_shipping' 	: ''
		}],
		'buyer_info'	: {
			'first_name' : '',
			'last_name'  : '',
			'email'		 : '',
			'address_1'  : '',
			'address_2'  : ''
		}
	}
	print cl.invoice('create',create_invoice_data)

	create_product_data = {
		'product_name' 			: '',
		'product_description'	: '',
		'product_price' 		: 20,
		'product_shipping' 		: 10
	}
	print cl.product('create',create_product_data)
	print mod.product('update','<product_id>',create_product_data)

if __name__ == "__main__":
    main()