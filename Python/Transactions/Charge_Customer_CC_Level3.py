##
# BluePay Python Sample code.
#
# This code sample runs a $3.00 CC Sale transaction
# against a customer using test payment information.
##
from __future__ import print_function
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from BluePay import BluePay

account_id = "Merchant's Account ID Here"
secret_key = "Merchant's Secret Key Here"
mode = "TEST"  

payment = BluePay(
    account_id = account_id, 
    secret_key = secret_key, 
    mode = mode
) 

payment.set_customer_information(
    name1 = "Bob",
    name2 = "Tester",
    addr1 = "123 Test St.",
    addr2 = "Apt #500",
    city = "Testville",
    state = "IL",
    zipcode = "54321",
    country = "USA"
)

payment.set_cc_information(
    card_number = "4111111111111111",
    card_expire = "1225",
    cvv2 = "123"    
)

payment.add_line_item(
  quantity = "1", # The number of units of item. Max: 5 digits
  unit_cost = "3.00", # The cost per unit of item. Max: 9 digits decimal
  descriptor = "test", # Description of the item purchased. Max: 26 character
  commodity_code = "123412341234", # Commodity Codes can be found at http://www.census.gov/svsd/www/cfsdat/2002data/cfs021200.pdf. Max: 12 characters
  product_code = "432143214321", # Merchant-defined code for the product or service being purchased. Max: 12 characters 
  measure_units = "EA", # The unit of measure of the item purchase. Normally EA. Max: 3 characters
  tax_rate = "0%", # Tax rate for the item. Max: 4 digits
  tax_amount = "0.00", # Tax amount for the item. Max: 9 digits
  item_discount = "0.00", # The amount of any discounts on the item. Max: 12 digits.
  line_item_total = "3.00" # The total amount for the item including taxes and discounts.
)

payment.sale(amount = '3.00') # Sale Amount: $3.00

# Makes the API Request
payment.process()

# Read response from BluePay
if payment.is_successful_response():
    print('Transaction Status: ' + payment.status_response)
    print('Transaction Message: ' + payment.message_response)
    print('Transaction ID: ' + payment.trans_id_response)
    print('AVS Result: ' + payment.avs_code_response)
    print('CVV2 Result: ' + payment.cvv2_code_response)
    print('Masked Payment Account: ' + payment.masked_account_response)
    print('Card Type: ' + payment.card_type_response)
    print('Auth Code: ' + payment.auth_code_response)
else:
    print(payment.message_response)
