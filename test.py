import requests

#file_name = '샘플_1.wav'
#
#res = requests.post('http://15.164.58.213:5000/test',  json={'test':'asd'})
#print(res.json())

#res2 = requests.get('http://15.164.58.213:5000/status')
#print(res2)

#values={'file_name': file_name}
#upload = {'audio': open('./sample/sample_1.wav', 'rb')}
#res = requests.post('http://15.164.58.213:5000/receive', files=upload).json()
#res = requests.post('http://15.164.58.213:5000/test', files=upload).json()
#res = requests.post('http://192.168.42.148:5000/receive', files=upload).json()
values={'path': 'https://lupin-public-bucket.s3.ap-northeast-2.amazonaws.com/40413c289b334263228bed2f8ad48852', 'filename': 'sample_1.wav'}
res = requests.post('http://15.164.58.213:5000/path', json=values)

print(res.json())
#f=open('reseponse', 'w', encoding='UTF-8')
#f.write(str(res))
#f.close()