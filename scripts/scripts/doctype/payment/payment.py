# Copyright (c) 2025, Kesavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Payment(Document):
	@frappe.whitelist()
	def change_status(self):
		print("Hello")

		doc = frappe.get_doc("Customer List",self.customer_id)

		if(doc):
			doc.status = "Paid"
			doc.save()
			return "Ok"
		else:
			return "Record Not Found"
