import requests

url = "https://b-graph.facebook.com/graphql"

headers = {
    "host": "b-graph.facebook.com",
    "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
    "x-fb-rmd": "state=URL_ELIGIBLE",
    "priority": "u=0",
    "content-encoding": "gzip",
    "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
    "user-agent": "[FBAN/FB4A;FBAV/578.0.0.40.75;FBBV/1063016987;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/PGFM10;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]",
    "x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "x-zero-f-device-id": "71f99456-d788-4d24-bb2a-15d72db8d46d",
    "x-graphql-request-purpose": "fetch",
    "x-fb-device-group": "5389",
    "x-tigon-is-retry": "False",
    "x-graphql-client-library": "graphservice",
    "content-type": "application/x-www-form-urlencoded",
    "x-fb-net-hni": "310005",
    "x-fb-sim-hni": "310005",
    "authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "x-zero-state": "unknown",
    "x-meta-zca": "empty_token",
    "app-scope-id-header": "ae0e2f86-8601-466d-ad7f-21dbb1a5650e",
    "x-fb-connection-type": "WIFI",
    "x-meta-usdid": "6edc8622-b734-4e7f-ac53-95ccc498d8c7.1789826794.MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEZZd1tilEeLRKTKRBs2f19o5hkfKTcZEy_hSTJIRDajXPTZDAsDzvRPbGcw4QMIaedDrPJ5laOSFpqmNcwUTo6w.MEYCIQDFtUbcknrthfjK9L81PshSSH0bg56AW1g3Zaq7sAFckAIhAPyyI8eKwtv4EiOXJ061oHeehmJ1Z3et0wtUzZA3q0sQ",
    "accept-encoding": "gzip, deflate",
    "x-fb-http-engine": "Tigon/Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "x-fb-conn-uuid-client": "oGTxcIGxLR8NxrbOIFIPyQ==",
}

