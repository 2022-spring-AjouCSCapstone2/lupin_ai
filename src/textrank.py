from konlpy.tag import Komoran
import kss
from summarizer import KeysentenceSummarizer
from summarizer import KeywordSummarizer
import itertools
from pathlib import Path
import os

original_txt_path = '/lupin/text/org/'
summary_txt_path = '/lupin/text/sum/'

komoran = Komoran()

stopwords = []
f = open('/lupin/src/stopwords.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    line = line.replace('\t', ' ').strip()
    stopwords.append(line)
f.close()
stopwords = set(stopwords)

def komoran_tokenizer(sent):
    words = komoran.pos(sent, join=True)
    words = [w.split('/')[0] for w in words if (('/NNG' in w or '/NNP' in w) and w.split('/')[0] not in stopwords)]
    return words

def getsummarize(sents):
    summarizer = KeysentenceSummarizer(
        tokenize = komoran_tokenizer,
        min_sim = 0.5,
        verbose = True
        )
    keysents = summarizer.summarize(sents, topk=30)
    keysents.sort(key = lambda x : x[0])
    return list(itertools.chain(*keysents))[2::3]

def getkeyword(sents):
    summarizer = KeywordSummarizer(tokenize=komoran_tokenizer, min_count=2, min_cooccurrence=1)
    keywords = summarizer.summarize(sents, topk=30)
    return list(itertools.chain(*keywords))[0::]

#if __name__ == '__main__':
def rank(file_name):

    #txt_flie_list = os.listdir(original_txt_path)

    # file_name is [~~.wav]
    org_txt_file_path = original_txt_path + file_name[:-4] + '.txt'


    #for i in txt_flie_list:

        #content = Path(original_txt_path + i).read_text().replace('\n', ' ')
        #sents = kss.split_sentences(content)

        #t = open(summary_txt_path + i[:-4] + '_sum.txt', 'w', encoding='UTF-8')
        #t.write('------- keywords -------\n')
        #t.write(str(getkeyword(sents)))
        #check = 0
        #for j in getkeyword(sents):
            #if check % 2 == 0:
                #t.write(str(j) +'\n')
            #check += 1
        #t.write('\n\n')
        #t.write('------- summary -------\n')
        #t.write(str(getsummarize(sents)))
        #for k in getsummarize(sents):
            #t.write(str(k)+ '\n')
        #t.close()
        #print(getsummarize(sents))
        #print(getkeyword(sents))

    content = Path(org_txt_file_path).read_text(encoding='UTF-8').replace('\n', ' ')
    sents = kss.split_sentences(content)

    t = open(summary_txt_path + file_name[:-4] + '_sum.txt', 'w', encoding='UTF-8')
    t.write('------- keywords -------\n')
    #t.write(str(getkeyword(sents)))
    check = 0
    for j in getkeyword(sents):
        if check % 2 == 0:
            t.write(str(j) +'\n')
        check += 1
    t.write('\n\n')
    t.write('------- summary -------\n')
    #t.write(str(getsummarize(sents)))
    for k in getsummarize(sents):
        t.write(str(k)+ '\n')
    t.close()