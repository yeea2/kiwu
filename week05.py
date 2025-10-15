
import requests

url = f"https://wttr.in/jeju?format=%C+%t"
# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
# url = f"https://wttr.in/incheon?&0&Q"
response = requests.get(url)
print(response)
=======

import requests

# Moon day(%m) + Sunrise(%S) + 현재 날씨 요약(%c+%t)
url = url = "https://wttr.in/seoul?format=Moon:%m+Sunrise:%S+LocalTime:%l"

response = requests.get(url)

>>>>>>> 54d0e82970da16583be6eb369276eb2a4a007a0a
print(response.status_code)
if response.status_code == 200:
    print(response.text.strip())
else:

    print(f"상태 코드 : {response.status_code}")
=======
    print(f"상태 코드 : {response.status_code}")

#202308021 이예원
>>>>>>> 54d0e82970da16583be6eb369276eb2a4a007a0a