data = {
    "method": "post",
    "format": "json",
    "server_timestamps": "true",
    "locale": "en_US",
    "purpose": "fetch",
    "fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "11994080421623718916785082173",
    "fb_api_client_context": '{"is_background":false}',
    "variables": '{"params":{"params":"{\"params\":\"{\\\"client_input_params\\\":{\\\"blocked_uids\\\":[],\\\"aac\\\":\\\"Q7jiDQEG0AEPEEknXOBAOYg16bXhwen6uLG9-WXW60jzT-0yQKwNmI6lLMetO7FQFHdG43lXxnPptxUkw8_3OAxr3Gom0ybO-h2d_L4cwbtKK4cWavt237ba5wSvU-s8Tkby8ewhaKQSv_xLpdzKrBqeGzUrHDVnz-pHeTbo0o8mFfa-DdaKLzdBgXFQSboOJsuwOjnKw3c6wTt5wmWruX8ZXH-54pn3b2LJiysYSNiuPgKvJOYUYfXW5fk9f2ac\\\",\\\"sim_phones\\\":[],\\\"aymh_accounts\\\":[{\\\"profiles\\\":{\\\"id\\\":{\\\"is_derived\\\":0,\\\"credentials\\\":[],\\\"account_center_id\\\":\\\"\\\",\\\"profile_picture_url\\\":\\\"\\\",\\\"small_profile_picture_url\\\":null,\\\"notification_count\\\":0,\\\"token\\\":\\\"\\\",\\\"last_access_time\\\":0,\\\"has_smartlock\\\":0,\\\"credential_type\\\":\\\"none\\\",\\\"password\\\":\\\"\\\",\\\"from_accurate_privacy_result\\\":0,\\\"dbln_validated\\\":0,\\\"user_id\\\":\\\"\\\",\\\"name\\\":\\\"\\\",\\\"nta_eligibility_reason\\\":null,\\\"username\\\":\\\"\\\",\\\"account_source\\\":\\\"\\\"}},\\\"id\\\":\\\"\\\"}],\\\"network_bssid\\\":null,\\\"secure_family_device_id\\\":\\\"7e598a69-7070-4e96-a863-edbac0daf248\\\",\\\"attestation_result\\\":{\\\"keyHash\\\":\\\"4a04279c2b8a8ef94d04e66e0d276ceeebf478ccde524ae6baa8bdb6125c91e1\\\",\\\"data\\\":\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiIveWNQTWNUZkUxWnY3MWwyV0FhZzlxcEQxYXU0VHhlZHk2Uml5MTNDTnRZPSIsInVzZXJuYW1lIjoiTm9vcjQwNDQ0NDQifQ==\\\",\\\"signature\\\":\\\"MEUCIQDoyeS+pQd6RPRGaAy5WjJnwuOmILFxNQeeg3b87YzHJAIgCCxd+GHAljE1TskUMGGLykMvwinHlzrxlcar+eKwwTQ=\\\"},\\\"has_granted_read_contacts_permissions\\\":0,\\\"auth_secure_device_id\\\":\\\"\\\",\\\"has_whatsapp_installed\\\":0,\\\"si_device_param_network_info\\\":{\\\"active_subscriptions_info\\\":null,\\\"default_subscription_info\\\":{\\\"network_type\\\":null,\\\"is_data_roaming\\\":1,\\\"is_esim\\\":null,\\\"is_gsm_roaming\\\":0,\\\"is_sim_sms_capable\\\":null,\\\"is_mobile_data_enabled\\\":0,\\\"sim_carrier_id\\\":-1,\\\"sim_carrier_id_name\\\":null,\\\"sim_state\\\":5,\\\"sim_operator\\\":\\\"310005\\\",\\\"sim_operator_name\\\":\\\"Verizon+Wireless\\\",\\\"signal_strength\\\":null,\\\"group_id_level_1\\\":null,\\\"network_operator\\\":\\\"310005\\\"},\\\"is_airplane_mode\\\":0,\\\"is_active_network_cellular\\\":0,\\\"is_device_sms_capable\\\":1,\\\"sim_count\\\":1,\\\"is_wifi\\\":1},\\\"password\\\":\\\"#PWD_FB4A:2:1789823223:ARiUgK3YFSyW1QjG3ckAAa5m3cUt\\/iGAvVTXxEo4P58g4bYgEh9ZDjk\\/RG0SjESSyEZO6JqD9Lqoei7eqhJfZDjnKI8MiwwlX7Gf1cuzfYR0QmPksVdTZY0hwmqvUJ3SiMOcSfxmkyFaVyi6wAyQ++vYOFbwKR3kRN386mhBLRkeGlwMjygrub39lE2h7JI6o4jX05Eizh0dzWstSTpwCyqIygUKwIUzqx6\\/FjQ7cQmdWCJv5CWy3WJK90LPh4lfAywWVnbmLtW4LfdySaujPU0W6sC4VvlcTzDt4yUYtQg\\/zDbCfs4TGfvzdKsuCo38s5cnDid1qxsYKE8olQkluEdaB3xqMaiXeiaeaBzWkO8e+adKAMRs5a0fxWGvsVaaI6rr5r2TJBIU5VoUpgDsrfnE\\\",\\\"sso_token_map_json_string\\\":\\\"\\\",\\\"block_store_machine_id\\\":null,\\\"cloud_trust_token\\\":null,\\\"event_flow\\\":\\\"login_manual\\\",\\\"password_contains_non_ascii\\\":\\\"false\\\",\\\"sim_serials\\\":[],\\\"client_known_key_hash\\\":\\\"\\\",\\\"sso_accounts_auth_data\\\":[],\\\"encrypted_msisdn\\\":\\\"\\\",\\\"has_granted_read_phone_permissions\\\":0,\\\"app_manager_id\\\":\\\"null\\\",\\\"should_show_nested_nta_from_aymh\\\":0,\\\"device_id\\\":\\\"ae0e2f86-8601-466d-ad7f-21dbb1a5650e\\\",\\\"zero_balance_state\\\":\\\"init\\',\`login_attempt_count\`:1,\\\"machine_id\\\":\\\"\\\",\\\"flash_call_permission_status\\\":{\\\"READ_PHONE_STATE\\\":\\\"DENIED\\\",\\\"READ_CALL_LOG\\\":\\\"DENIED\\\",\\\"ANSWER_PHONE_CALLS\\\":\\\"DENIED\\\"},\\\"accounts_list\\\":[],\\\"gms_incoming_call_retriever_eligibility\\\":\\\"not_eligible\\\",\\\"family_device_id\\\":\\\"71f99456-d788-4d24-bb2a-15d72db8d46d\\\",\\\"fb_ig_device_id\\\":[],\\\"device_emails\\\":[],\\\"try_num\\\":1,\\\"lois_settings\\\":{\\\"lois_token\\\":\\\"\\\"},\\\"event_step\\\":\\\"home_page\\\",\\\"headers_infra_flow_id\\\":\\\"f73fa3e2-666c-40f4-aa53-a6ef96db6c70\\\",\\\"openid_tokens\\\":{},\\\"contact_point\\\":\\\"Noor4044444\\\"},\\\"server_params\\\":{\\\"should_trigger_override_login_2fa_action\\\":0,\\\"is_from_logged_out\\\":0,\\\"should_trigger_override_login_success_action\\\":0,\\\"login_credential_type\\\":\\\"none\\\",\\\"server_login_source\\\":\\\"login\\\",\\\"waterfall_id\\\":\\\"753ff83e-76bf-4c3f-8b0e-ab05b448c93a\\\",\\\"two_step_login_type\\\":\\\"one_step_login\\\",\\\"login_source\\\":\\\"Login\\\",\\\"is_platform_login\\\":0,\\\"pw_encryption_try_count\\\":1,\\\"login_entry_point\\\":\\\"logged_out\\\",\\\"INTERNAL__latency_qpl_marker_id\\\":36707139,\\\"is_from_aymh\\\":0,\\\"offline_experiment_group\\\":\\\"caa_iteration_v6_perf_fb_2\\\",\\\"is_from_landing_page\\\":0,\\\"left_nav_button_action\\\":\\\"BACK\\\",\\\"password_text_input_id\\\":\\\"eimyf4:56\\\",\\\"is_from_empty_password\\\":0,\\\"is_from_msplit_fallback\\\":0,\\\"ar_event_source\\\":\\\"login_home_page\\\",\\\"username_text_input_id\\\":\\\"eimyf4:55\\\",\\\"layered_homepage_experiment_group\\\":null,\\\"device_id\\\":\\\"ae0e2f86-8601-466d-ad7f-21dbb1a5650e\\\",\\\"login_surface\\\":\\\"login_home\\\",\\\"INTERNAL__latency_qpl_instance_id\\\":87783059200771,\\\"reg_flow_source\\\":\\\"lid_landing_screen\\\",\\\"is_caa_perf_enabled\\\":1,\\\"credential_type\\":\\\"password\\\",\\\"is_from_password_entry_page\\\":0,\\\"caller\\\":\\\"gslr\\\",\\\"family_device_id\\\":\\\"71f99456-d788-4d24-bb2a-15d72db8d46d\\\",\\\"is_from_assistive_id\\\":0,\\\"access_flow_version\\\":\\\"pre_mt_behavior\\\",\\\"is_from_logged_in_switcher\\\":0}}\"}","bloks_versioning_id":"a0a64048203112daaec7daec70feca998f2220cd551309e234f9d678fe5443bc","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"3","nt_context":{"using_white_navbar":true,"styles_id":"0c28c2fb31d4e397db6494e82e716e1b","pixel_ratio":3,"is_push_on":true,"is_flipper_enabled":false,"android_device_performance_class":null,"debug_tooling_metadata_token":null,"gpu_memory_mb":null,"theme_params":[{"value":["three_neutral_gray"],"design_system_name":"XMDS"},{"value":[],"design_system_name":"FDS"}],"bloks_version":"a0a64048203112daaec7daec70feca998f2220cd551309e234f9d678fe5443bc","android_os_api_level":28}}',
    "fb_api_analytics_tags": '["GraphServices"]',
    "client_trace_id": "a19e9103-a255-4a7c-b1e3-3d1a18e7bf52",
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)
