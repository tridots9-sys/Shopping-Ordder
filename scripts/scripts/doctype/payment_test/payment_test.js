frappe.ui.form.on("Payment Test", {
    refresh(frm) {
        if (!frm.doc.__islocal) {
            frm.add_custom_button("Pay with Razorpay (Dummy)", () => {
                start_dummy_payment(frm);
            }, "Actions");
        }
    },
});

// function start_dummy_payment(frm) {
//     let options = {
//         key: "rzp_test_1DP5mmOlF5G5ag", // Razorpay dummy test key
//         amount: frm.doc.amount * 100, // convert rupees to paise
//         currency: "INR",
//         name: "Frappe Demo Payment",
//         description: "This is a dummy test transaction",
//         image: "https://razorpay.com/favicon.png",
//         handler: function (response) {
//             frappe.msgprint(`✅ Dummy Payment Success!
//             Payment ID: ${response.razorpay_payment_id || "N/A"}`);
            
//             // Optionally update status in Frappe
//             frm.set_value("status", "Paid");
//             frm.save();
//         },
//         theme: {
//             color: "#3399cc",
//         },
//     };

//     let rzp = new Razorpay(options);
//     rzp.open();
// }

function start_dummy_payment(frm){
    let options = {
        key: "rzp_test_1DP5mmOlF5G5ag",
        amount:frm.doc.amount * 100,
        currency: "INR",
        name: "SSS Supermarket",
        description: "Payment",
        image: "https://razorpay.com/favicon.png",
        method: {
            netbanking: true,
            card: true,
            upi: false,
            wallet: true,
            emi: false
        },
        handler: (r)=> {
            frappe.msgprint(`${frm.doc.amount} Paid Successfully
                 Payment ID : ${r.razorpay_payment_id || "N/A"}`);

            frm.set_value("status","Paid");
            frm.save()
                               
        },
        theme:{
            color: "#000000"
        },
    };

    let rzp = new Razorpay(options);
    rzp.open()
}
