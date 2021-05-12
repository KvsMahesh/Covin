from cowin_api import CoWinAPI

# cowin = CoWinAPI()

# states = cowin.get_states()
# # print(states)

# state_id = '2'
# # cowin = CoWinAPI()
# districts = cowin.get_districts(state_id)
# print(districts)
# district_id = '395'
# date = '07-05-2021'  # Optional. Takes today's date by default
# # Optional. By default returns centers without filtering by min_age_limit
# min_age_limit = 18

# cowin = CoWinAPI()
# available_centers = cowin.get_availability_by_district(
#     district_id, date, min_age_limit)
# print(available_centers)
pin_code = "110003"
date = '06-05-2021'  # Optional. Default value is today's date
# Optional. By default returns centers without filtering by min_age_limit
min_age_limit = 45

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_pincode(
    pin_code, date, min_age_limit)
print(available_centers)

# new_date = date[8]+date[9]+'-'+date[5] +date[6]+'-'+date[0]+date[1]+date[2]+date[3]
# print(new_date)
# print(date)
# date = new_date
# print(type(date))
