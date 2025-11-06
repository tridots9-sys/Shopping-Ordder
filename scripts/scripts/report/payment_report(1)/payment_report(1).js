// Copyright (c) 2025, Kesavan and contributors
// For license information, please see license.txt

frappe.query_reports["Payment Report(1)"] = {
	filters: [
  		{
  		 "fieldname": "customer_name",
  		 "fieldtype": "Data",
  		 "label": "Customer Name",
  		 "mandatory": 0,
  		 "wildcard_filter": 0
  		},
  		{
  		 "fieldname": "date_of_payment",
  		 "fieldtype": "Datetime",
  		 "label": "Date Of Payment",
  		 "mandatory": 0,
  		 "wildcard_filter": 0
  		},
  		{
  		 "fieldname": "payment_method",
  		 "fieldtype": "Select",
  		 "label": "Payment Method",
  		 "mandatory": 0,
  		 "options": "UPI\nNet Banking\nDebit Card\nCredit Card",
  		 "wildcard_filter": 0
  		}
 	],
};
