## buy_policy_1
## happy path product -> buy_policy -> correct_details -> webcam -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_2
## affirm in opening the webcam
## buy_policy -> correct_details -> webcam -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_4
## affirm happy path product -> buy_policy -> correct_details -> webcam -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* affirm
    - action_affirm
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_5
## happy path product -> buy_policy -> correct_details -> webcam -> upload not success -> re choose webcam->
## upload ok -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* upload_not_success
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_6
## happy path product -> buy_policy -> correct_details -> webcam -> upload not success -> re choose loacl file->
## upload ok -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* upload_not_success
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_7
## happy path product -> buy_policy -> correct_details -> localfile -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_8
## affirm happy path product -> buy_policy -> correct_details -> localfile -> paymentOK -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* affirm
    - action_affirm
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_9
## unhappy path product->buy_policy->wrong_details->re-enter_details->correct_details->webcam->paymentOK->no_main_menu

* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_wrong_buy_policy
    - action_correct_cus_info
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_10
## deny in details correct question
## unhappy path product->buy_policy->wrong_details->re-enter_details->correct_details->webcam->paymentOK->no_main_menu

* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* deny
    - action_deny
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## buy_policy_11
## deny in details correct question, affirm in confirming details, 
## unhappy path product->buy_policy->wrong_details->re-enter_details->correct_details->webcam->paymentOK->no_main_menu

* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* deny
    - action_deny
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* affirm
    - action_affirm
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* deny
    - action_deny

## buy_policy_12
## unhappy path product->buy_policy->wrong_details->re-enter_details->correct_details->localfile->paymentOK->no_main_menu

* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* buy_policy
    - action_set_slot_flow_buy_policy
    - utter_buy_policy_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_wrong_buy_policy
    - action_correct_cus_info
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - action_insert_new_customer
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## show_policy_1
## product->show_quotation->correct_details->send_quot_mail-> no_buy_policy -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou
    
## show_policy_2
## affirm product->show_quotation->correct_details->send_quot_mail-> no_buy_policy -> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou

## show_policy_3
## product->show_quotation->wrong_details->re-enter_details->correct_details->send_quot_mail->no_buy_policy->no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_wrong_show_quotation
    - action_correct_cus_info
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou
    
## show_policy_4
## deny in entering the details affirm in confirming the details, deny in buy policy and deny in anything else
## product->show_quotation->wrong_details->re-enter_details->correct_details->send_quot_mail->no_buy_policy->no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* deny
    - action_deny
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* deny
    - action_deny
* deny
    - action_deny

## show_policy_5
## deny in entering the details
## product->show_quotation->wrong_details->re-enter_details->correct_details->send_quot_mail->no_buy_policy->no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* deny
    - action_deny
    - utter_cus_info
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* deny
    - action_deny

## show_policy_6
## product->show_quotation -> send_quot_whatsapp -> no_buy_policy -> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* yes_main_menu
    - action_products_display
    
## show_policy_7
## deny in buy policy and affirm in ask anything else
## product->show_quotation -> send_quot_whatsapp -> no_buy_policy -> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* deny
    - action_deny
* affirm
    - action_affirm

## show_policy_8
## deny in buying policy
## product->show_quotation -> send_quot_whatsapp -> deny in buy_policy -> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* deny
    - action_deny
* affirm
    - action_affirm

## show_policy_9
## affirm for yes_main_menu -> product->show_quotation -> send_quot_whatsapp -> no_buy_policy -> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* affirm
    - action_affirm

## show_policy_10
## affirm product->show_quotation -> send_quot_whatsapp -> no_buy_policy -> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* yes_main_menu
    - action_products_display

## show_policy_11
## product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> local_file -> paymentOK-> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou
    
## show_policy_12
## affirm for yes_buy_policy and yes_detials_right 
## product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> local_file -> paymentOK-> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* affirm
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* affirm
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou
    
## show_policy_13
## affirm for yes_buy_policy and yes_detials_right 
## product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> local_file -> paymentOK-> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* affirm
    - action_affirm
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* affirm
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* affirm
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## show_policy_14
## product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> local_file -> paymentOK-> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* yes_main_menu
    - action_products_display

## show_policy_15
## affirm for yes_buy_policy -> product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> local_file -> 
## paymentOK-> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* affirm
    - action_affirm
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - utter_documents_required_message
    - utter_upload_document
* localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* yes_main_menu
    - action_products_display

## show_policy_16
## product->show_quotation -> send_quot_whatsapp -> yes_buy_policy -> web_cam -> paymentOK-> no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## show_policy_17
## product->show_quotation ->send_quot_whatsapp -> yes_buy_policy -> web_cam -> paymentOK-> yes_main_menu
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_whatsapp
    - utter_whatsapp_instructions
* done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ask_buy_policy
* yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_slots_values
    - utter_ask_continue_buy_policy
* info_correct_buy_policy
    - utter_documents_required_message
    - utter_upload_document
* webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* yes_main_menu
    - action_products_display

## show_policy_18
## very unhappy path
* greet
    - utter_greet
    - utter_type_customer
* new_policy
    - action_products_display 
* product
    - action_product_info_display
    - utter_buy_or_quote
* show_quotation
    - action_show_quotation
    - utter_provide_details_message
    - name_phoneno_form
    - form{"name": "name_phoneno_form"}
    - form{"name": null}
    - age_profession_form
    - form{"name": "age_profession_form"}
    - form{"name": null}
    - email_address_form
    - form{"name": "email_address_form"}
    - form{"name": null}
    - utter_slots_values
    - utter_ask_continue_show_quotation
* info_correct_show_quotation
    - action_insert_new_customer
    - utter_ask_sending_quotation
* send_quotation_mail
    - action_send_mail
    - utter_ask_buy_policy
* no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou

## exisiting_policy flow starts here

## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->buy policy->localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## enter phone_no on identifying customer
## existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->buy policy->localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* phone_intent
    - action_phone_no_intent
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->buy policy-> webcam
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou
    
## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->show quotation-> via mail-> yes buy policy-> webcam
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou
    
## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->show quotation-> via mail-> yes buy policy-> localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->view products->show quotation-> via whatsapp-> yes buy policy-> localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_whatsapp
    - utter_ec_whatsapp_instructions
* ec_done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou


## happy path existing customer->enter phone_no->validate ok->enter otp->otp not ok-> re- enter otp-> otp ok
## display customer details->view products->show quotation-> via whatsapp-> yes buy policy-> webcam
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_whatsapp
    - utter_ec_whatsapp_instructions
* ec_done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## Unhappy path existing customer->enter phone_no->validate not ok->enter otp->otp ok->display customer details-> view products
## -> show quotation-> yes send mail->no buy policy
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou

## existing customer->enter phone_no->validate not ok->enter otp-> validate not ok otp-> re-enter otp
## otp ok->display customer details-> view products -> show quotation-> yes send mail-> no buy policy
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou

## happy path existing customer->enter phone_no->validate not ok->enter otp->otp ok->display customer details-> view products
## -> show quotation-> no send mail->no buy policy
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_whatsapp
    - utter_ec_whatsapp_instructions
* ec_done_whatsapp_initiation
    - action_send_whatsapp_quotation
    - utter_ec_ask_buy_policy
* ec_no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou 

## happy path existing customer->enter phone_no->validate not ok->enter otp->otp ok->display customer details-> view products
## -> show quotation-> yes send mail->yes buy policy->webcam
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path existing customer->enter phone_no->validate not ok->enter otp->otp ok->display customer details-> view products
## -> show quotation-> yes send mail->yes buy policy->localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou


## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->view products->buy policy
## -> localfile
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->view products->show quotation
## ->yes send mail->yes buy policy-> localfile

* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_localfile_upload
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->view products->show quotation
## ->yes send mail->yes buy policy-> webcam

* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
    - utter_ec_ask_sending_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_yes_buy_policy
    - action_set_slot_flow_buy_policy
    - utter_ec_documents_required_message
    - utter_ec_upload_document
* ec_webcam
    - utter_upload_success_go_to_payment_message
* go_to_payment
    - utter_payment_success_message
    - action_send_mail
    - utter_ask_anything_else
* restart
    - action_restart
* no_main_menu
    - action_thankyou

## happy path with existing customer-> policy no-> manually-> validate Not ok-> re-enter policy no(handled within followup action)
## ->validate Ok->display customer details-> view products -> show quotation-> yes send mail->no buy policy
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* view_products
    - action_products_display
* product
    - action_product_info_display
    - utter_ec_buy_or_quote
