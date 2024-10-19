# from frappe import _


# def get_data():
# 	return {
# 		"fieldname": "customer",
# 		"non_standard_fieldnames": {
# 			"Payment Entry": "party",
# 			"Quotation": "party_name",
# 			"Opportunity": "party_name",
# 			"Bank Account": "party",
# 			"Subscription": "party",
# 		},
# 		"dynamic_links": {"party_name": ["Customer", "quotation_to"]},
# 		"transactions": [
# 			{"label": _("Pre Sales"), "items": ["Opportunity", "Quotation"]},
# 			{"label": _("Orders"), "items": ["Sales Order", "Delivery Note", "Sales Invoice"]},
# 			{"label": _("Payments"), "items": ["Payment Entry", "Bank Account"]},
# 			{
# 				"label": _("Support"),
# 				"items": ["Issue", "Maintenance Visit", "Installation Note", "Warranty Claim"],
# 			},
# 			{"label": _("Projects"), "items": ["Project"]},
# 			{"label": _("Pricing"), "items": ["Pricing Rule"]},
# 			{"label": _("Subscriptions"), "items": ["Subscription"]},
# 		],
# 	}


# Original code has been commented out. Using custom code to include only Quotation, Sales Invoice, Payment Entry, and Project without labels.

# from frappe import _

# def get_data():
#     return {
#         "fieldname": "customer",
#         "non_standard_fieldnames": {
#             "Payment Entry": "party",
#             "Quotation": "party_name",
#             "Plot": "customer_name",
#         },
#         "dynamic_links": {"party_name": ["Customer", "quotation_to"]},
#         "transactions": [
#             {
#                 "items": [
#                     "Plot",
#                     "Quotation",
#                     "Project",
#                     "Sales Invoice",
#                     "Payment Entry"
#                 ]
#             }
#         ]
#     }

# from frappe import _


# def get_data():
# 	return {
# 		"fieldname": "customer",
# 		"non_standard_fieldnames": {
# 			"Payment Entry": "party",
# 			"Quotation": "party_name",
# 			"Plot": "customer_name",
# 			"Work": "customer",
# 		},
# 		"dynamic_links": {"party_name": ["Customer", "quotation_to"]},
# 		"transactions": [
# 			{"items": ["Plot", "Quotation", "Project", "Sales Invoice", "Payment Entry", "Work"]}
# 		],
# 	}


from frappe import _


def get_data():
	return {
		"fieldname": "customer",
		"non_standard_fieldnames": {
			"Payment Entry": "party",
			"Quotation": "party_name",
			"Plot": "customer_name",
			"Work": "customer",
		},
		"dynamic_links": {"party_name": ["Customer", "quotation_to"]},
		"transactions": [
			{"items": ["Plot", "Quotation", "Project", "Work", "Sales Invoice", "Payment Entry"]}
		],
	}
