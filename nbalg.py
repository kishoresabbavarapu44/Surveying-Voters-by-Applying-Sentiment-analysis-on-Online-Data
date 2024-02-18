import string
from collections import Counter
pos_text_file = open("data/positivef.txt", "r")
neg_text_file = open("data/negativef.txt", "r")
ppos = 0.5
pneg = 0.5
count1 = 0
count2 = 0
words1 = []
words2 = []
frequency1 = {}
frequency2 = {}
count_word = 0
x = 0
a = 0
prob1 = {}
prob2 = {}
def read_words(pos_text_file):
  global count1
  global words1
  with open('data/positivef.txt', 'r') as file_object:
    for line in file_object:
      words1 += line.split()
  return words1
words_list = read_words(pos_text_file)
count_each_word = Counter(words_list)
count1 += len(count_each_word)
def read_words(neg_text_file):
  global count2
  global words2
  with open('data/negativef.txt', 'r') as file_object:
    for line in file_object:
      words2 += line.split()
  return words2
words_list = read_words(neg_text_file)
count_each_word = Counter(words_list)
count2 += len(count_each_word)
vocab_size = count1 + count2
ppos = count1 / vocab_size
pneg = count2 / vocab_size
for word in words1[: ]: 
  count_word = frequency1.get(word, 0)
  frequency1[word] = count_word + 1
  word_prob = (frequency1[word] + 1) / (count1 + vocab_size)
  prob1[word] = word_prob
for word in words2[: ]: 
  count_word = frequency2.get(word, 0)
  frequency2[word] = count_word + 1
  word_prob = (frequency2[word] + 1) / (count1 + vocab_size)
  prob2[word] = word_prob
test_data = open('data/newfile.txt', 'r')
positive_count = 0
negative_count = 0
total = 0
positive_percent = 0
negative_percent = 0
lines = test_data.readlines()
for line in lines:
  a = 0
  b = 0
  pos_sum = ppos
  c = 0
  d = 0
  neg_sum = pneg
  words = line.split()
  for word in words:
    if word in prob1:
      a = prob1[word]
      pos_sum = pos_sum * a
    else :
      b = 1 / (count1 + vocab_size)
      pos_sum = b * pos_sum
  words = line.split()
  for word in words:
    if word in prob2:
      c = prob2[word]
      neg_sum = neg_sum * c
    else :
      d = 1 / (count2 + vocab_size)
      neg_sum = d * neg_sum
  if (pos_sum > neg_sum): 
    positive_count += 1
  else :
    negative_count += 1
total = positive_count + negative_count
positive_percent = (positive_count / total) * 100
negative_percent = (negative_count / total) * 100
print("Results for the party are:")
print("Positive percentage for test data is", positive_percent)
print("Negative percentage for test data is", negative_percent)