* ec_show_quotation
    - action_show_quotation
* ec_send_quotation_mail
    - action_send_mail
    - utter_ec_ask_buy_policy
* ec_no_buy_policy
    - utter_ask_anything_else
* no_main_menu
    - action_thankyou

## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details->update ph no option-> otp ok-> update ph no 
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou
 

## happy path existing customer->enter phone_no->validate ok->enter otp->otp not ok-> re enter otp-> otp ok
## display customer details->update details->update ph no option-> otp ok-> update ph no 
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou

## enter phone_no as text for update phone no   
## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details->update ph no option-> otp ok-> update ph no 
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* phone_intent
    - action_phone_no_intent
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou
    
## enter phone_no as text for update phone no   
## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details->update ph no option-> otp ok-> update ph no -> affirm in ask anything else 
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* phone_intent
    - action_phone_no_intent
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* affirm
    - action_affirm

## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details->update ph no option-> otp not ok->re-enter otp-> update ph no 
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou
    
## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->update details->ph no
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou

## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->update ph no->
## ->otp not ok->re-enter otp->update ph no
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* no_main_menu
    - action_thankyou
 
 ## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->update ph no->
## ->otp not ok->re-enter otp->update ph no-> deny in anything else
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_phone_no
    - action_set_slot_update_details
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - action_send_mail_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_phone_no_otp
* deny
    - action_deny
    
## happy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details-> update email ID -> send whats app otp -> validate otp ok -> email updated
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* no_main_menu
    - action_thankyou

## happy path with existing customer-> policy no-> manually-> validate ok->display customer details->update details->email id
## -> send whats app otp -> validate otp ok -> email updated
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* no_main_menu
    - action_thankyou

## Unhappy path existing customer->enter phone_no->validate ok->enter otp->otp ok->
## display customer details->update details-> update email ID -> send whats app otp -> validate otp not ok
## re enter otp -> email updated
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* no_main_menu
    - action_thankyou
    
## Unhappy path with existing customer-> policy no-> manually-> validate ok->display customer details->update details->email id
## -> send whats app otp -> validate otp not ok -> re enter otp -> email updated-> deny in no_main_menu
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* deny
    - action_deny


## Unhappy path with existing customer-> policy no-> manually-> validate ok->display customer details->update details->email id
## -> send whats app otp -> validate otp not ok -> re enter otp -> email updated-> affirm in yes_main menu
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_policy_no
    - utter_ec_scan_or_manual_policy_no
* ec_policy_no_manually
    - ec_policy_no_form
    - form{"name": "ec_policy_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* affirm
    - action_affirm

## Unhappy path with existing customer-> phone no-> validate not ok->re-enter phone no-> validate ok ->
## display customer details->update details->email id-> send whats app otp -> validate otp ok-> email updated-> no_main menu
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* no_main_menu
    - action_thankyou

## Unhappy path with existing customer-> phone no-> validate not ok->re-enter phone no-> validate ok ->
## display customer details->update details->email id-> send whats app otp -> validate otp ok-> email updated-> yes_main menu
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* yes_main_menu
    - action_products_display

## existing customer->enter phone_no->validate not ok->enter otp-> validate not ok otp-> re-enter otp
## otp ok->display customer details-> update details->email id-> send whats app otp -> validate otp ok-> email updated-> no_main menu
* greet
    - utter_greet
    - utter_type_customer
* existing_policy
    - utter_ec_phone_or_policy_number
* ec_phone_no
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_phone_no_form
    - form{"name": "ec_phone_no_form"}
    - form{"name": null}
    - action_validate_existing_customer
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
    - ec_otp_form
    - form{"name": "ec_otp_form"}
    - form{"name": null}
    - action_validate_existing_customer_otp
* update_details
    - utter_update_details_options
* update_email_id
    - action_set_slot_update_details_email
    - ec_update_details_form
    - form{"name": "ec_update_details_form"}
    - form{"name": null}
    - utter_ec_whatsapp_otp_instructions
* ec_continue_to_send_otp
    - action_send_whatsapp_otp_update_email
    - ec_whatsapp_otp_form
    - form{"name": "ec_whatsapp_otp_form"}
    - form{"name": null}
    - action_ec_validate_update_email_otp
* yes_main_menu
    - action_products_display

## bot challenge
* bot_challenge
  - utter_iamabot