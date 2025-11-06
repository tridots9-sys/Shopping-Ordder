# Copyright (c) 2025, Kesavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string


class Payment(Document):
    pass
	# @frappe.whitelist()
	# def change_status(self):
	# 	print("Hello")

	# 	doc = frappe.get_doc("Order Section",self.customer_id)

	# 	if(doc):
	# 		doc.status = "Paid"
	# 		doc.save()
	# 		return "Ok"
	# 	else:
	# 		return "Record Not Found"
		
	# def before_save(self):
	# 	if self.customer_name and self.mobile_no:
	# 		docs = frappe.get_all("Customer", 
	# 						filters={
	# 							"customer_name":self.customer_name, 
	# 							"mobile_no":self.mobile_no
	# 						},
	# 					   fields=[
	# 						   "customer_name",
	# 						   "mobile_no",
	# 						   "bank_name",
	# 						   "branch_name",
	# 						   "account_no",
	# 						   "ifsc_code",
	# 						   "balance",
	# 						   "c_card_no",
	# 						   "c_cvv",
	# 						   "c_exp_date",
	# 						   "c_card_limit",
	# 						   "d_card_no",
	# 						   "d_exp_date",
	# 						   "d_cvv_no",
	# 						   "d_card_limit",
	# 						   "upi_id",
	# 						   "upi_limit",
	# 						   "upi_id_password"
	# 					   ]
	# 		)

	# 		# docs = frappe.db.sql("""
	# 		# 				select * from `tabCustomer` where customer_name = %(customer_name)s And mobile_no = %(mobile_no)s
	# 		# 		   """, {"customer_name":self.customer_name, "mobile_no":self.mobile_no,}, as_dict = 0)

	# 		doc = docs[0]


	# 		# frappe.log_error(doc)
	# 		if(self.payment_method == "UPI"):
	# 			if(self.upi_id == doc["upi_id"] and self.upi_password == doc["upi_id_password"]):

	# 				if self.total_amount < doc["balance"]:
	# 					frappe.msgprint("Payment Done")
	# 				else:
	# 					frappe.throw("Insufficient Balance")
	# 			else:
	# 				frappe.throw("Invalid Credientials")
	# 		elif self.payment_method == "Net Banking":
	# 			self.Netbanking_validation()
	# 		elif self.payment_method == "Credit Card":
	# 			# self.credit_card()
	# 			print("hlo")

	# def before_submit(self):

	# 	# # if self.customer_name and self.mobile_no:
	# 	# # 	docs = frappe.get_all("Customer", 
	# 	# # 					filters={
	# 	# # 						"customer_name":self.customer_name, 
	# 	# # 						"mobile_no":self.mobile_no
	# 	# # 					},
	# 	# # 				   fields=[
	# 	# 					   "customer_name",
	# 	# 					   "mobile_no",
	# 	# 					   "bank_name",
	# 	# 					   "branch_name",
	# 	# 					   "account_no",
	# 	# 					   "ifsc_code",
	# 	# 					   "balance",
	# 	# 					   "c_card_no",
	# 	# 					   "c_cvv",
	# 	# 					   "c_exp_date",
	# 	# 					   "c_card_limit",
	# 	# 					   "d_card_no",
	# 	# 					   "d_exp_date",
	# 	# 					   "d_cvv_no",
	# 	# 					   "d_card_limit",
	# 	# 					   "upi_id",
	# 	# 					   "upi_limit",
	# 	# 					   "upi_id_password"
	# 	# # 				   ]
	# 	# # 	)

	# 	doc = frappe.get_value("Customer",filters={
	# 							"customer_name":self.customer_name, 
	# 							"mobile_no":self.mobile_no
	# 	}, as_dict = True)

	# 	docs = frappe.get_doc("Customer",doc)


	# 	if self.payment_status == "Paid":

	# 		balance = float(docs.balance) - float(self.total_amount)
	# 		frappe.log_error(balance)
	# 		docs.balance = balance
	# 		docs.save()

	# @frappe.whitelist()
	# def Netbanking(self):
		
	# 	doc = frappe.get_value("Customer", filters={
	# 		"customer_name":self.customer_name,
	# 		"mobile_no":self.mobile_no
	# 	})

	# 	docs = frappe.get_doc("Customer", doc)

	# 	if docs:
	# 		if docs.account_no == self.account_no and docs.ifsc_code == self.ifsc_code:
				
							   
	# 			self.account_holder_name = docs.customer_name
	# 			self.branch_name = docs.branch_name

	# 			id = string.ascii_uppercase + string.digits
	# 			self.transaction_id = ''.join(random.choice(id) for _ in range(20))
	# 	return True
	
	# @frappe.whitelist()
	# def Netbanking_validation(self):
	# 	doc = frappe.get_value("Customer", filters={
	# 		"customer_name":self.customer_name,
	# 		"mobile_no":self.mobile_no
	# 	})
	# 	docs = frappe.get_doc("Customer", doc)

	# 	if docs:
	# 		if self.total_amount < docs.balance:
	# 			frappe.msgprint("Payment Done")
	# 		else:
	# 			frappe.throw("Insufficient Balance")

	# 	if self.payment_status == "Paid":

	# 		self.status = "Success"
	# 		balance = float(docs.balance) - float(self.total_amount)
	# 		frappe.log_error(balance)
	# 		docs.balance = balance
	# 		docs.save()

	# def before_submit(self):


	# 	doc = frappe.get_value("Customer", filters={
	# 		"customer_name":self.customer_name,
	# 		"mobile_no":self.mobile_no
	# 	})
	# 	docs = frappe.get_doc("Customer", doc)

	# 	frappe.log_error(docs.c_card_no)

	# 	if docs:
	# 		if self.credit_card_no == docs.c_card_no and self.credit_card_holder_name == self.customer_name and self.card_cvv_no == docs.c_cvv and docs.c_exp_date == self.card_exp_no:

	# 			loan = float(self.total_amount) + float(docs.credit_card_loan_amount)
	# 			docs.credit_card_loan_amount = loan
	# 			docs.save()
	# 			frappe.log_error(loan)
	# 		else:
	# 			frappe.throw("invalid Credientials")
	# @frappe.whitelist()
	# def get_razorpay_order(*args, **kwargs):
	    
	#    return {"status": "ok"}