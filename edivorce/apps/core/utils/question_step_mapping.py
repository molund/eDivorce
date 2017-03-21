"""
    Mapping between questions and steps
    Usage: For each step title, list all questions_keys belong to that step
"""
question_step_mapping = {'prequalification': ['married_marriage_like', 'lived_in_bc', 'lived_in_bc_at_least_year', 'separation_date',
                                              'children_of_marriage', 'any_under_19', 'children_financial_support', 'original_marriage_certificate',
                                              'provide_certificate_later', 'provide_certificate_later_reason', 'not_provide_certificate_reason',
                                              'divorce_reason', 'marriage_certificate_in_english', 'try_reconcile_after_separated', 'reconciliation_period',],
                         'which_orders': ['want_which_orders',],
                         'your_information': ['name_you', 'any_other_name_you', 'other_name_you', 'last_name_born_you',
                                              'last_name_before_married_you', 'birthday_you', 'lived_in_bc_you', 'moved_to_bc_date_you',
                                              'occupation_you'],
                         'your_spouse': ['name_spouse', 'any_other_name_spouse', 'other_name_spouse', 'last_name_born_spouse',
                                         'last_name_before_married_spouse', 'birthday_spouse', 'lived_in_bc_spouse', 'moved_to_bc_date_spouse',
                                         'occupation_spouse'],
                         'your_marriage': ['when_were_you_married', 'where_were_you_married_city', 'where_were_you_married_prov',
                                           'where_were_you_married_country', 'where_were_you_married_other_country', 'marital_status_before_you',
                                           'marital_status_before_spouse', 'when_were_you_live_married_like', ],
                         'your_separation': ['no_reconciliation_possible', 'no_collusion',],
                         'spousal_support': ['spouse_support_details', 'spouse_support_act',],
                         'property_and_debt': ['deal_with_property_debt', 'how_to_divide_property_debt', 'other_property_claims', 'want_other_property_claims'],
                         'other_orders': ['other_orders_detail'],
                         'other_questions': ['address_to_send_official_document_street_you',
                                             'address_to_send_official_document_city_you',
                                             'address_to_send_official_document_prov_you',
                                             'address_to_send_official_document_country_you',
                                             'address_to_send_official_document_other_country_you',
                                             'address_to_send_official_document_postal_code_you',
                                             'address_to_send_official_document_fax_you',
                                             'address_to_send_official_document_email_you',
                                             'address_to_send_official_document_street_spouse',
                                             'address_to_send_official_document_city_spouse',
                                             'address_to_send_official_document_prov_spouse',
                                             'address_to_send_official_document_country_spouse',
                                             'address_to_send_official_document_other_country_spouse',
                                             'address_to_send_official_document_postal_code_spouse',
                                             'address_to_send_official_document_fax_spouse',
                                             'address_to_send_official_document_email_spouse',
                                             'divorce_take_effect_on',
                                             'divorce_take_effect_on_specific_date',],
                         'filing_locations': ['court_registry_for_filing',],
                         }


"""
    Dictionary for a list of court registries
"""
list_of_registries = ['Fort St. John', 'Dawson Creek', 'Prince Rupert', 'Terrace', 'Smithers', 'Prince George', 'Quesnel',
                      'Williams Lake', 'Campbell River', 'Powell River', 'Courtenay', 'Port Alberni', 'Duncan', 'Nanaimo',
                      'Victoria', 'Golden', 'Kamloops', 'Salmon Arm', 'Vernon', 'Kelowna', 'Penticton', 'Nelson', 'Rossland',
                      'Cranbrook', 'Chilliwack', 'New Westminster', 'Vancouver', 'Fort Nelson', 'Revelstoke',]


complete_state_for_step = {'which_orders': {'required': ['want_which_orders']},
                           'your_information': {'required': ['name_you', 'last_name_born_you',
                                                             'last_name_before_married_you', 'birthday_you', 'occupation_you'],
                                                'conditional': {'any_other_name_you': ['YES', 'other_name_you'],
                                                                'lived_in_bc_you': ['Moved to B.C. on', 'moved_to_bc_date_you']},},
                           'your_spouse': {'required': ['name_spouse', 'last_name_born_spouse',
                                                        'last_name_before_married_spouse', 'birthday_spouse', 'occupation_spouse'],
                                           'conditional': {'any_other_name_spouse': ['YES', 'other_name_spouse'],
                                                           'lived_in_bc_spouse': ['Moved to B.C. on', 'moved_to_bc_date_spouse']},},
                           'your_marriage': {'required': ['when_were_you_live_married_like', 'marital_status_before_you', 'marital_status_before_spouse'],
                                             'conditional': {'married_marriage_like': ['Legally married', 'when_were_you_married']}},
                           'your_separation': {'required': ['no_reconciliation_possible', 'no_collusion']},
                           'spousal_support': {'required': ['spouse_support_details', 'spouse_support_act']},
                           'property_and_debt': {'required': ['want_other_property_claims', 'other_property_claims'],
                                                 'conditional': {'deal_with_property_debt': ['unequal division', 'how_to_divide_property_debt']}},
                           'other_orders': {'required': ['other_orders_detail']},
                           'other_questions': {'required': ['address_to_send_official_document_street_you',
                                                            'address_to_send_official_document_city_you',
                                                            'address_to_send_official_document_prov_you',
                                                            'address_to_send_official_document_postal_code_you',
                                                            'address_to_send_official_document_street_spouse',
                                                            'address_to_send_official_document_city_spouse',
                                                            'address_to_send_official_document_prov_spouse',
                                                            'address_to_send_official_document_postal_code_spouse'],
                                               'conditional': {'address_to_send_official_document_country_you': ['Other', 'address_to_send_official_document_other_country_you'],
                                                               'address_to_send_official_document_country_spouse': ['Other', 'address_to_send_official_document_other_country_spouse'],
                                                               'divorce_take_effect_on': ['specific date', 'divorce_take_effect_on_specific_date']}},
                           'filing_locations': {'required': ['court_registry_for_filing']},
                           }