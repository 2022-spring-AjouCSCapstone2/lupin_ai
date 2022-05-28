import requests

file_name = '샘플_1.wav'

#values={'file_name': file_name}
upload = {'audio': open('./sample/sample_1.wav', 'rb')}
res = requests.post('http://15.164.58.213:5000/receive', files=upload).json()

print(res)
f=open('reseponse', 'w', encoding='UTF-8')
f.write(str(res))
f.close()