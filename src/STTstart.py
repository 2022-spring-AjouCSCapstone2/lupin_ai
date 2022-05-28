import requests
import json
import os

audio_path = '/lupin/audio/'
text_path = '/lupin/text/org/'

class ClovaSpeechClient:
    # Clova Speech invoke URL(have to change key)
    invoke_url = 'https://clovaspeech-gw.ncloud.com/external/v1/2806/850d6ee87127dfa221485246c26d4c069fa31beca079cabf609fcf7a8f08dbab'
    # Clova Speech secret key(have to change key)
    secret = '5fceed12cb33458ebc2d20bb2f84f7d2'

    def req_url(self, url, completion, callback=None, userdata=None, forbiddens=None, boostings=None, wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'url': url,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/url',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_object_storage(self, data_key, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                           wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'dataKey': data_key,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/object-storage',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                   wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            'media': open(file, 'rb'),
            'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
        }
        response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
        return response

#if __name__ == '__main__':
def STT(audio_file_name):

    #audio_flie_list = os.listdir(audio_path)
    audio_file_path = audio_path + audio_file_name
    #for i in audio_flie_list:

        # res = ClovaSpeechClient().req_url(url='http://example.com/media.mp3', completion='sync')
        # res = ClovaSpeechClient().req_object_storage(data_key='data/media.mp3', completion='sync')
        
        #res = ClovaSpeechClient().req_upload(file = audio_path + i, completion='sync')
        #json_temp = res.json()
        #res_txt = json_temp.get("text")

        #f = open(text_path + i[:-4] + '.txt', 'w')
        #f.write(str(res_txt))
        #f.close()

        #os.system('rm ' + audio_path + i)

        #print(res.text)
    res = ClovaSpeechClient().req_upload(file = audio_file_path, completion='sync')
    json_temp = res.json()
    res_txt = json_temp.get("text")

    f = open(text_path + audio_file_name[:-4] + '.txt', 'w', encoding='UTF-8')
    f.write(str(res_txt))
    f.close()