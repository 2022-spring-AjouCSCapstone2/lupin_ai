# Lupin AI

## STT

#### STTstart.py

`python STTstart.py`

- 실행 시 ./audio 디렉토리의 모든 파일에 대해서 CLOVA SPEECH API 요청을 보내고 이 결과값을 ./text/org 디렉토리에 저장됨. 이후 변환된 audio 파일은 삭제 처리
  
  `./audio/sample1.wav`
  
  `./text/org/sample1.txt`
- 확장자만 바뀌고, 파일 이름은 그대로 유지됨

### 주의사항

서버에 적용 시 STTstart.py의 audio_path, text_path를 절대경로로 변경해주세요.
반드시 문자열 맨 뒤에 / 넣어야합니다.

ex) audio_path = '/CLOVA/audio/'

ex) text_path = '/CLOVA/text/org/'

---

## textrank

### textrank.py

`python textrank.py`

- ./text/org 디렉토리에 저장된 STT 결과 파일에 대해서 textrank를 수행 후 ./text/sum 디렉토리에 저장
- 파일은 키워드와 문장 요약으로 구성됨
- 동일 파일 명, 맨 뒤에 \_sum 추가된 이름으로 저장

### requirements

`pip install kss konlpy`

### 주의사항

서버에 적용 시 textrank.py의 original_txt_path, summary_txt_path를 절대경로로 변경해주세요.
반드시 문자열 맨 뒤에 / 넣어야합니다.

ex) original_txt_path = '/CLOVA/text/org/'

ex) summary_txt_path = '/CLOVA/text/sum/'

---

## sample

테스트에 사용된 예시

- /sample 참고
