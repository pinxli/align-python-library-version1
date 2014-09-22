from Align.Curl import Curl
from Align.SqliteSession import SqliteSession
import sys, os

def main():
	cl = SqliteSession()
	
	cl.getAccessToken()

	# cl = Curl()

	# cl.get('products','42ztNrSxchJFTBDA6Avh')

	# cl.get('http://localhost:8000/')
	# cl.get('products')
	# cl.get('products','ZgAshovYZi1N9L43HVUW')
	# create = {
	# 	'first_name'		: 'Python Two',
	# 	'last_name'			: 'Test Two',
	# 	'email'				: 'testtwo@mail.com',
	# 	'address_1'			: 'required',
	# 	'address_2'			: 'required',
	# 	'address_number'	: 'required',
	# 	'address_city'		: 'required',
	# 	'address_state'		: 'required',
	# 	'address_zip'		: 'required',
	# 	'address_country'	: 'required',
	# 	'address_phone'		: 'require'
	# }
	# print(create)

	# create = {
	# 	'product_name' 			: 'Python Product 2',
	# 	'product_description'	: 'Python Product 2',
	# 	'product_price' 		: 20,
	# 	'product_shipping' 		: 10
	# }

	# cl.post('products',create)

	# update = {
	# 	'id' : '42ztNrSxchJFTBDA6Avh',
	# 	'data' : {	
	# 		'product_name' 			: 'Python Product 2sss',
	# 		'product_description'	: 'Python Product 2sss',
	# 		'product_price' 		: 20,
	# 		'product_shipping' 		: 10
	# 	}
	# }

	# cl.put('products',update)
	
	# cl.get('products','nFYNjcTcjotiIvPXoZwD')
	# cl.get('products','42ztNrSxchJFTBDA6Avh')
	# print("\n")

if __name__ == "__main__":
    main()
    # print( os.getcwd() )