
import pickle
from pickle import dump

#@ Define the function to load the file into memory
def load_doc(filename):
  file = open(filename, mode='rt', encoding='utf-8')                            # Open the file as read only mode
  text = file.read()                                                            # Read all text from the file
  file.close()                                                                  # Closing the file
  return text

#@ Split the loaded document into the sentences
def to_sentences(doc):
  return doc.strip().split("\n")

#@ The shortest and longest sentences length
def sentence_lengths(sentences):
  lengths = [len(s.split()) for s in sentences]
  return min(lengths), max(lengths)

#@ Cleaning lines
import re
import string
import unicodedata

def clean_lines(lines):
  cleaned = list()
  re_print = re.compile('[^%s]' % re.escape(string.printable))                  # Preparing regex for char filtering
  table = str.maketrans('', '', string.punctuation)                             # Prepare translation table for removing punctuation
  for line in lines:
    line = unicodedata.normalize('NFD', line).encode('ascii', 'ignore')         # Normalize unicode characters
    line = line.decode('UTF-8')
    line = line.split()                                                         # Tokenize on white space
    line = [word.lower() for word in line]                                      # Convert to lowercase
    line = [word.translate(table) for word in line]                             # Remove punctuation from each token
    line = [re_print.sub('', w) for w in line]                                  # Remove non-printable chars from each token
    line = [word for word in line if word.isalpha()]                            # Remove tokens with numbers in them
    cleaned.append(' '.join(line))                                              # Storing as string
  return cleaned

#@ Loading the English Data
filename = '/content/drive/MyDrive/Machine Translation/europarl-v7.fr-en.en'
doc = load_doc(filename)
sentences = to_sentences(doc)
minlen, maxlen = sentence_lengths(sentences)
print("English data: sentences=%d, min=%d, max=%d" % (len(sentences),
                                                      minlen, maxlen))
cleanf=clean_lines(sentences)
filename = 'English.pkl'
outfile = open(filename, 'wb')
pickle.dump(cleanf, outfile)
outfile.close()
print(filename, 'saved')


#@ Loading the French Data
filename = '/content/drive/MyDrive/Machine Translation/europarl-v7.fr-en.fr'
doc = load_doc(filename)
sentences = to_sentences(doc)
minlen, maxlen = sentence_lengths(sentences)
print("French data: sentences=%d, min=%d, max=%d" % (len(sentences),
                                                      minlen, maxlen))
cleanf=clean_lines(sentences)
filename = 'French.pkl'
outfile = open(filename, 'wb')
pickle.dump(cleanf, outfile)
outfile.close()
print(filename, 'saved')
