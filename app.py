from flask import Flask, request, jsonify
from flask_cors import CROS
from werkzeug.utils import secure_filename
from src import STTstart
from src import textrank
import os

app = Flask(__name__)
CORS(app)
# have to change absolute path
origin_text_path = '/lupin/text/org/'
summary_text_path = '/lupin/text/sum/'
audio_path = '/lupin/CLOVA/audio/'

# receive audio file
@app.route('/receive', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        f = request.files['audio']
        #file_name = str(request.data['file_name'])
        file_name = secure_filename(f.filename)
        # file name : ~~.wav

        f.save('./audio/' + file_name)

        # use CLOVA SPEECH API
        STTstart.STT(file_name)
        # result .txt file (./text/org/[filename].txt)
        # remove original audio file

        # use textrank module
        textrank.rank(file_name)
        # result .txt summary file (./text/sum/[filename]_sum.txt)

        STT_text_file_name = file_name[:-4] + '.txt'
        Sum_text_file_name = file_name[:-4] + '_sum.txt'

        STT_text = open(origin_text_path + STT_text_file_name, 'r', encoding='UTF-8')
        STT_data = STT_text.read()
        Sum_text = open(summary_text_path + Sum_text_file_name, 'r', encoding='UTF-8')
        Sum_data = Sum_text.read()

        res_json = jsonify({"file_name": file_name, "STT_text": STT_data, "Sum_text": Sum_data})

        STT_text.close()
        Sum_text.close()

        #os.remove(audio_path + file_name)
        #os.remove(origin_text_path + STT_text_file_name)
        #os.remove(summary_text_path + Sum_text_file_name)

        return res_json

if __name__ == '__main__':
    app.run(debug=True)