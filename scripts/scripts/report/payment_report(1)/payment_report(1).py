# Copyright (c) 2025, Kesavan and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):

	columns = get_columns()
	data = get_data(filters)

	return columns, data


def get_columns():

	return [
		{
		 "fieldname": "customer_id",
		 "fieldtype": "Data",
		 "label": "Customer ID",
		 "width": 200
		},
		{
		 "fieldname": "customer_name",
		 "fieldtype": "Data",
		 "label": "Customer Name",
		 "width": 200
		},
		{
		 "fieldname": "date_of_payment",
		 "fieldtype": "Datetime",
		 "label": "Date Of Payment",
		 "width": 200
		},
		{
  			"fieldname": "payment_method",
  			"fieldtype": "Select",
  			"label": "Payment Method",
  			"options": "UPI /nNet /nBanking/n Debit Card /nCredit Card",
  			"width": 200
		},
		{
		 "fieldname": "total_amount",
		 "fieldtype": "Currency",
		 "label": "Total Amount",
		 "width": 200
		},
		{
			"fieldname": "payment_status",
			"fieldtype":"Data",
			"label": "Status",
			"width": 200
		}
	]


def get_data(filters):

	conditions = {}

	if filters.get("customer_name"):
		conditions["customer_name"] = filters.customer_name
	if filters.get("date_of_payment"):
		conditions["date_of_payment"] = filters.date_of_payment
	if filters.get("payment_method"):
		conditions["payment_method"] = filters.payment_method

	frappe.log_error(conditions)


	return frappe.db.get_all(
		"Payment",
		filters=conditions,
		fields=["customer_id","customer_name","date_of_payment","payment_method","total_amount","payment_status"]

	)



