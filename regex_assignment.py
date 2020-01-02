import re

# user_vehicle_number = "DL 01 AA 1111"

valid_state_codes = ["DL","AR","AP","AS","BR","CG","GA","GJ","HR","HP","JH","KA",
                    "KL","MP","MH","MN","ML","MZ","NL","OD","PB","RJ","SK","TN",
                    "TS","TR","UP","UK","WB","AN","CH","DN","DD","DL","JK","LA",
                    "LD","PY"]
                    
if not re.match("^[A-Z]{2}\s[0-9]{1,2}\s[A-Z]{1,3}\s[0-9]{1,4}$", user_vehicle_number):
    print ("FALSE")
elif user_vehicle_number[0:2] not in valid_state_codes:
    print("FALSE")
else:
    print("TRUE")