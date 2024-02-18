import re,string
a=''
def strip_links(text):
 global a
 link_regex =re.compile('((https?):((//)|(\\\\))|1|2|3|4|5|6|7|8|9|0|RT+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)',re.DOTALL)
 stringwithouthash = re.sub(r'#\w+ ?', '', text)
 stringwithoutlink = re.sub(r'http\S+', '',text)
 links = re.findall(link_regex, text)
 for link in links:
     text = text.replace(link[0], ', ')
 return text
def strip_all_entities(text):
 global a
 entity_prefixes = ['@','#']
 for separator in string.punctuation:
     if separator not in entity_prefixes :
         text = text.replace(separator,' ')
         words = []
     for word in text.split():
         word = word.strip()
         if word:
                if word[0] not in entity_prefixes:
                   words.append(word)
                   a=' '.join(words)
 print (a)
 return a
myfile = open("data/janasena_stream.csv","r",encoding='utf-8')
lines = myfile.readlines()
for line in lines:
    strip_all_entities(strip_links(line))
