#pip install "camelot-py[cv]"
#pip install deepdiff


from http import client
from deepdiff import DeepDiff
import camelot

client_Data = {"id": "2", "first_name": "JITENDER", "middle_name": " ", "last_name": "DAGAR", "email": "athulk@webandcrafts.in",
                "country_code": "+91", "phone": "9072482174", "sex": "male", "country_id": "1", "language_id": "1", "dob": "1999-10-02", "height": "178",
                "weight": "142", "address": "address", "city": "Thrissure", "state": "kerala", "pincode": "679865", "blood_group": "A+ve", "ethnicity": "",
                "marital_status": "", "occupation": "", "longitude": "", "latitude": ""}

tables2=camelot.read_pdf('GFX0202827-pages-2.pdf', flavor='stream', table_areas=['35,750,550,343'], pages = '1')

#print(tables2[0].parsing_report)

df2=tables2[0].df
df2.columns = ['0','1']
dictt = df2.set_index('0')['1'].to_dict()
#print(dictt)

lab_data = dict((k.lower(), v.lower()) for k, v in dictt.items())
client_Data = dict((k.lower(),v.lower()) for k,v in client_Data.items())

print(client_Data)
print(lab_data)

diff = DeepDiff(client_Data, lab_data)
#print(diff)

print(lab_data.get('patient name','').upper())

if(client_Data.get('first_name','')+client_Data.get('middle_name','')+client_Data.get('last_name','')==lab_data.get('patient name','')): print("Names Matched")
if(client_Data.get('weight',0)==lab_data.get('weight (kg)')): print("Weight matched")
if(client_Data.get('height',0)==lab_data.get('height (cm)')): print("Height matched")
if(client_Data.get('sex',0)==lab_data.get('gender')): print("Gender matched")



# OUTPUT

# {'id': '2', 'first_name': 'jitender', 'middle_name': ' ', 'last_name': 'dagar', 'email': 'athulk@webandcrafts.in', 'country_code': '+91', 'phone': '9072482174', 'sex': 'male', 'country_id': '1', 'language_id': '1', 'dob': '1999-10-02', 'height': '178', 'weight': '142', 'address': 'address', 'city': 'thrissure', 'state': 'kerala', 'pincode': '679865', 'blood_group': 'a+ve', 'ethnicity': '', 'marital_status': '', 'occupation': '', 'longitude': '', 'latitude': ''}
# {'patient name': 'jitender dagar', 'age (years)': '35', 'weight (kg)': '142', 'gender': 'male', 'height (cm)': '178', 'patient id': 'vi2203092576', 'test id': 'nmc-wl01', 'sample type': 'saliva', 'sample collection date': '21/01/2022', 'report generation date': '12/03/2022', 'referred by (doctor)': 'vieroots wellness solution pvt ltd', 'referred by (hospital)': 'n/a'}
# JITENDER DAGAR
# Names Matched
# Weight matched
# Height matched
# Gender matched