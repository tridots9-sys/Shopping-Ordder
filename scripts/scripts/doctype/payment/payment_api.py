import frappe
import requests

@frappe.whitelist()
def send_whatsapp_bill(docname):
    # Get Payment document
    doc = frappe.get_doc("Payment", docname)

    # Customer phone number (should be stored in Payment doctype)
    phone = doc.mobile_no or "91XXXXXXXXXX"  # Replace with default if needed

    # Generate the print format link
    print_url = frappe.utils.get_url(
        f"/printview?doctype=Payment&name={doc.name}&format=Bill Format&no_letterhead=0"
    )

    # WhatsApp message body
    message = f"Hello {doc.customer_name},\nThank you for your payment of ₹{doc.total_amount}.\nYour bill is ready:\n{print_url}"

    # UltraMsg API details
    url = "https://api.ultramsg.com/instance149077/messages/chat"
    data = {
        "token": "krv8uli5ygptdids",
        "to": phone,  # Must include country code (e.g., 91XXXXXXXXXX)
        "body": message,
    }

    # Send WhatsApp message
    response = requests.post(url, data=data)

    # Log response
    frappe.logger().info(f"WhatsApp Response: {response.text}")
    return response.json()
