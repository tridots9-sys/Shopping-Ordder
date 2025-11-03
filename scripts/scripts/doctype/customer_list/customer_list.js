frappe.ui.form.on("Order Table",{

    qty: function(frm,cdt,cdn){
        let row = locals[cdt][cdn];

        row.total = row.qty * row.price;

        frm.refresh_fields("order")
        calculation(frm);
    },
    // product_id: function(frm, cdt, cdn) {
    //     let d = locals[cdt][cdn];
    //     const childfield = d.parentfield;
    //     frm.set_query("product_id", childfield, () => {
    //         return {
    //             filters: {
    //                 product_name: ["in", ["Apricot", "Apple Kashmir"]]
    //             }
    //         };
    //     });
    // }

})

frappe.ui.form.on("GST Table",{

    gst_percentage: function(frm,cdt,cdn){
        
        gst_calculation(frm, cdt, cdn);

        
    }
})

function calculation(frm){

    let total = 0;

    (frm.doc.order || []).forEach(row => {

        total += row.total;        
    });

    frm.set_value("total_amount",total);

}

function gst_calculation(frm,cdt,cdn){
    

    let amount = frm.doc.total_amount;
    let row = locals[cdt][cdn];

    row.total_amount = amount

    frm.set_df_property("total_amount", "read_only", 1);


    row.gst_percent = (row.total_amount * row.gst_percentage) / 100;

    frm.refresh_fields("gst")
    grand_total_calculation(frm, cdt, cdn);
}

function grand_total_calculation(frm,cdt,cdn){

    let grand_total = 0;

    let row = locals[cdt][cdn];

    grand_total = row.total_amount + row.gst_percent;

    frm.set_value("grand_total", grand_total);

    frm.set_df_property("grand_total", "read_only", 1);
}

// frappe.ui.form.on("Order Table", {

// });

