## Yes intents -- Affirm intent
## No intents  -- Deny intent
class Intents:

    @staticmethod
    def affirm_intents(intentkey):
        affirm_intent = {
            "utter_ask_continue_buy_policy": ["action_insert_new_customer", "utter_documents_required_message",
                                              "utter_upload_document"],
            "utter_ask_continue_show_quotation": ["action_insert_new_customer", "utter_ask_sending_quotation"],
            "utter_ask_buy_policy": ["action_set_slot_flow_buy_policy", "utter_slots_values", "utter_ask_continue_buy_policy"],
            "utter_ask_anything_else": ["action_products_display"],
            "action_affirm": ["utter_documents_required_message", "utter_upload_document"],
            "action_existing_customer_update_phone_no": ["action_products_display"],
            "utter_upload_via_webcam_instructions": ["action_capture_document_image_and_crop"],
            "action_deny": ["action_products_display"],
            "action_ec_validate_update_email_otp": ["action_products_display"],
            "action_existing_customer_update_email_address": ["action_products_display"]
        }
        return affirm_intent[intentkey]

    def deny_intents(intentkey):
        deny_intents = {
            "utter_ask_continue_buy_policy": ["action_correct_cus_info", "utter_cus_info", "new_policy_form",
                                              "utter_slots_values", "utter_ask_continue_buy_policy"],
            "utter_ask_continue_show_quotation": ["action_correct_cus_info"],
            "utter_ask_buy_policy": ["utter_ask_anything_else"],
            "utter_ask_anything_else": ["action_thankyou"],
            "action_deny": ["action_thankyou"],
            "action_restart": ["action_thankyou"],
            "action_existing_customer_update_phone_no": ["action_thankyou"],
            "action_validate_existing_customer_otp":["action_thankyou"],
            "action_existing_customer_update_email_address": ["action_thankyou"]
        }
        return deny_intents[intentkey]

    @staticmethod
    def phone_no_intents(intentkey):
        phone_no_intents = {
            "utter_ec_phone_or_policy_number": ["ec_phone_no_form",
                                                 "action_validate_existing_customer"],
            "utter_update_details_options": ["action_set_slot_update_details"]
        }
        return phone_no_intents[intentkey]

    @staticmethod
    def scan_intents(intentkey):
        scan_intents = {
            "utter_upload_via_webcam_instructions": ["action_capture_document_image_and_crop"],
            "utter_ec_scan_or_manual_policy_no": ["action_scan_policy_qr_code", "utter_ec_options"]
        }
        return scan_intents[intentkey]


