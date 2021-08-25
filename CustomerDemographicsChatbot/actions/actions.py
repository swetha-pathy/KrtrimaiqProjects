from rasa_sdk.interfaces import Action
# from rasa_sdk.events import (
#     SlotSet,
#     EventType,
#     ActionExecuted,
#     SessionStarted,
#     Restarted,
#     FollowupAction,
#     UserUtteranceReverted,
# )
from rasa_sdk import Tracker
from typing import Any, Text, Dict, List

from typing import Text, List, Any, Dict


from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import psycopg2
import re
from psycopg2 import sql
import uuid
import sys
import psycopg2.extras


class PGdB:
    psycopg2.extras.register_uuid()

    def __init__(self, db_cred):
        self.hostName = db_cred['hostName']
        self.dbName = db_cred['dbName']
        self.userName = db_cred['userName']
        self.password = db_cred['password']
        self.conn = psycopg2.connect(host=self.hostName,
                                     database=self.dbName,
                                     user=self.userName,
                                     password=self.password)
        self.cur = self.conn.cursor()

    def reconnect(self):
        self.conn = psycopg2.connect(host=self.hostName,
                                     database=self.dbName,
                                     user=self.userName,
                                     password=self.password)
        self.cur = self.conn.cursor()

    def insert_row(self, values):
        names = ['customer_id', 'name', 'gender', 'dob', 'address', 'pincode', 'mobile_number', 'email_id',
                 'marital_status', 'ethnicity', 'household_income', 'employment', 'family_dependants',
                 'voting_status', 'languages', 'place_of_birth', 'religion', 'political_affiliation',
                 'educational_qualification', 'own_electricity_connection', 'own_ceiling_fan', 'own_lpg_stove',
                 'own_two_wheeler', 'own_color_tv', 'own_refrigerator', 'own_washing_machine', 'own_pc_laptop',
                 'own_vehicle', 'own_air_con', 'own_agricultural_land', 'own_residence', 'buy_residence', 'own_office',
                 'buy_office', 'own_diamond_necklace', 'buy_diamond_necklace', 'own_gold_necklace', 'buy_gold_necklace',
                 'buy_gold_ring', 'own_gold_ring', 'buy_diamond_ring', 'own_diamond_ring', 'own_iphone', 'buy_iphone',
                 'own_smart_tv', 'buy_smart_tv', 'own_macbook', 'buy_macbook', 'own_vacuum_cleaner',
                 'buy_vacuum_cleaner', 'own_hifi_car_audio', 'buy_hifi_car_audio', 'visit_hotels', 'visit_restaurants',
                 'use_airlines', 'visit_salons', 'use_cabs', 'take_regular_holidays', 'like_debt', 'spend_wo_thinking',
                 'good_managing_money', 'use_herbal_products', 'family_nutrition', 'healthy_diet', 'health_checks',
                 'pay_organic_food', 'pay_good_quality_products', 'buy_best_brands', 'spend_expensive_brands',
                 'take_holidays', 'new_holiday_destinations', 'take_holiday_abroad']
        query = sql.SQL("INSERT INTO rasa_customer_onboarding.customer_onboarding ({}) values ({})").format(
            sql.SQL(', ').join(map(sql.Identifier, names)),
            sql.SQL(', ').join(sql.Placeholder() * len(names))
        )

        self.cur.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        try:
            self.conn.close()
            self.cur.close()
        except Exception as e:
            pass


class ActionSaveSlotValues(Action):

    def name(self) -> Text:
        return "action_save_slot_values"

    @staticmethod
    def update_db(customer_id, tracker):
        slots = ['a_PERSON', 'a_gender', 'a_dob', 'a_address', 'a_pincode', 'a_mobile_no', 'a_email_id', 'a_status',
                 'a_ethnicity', 'b_household_income', 'b_employment_status', 'b_family_dependencies', 'b_voting_status',
                 'b_languages', 'b_place_of_birth', 'b_religion', 'b_political_affiliation',
                 'b_educational_qualification',
                 'c_elec_conn', 'c_ceiling_fan', 'c_lpg_stove', 'c_two_wheeler', 'c_color_tv', 'c_refrigerator',
                 'c_wash_machine', 'c_comp_laptop', 'c_car', 'c_ac', 'c_agri', 'd_real_estate_res_own',
                 'd_real_estate_res_pur', 'd_real_estate_off_own', 'd_real_estate_off_pur', 'd_jewel_dian_own',
                 'd_jewel_dian_pur', 'd_jewel_goln_own', 'd_jewel_goln_pur', 'd_jewel_golr_pur', 'd_jewel_golr_own',
                 'd_jewel_diar_pur', 'd_jewel_diar_own', 'd_elec_iphone_own', 'd_elec_iphone_pur', 'd_elec_smarttv_own',
                 'd_elec_smarttv_pur', 'd_elec_mac_own', 'd_elec_mac_pur', 'd_elec_vac_own', 'd_elec_vac_pur',
                 'd_elec_hifi_own', 'd_elec_hifi_pur', 'e_hotel', 'e_restaurant', 'e_airlines', 'e_saloon', 'e_cabs',
                 'f_regular_holiday', 'f_debt', 'f_expenditure', 'f_managing_money', 'f_herbal_product',
                 'f_family_nutrition',
                 'f_diet', 'f_health_check', 'f_pay_organic_food', 'f_pay_good_products', 'f_brands',
                 'f_expensive_brands',
                 'f_travelling', 'f_holiday_destination', 'f_holiday_abroad']

        values = [tracker.get_slot(slot) for slot in slots]
        values.insert(0, customer_id)
        values = tuple(values)

        credentials = {'hostName': "164.52.202.154",
                       'dbName': 'rasa_insurance',
                       'userName': 'rasa_insurance',
                       'password': 'rasa'}
        DB = PGdB(credentials)

        try:
            DB.insert_row(values)
        except psycopg2.InternalError:
            DB.reconnect()
            DB.insert_row(values)
        except psycopg2.InterfaceError:
            DB.reconnect()
            DB.insert_row(values)
        except Exception as e:
            print(e)
            sys.exit(-1)

        DB.close_connection()

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_id = uuid.uuid1()
        self.update_db(customer_id, tracker)
        # write_json_to_file("slots.json", tracker.slots)
        dispatcher.utter_template('utter_thanks_for_submitting', tracker)
        return []


class ValidateCustomerInfoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_customer_info_form"

    def validate_a_PERSON(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `a_PERSON` value."""

        # print(f"First name given = {slot_value} length = {len(slot_value)}")
        if " " in slot_value:
            return {"a_PERSON": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter both first name and last name.")
            return {"a_PERSON": None}

