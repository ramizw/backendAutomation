import requests

cookie = {'visit-month': 'March'}
response = requests.get('http://rahulshettyacademy.com', cookies=cookie, timeout=1)
print(response.history)  # history checks if there is any re-directions in the endpoints
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'March'})

res = requests.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(res.text)

res1 = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(res1.text)

# Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"  # {petId} = 9843217
files = {'file': open('Ramizz.jpg', 'rb')}
r1 = requests.post(url, files=files)
print(r1.status_code)
print(r1.text)
