import requests

TOKEN = "bonoja-python-course"

# DOCUMENTATION: https://docs.pixe.la/
PIXELA_ENDPOINT = "https://pixe.la/v1/users/bonoja8678"

# PIXEL_PARAMS = {
#   "date": "20221205",
#   "quantity": "3"
# }

HEADERS = { 'X-USER-TOKEN': TOKEN }

r = requests.delete(url=PIXELA_ENDPOINT, headers=HEADERS) #, json=PIXEL_PARAMS)
print(r.text)
