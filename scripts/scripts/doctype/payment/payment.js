// Copyright (c) 2025, Kesavan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment", {
    after_save(frm){
        // use a proper callback and frm.set_value to update the field
        setTimeout(function() {
            frm.set_value("payment_status", "Paid");
        }, 1000);

        if(frm.doc.payment_status == "Paid"){
            frm.set_df_property("payment_status", "read_only", 1);
            frm.set_df_property("payment_method", "read_only", 1);
            frm.set_df_property("credit_card_no", "read_only", 1);
            frm.set_df_property("credit_card_holder_name", "read_only", 1);
            frm.set_df_property("card_exp_no", "read_only", 1);
            frm.set_df_property("card_cvv_no", "read_only", 1);

            frm.call("change_status", { throw_if_missing : true})
            .then(r =>{
                if(r.message){
                    frappe.msgprint("Payment Done")
                }

            })


        }


    },
    // before_save(frm){
    //         frm.call("payments", { throw_if_missing : true})
    //         .then(r=>{
    //             if(r.message){
    //                 console.log(r.message)
    //             }
    //         })
        
    // },

    ifsc_code: function(frm){

        frm.call("Netbanking", { throw_if_missing : true})
        .then(r=>{
            if(r.message){
                frm.set_df_property("account_holder_name", "read_only", 1)
                frm.set_df_property("branch_name", "read_only", 1)
                frm.set_df_property("status", "read_only", 1)
                frm.set_df_property("transaction_id", "read_only", 1)

                console.log(r.message)
            }
        })
    }
});
