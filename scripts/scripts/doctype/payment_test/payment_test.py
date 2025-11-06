import frappe
from frappe.model.document import Document

class PaymentTest(Document):
    pass

# @frappe.whitelist()
# def create_razorpay_order(docname):
#     doc = frappe.get_doc("Payment Test", docname)
#     client = razorpay.Client(auth=("rzp_test_1DP5mmOlF5G5ag", "1234567890abcdefghijk"))

#     order = client.order.create({
#         "amount": int(doc.amount) * 100,
#         "currency": "INR",
#         "payment_capture": 1
#     })

#     return {
#         "order_id": order["id"],
#         "amount": order["amount"]
#     }

# @frappe.whitelist()
# def verify_payment(payment_id, order_id, signature, docname):
#     doc = frappe.get_doc("Payment Test", docname)
#     doc.status = "Paid"
#     doc.save()
#     frappe.db.commit()
#     return "Success"
