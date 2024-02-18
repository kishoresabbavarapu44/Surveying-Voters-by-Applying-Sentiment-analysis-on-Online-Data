import string,re
t=''
pos_text_file = open("data/positivef.txt", "r")
pwords=[]
for pword in pos_text_file:
	pwords.append(pword)
pwords[:]=[pword.rstrip('\n') for pword in pwords]
neg_text_file = open("data/negativef.txt", "r")
nwords=[]
for nword in neg_text_file:
	nwords.append(nword)
nwords[:]=[nword.rstrip('\n') for nword in nwords]
positive_tweet_count=0
negative_tweet_count=0
neutral_tweet_count=0
positive_percent=0
negative_percent=0
def add_one_pos():
	global pos
	pos +=1
def add_one_neg():
        global neg
        neg +=1
myfile = open("data/jsptf.txt","r")
lines = myfile.readlines()
for line in lines:
        pos=0
        neg=0
        neutral=0
        tokens = line.split()
        for token in tokens:
                if token in pwords:
                        add_one_pos()
                elif token in nwords:
                        add_one_neg()
                else:
                        neutral+=1
        if (pos>neg) & (pos>=neutral):
                positive_tweet_count +=1
                p=[]
                p.append(tokens)
                a=' '.join(tokens)
        elif (neg>pos) & (neg>=neutral):
                negative_tweet_count +=1
                n=[]
                n.append(tokens)
                c=' '.join(tokens)
        else:
                if(pos>neg):
                        positive_tweet_count +=1
                        pp=[]
                        pp.append(tokens)
                        b=' '.join(tokens)
                elif(neg>pos):
                        negative_tweet_count +=1
                        nn=[]
                        nn.append(tokens)
                        d=' '.join(tokens)
                else:
                        neutral_tweet_count+=1
print('no of positive tweets',positive_tweet_count)
print('no of negative tweets',negative_tweet_count)
print('no of neutral tweets',neutral_tweet_count)
subtotal=positive_tweet_count+negative_tweet_count+neutral_tweet_count
print('subtotal tweets',subtotal)
positive_percent=(positive_tweet_count/subtotal)*100
print('positive percentage is:',positive_percent)
negative_percent=(negative_tweet_count/subtotal)*100
print('negative percentage is:',negative_percent)
if positive_tweet_count > negative_tweet_count:
        print(positive_percent,'% People are positive')
else:
        print(negative_percent,'% People are negative')
