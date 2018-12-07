#Create by Yumeng Yang on 9/18/2018

import os
import operator

def preprocess(src, output): 
	import re
	from nltk.stem import PorterStemmer
	from nltk.tokenize import sent_tokenize, word_tokenize
	from nltk import word_tokenize
	from nltk.corpus import stopwords

	stop = set(stopwords.words('english'))
	ps = PorterStemmer()

	files = os.listdir(src)
	for file in files:
		result = []
		with open(src + "/" + file, "r", encoding='utf-8') as fin:
			punctuations = '''!()-[]{},;:'"\,`<>./?@#$%^&*_~'''
			lines = fin.readlines()
			for line in lines:
				words = []
				line = line.strip('\n')
				words += line.split(' ')
				strp = ''
				for word in words: 
					if word in punctuations:
						continue;
					if word.startswith('<'):
						continue;
					if '.' in word:
						continue;
					# if word.endswith(','):
					# 	wordnocomma = re.sub("[,]", "", word)
					currword = re.sub("[0-9/(),']", "", word)
					newword = re.sub("[-]", " ", currword)
					if newword.lower() in stop: 
						continue;
					newword = ps.stem(newword.lower())
					if len(newword) <= 2:
						continue;
					if newword in stop:
						continue;
					strp = ''.join(newword)
					result.append(strp)
					result.append(' ')
		# print(result)
		fout = open("./" + output + "/" + file, 'a')
		fout.writelines(result)

if __name__ == '__main__':
	doc = '../cranfieldDocs'
	preprocessed_doc = '../preprocessed_doc'
	preprocess(doc, preprocessed_doc)

