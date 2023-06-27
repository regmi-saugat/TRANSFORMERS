
from pickle import load
from pickle import dump
from collections import Counter

#@ Loading a clean dataset
def load_clean_sentences(filename):
  return load(open(filename, 'rb'))

#@ Save a list of clean sentences to file
def save_clean_sentences(sentences, filename):
  dump(sentences, open(filename, 'wb'))
  print('Saved: %s' % filename)

#@ Creating a frequency table for all words
def to_vocab(lines):
  vocab = Counter()
  for line in lines:
    tokens = line.split()
    vocab.update(tokens)
  return vocab

#@ Removing all words with a frequency below a threshold
def trim_vocab(vocab, min_occurence):
  tokens = [k for k, c in vocab.items() if c>= min_occurence]
  return set(tokens)

#@ Marking all OOV with 'unk' for all lines
def update_dataset(lines, vocab):
  new_lines = list()
  for line in lines:
    new_tokens = list()
    for token in line.split():
      if token in vocab:
        new_tokens.append(token)
      else:
        new_tokens.append('unk')
    new_line = ' '.join(new_tokens)
    new_lines.append(new_line)
  return new_lines

#@ LOADING ENGLISH DATASET
filename = '/content/English.pkl'
lines = load_clean_sentences(filename)
vocab = to_vocab(lines)
print("English Vocabulary: %d" %len(vocab))                                     # Calculate len of vocabulary
vocab = trim_vocab(vocab, 5)                                                    # Reduce Vocabulary
print("New English Vocabulary: %d" % len(vocab))
lines = update_dataset(lines, vocab)                                            # Mark out of vocabulary words
filename = 'english_vocab.pkl'
save_clean_sentences(lines, filename)                                           # Saving the updated dataset
#@ Spot check 
for i in range(20):
  print("Line", i, ":", lines[i])

#@ LOADING FRENCH DATASET
filename = '/content/French.pkl'
lines = load_clean_sentences(filename)                                          # Cleaning the dataset
vocab = to_vocab(lines)                                                         # Calculate vocabulary
print("French Vocabulary: %d" %len(vocab))                                      # Displaying the length of vocabulary
vocab = trim_vocab(vocab, 5)                                                    # Reduce Vocabulary
print("New French Vocabulary: %d" % len(vocab))
lines = update_dataset(lines, vocab)                                            # Mark out of vocabulary words
filename = 'french_vocab.pkl'
save_clean_sentences(lines, filename)                                           # Saving the updated dataset

#@ Spot check 
for i in range(20):
  print("Line", i, ":", lines[i])
