punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(word):
    new_word = ''
    for letter in word:
        if letter in punctuation_chars:
            new_word += ''
        else:
            new_word += letter 
    return new_word

def get_pos(sentence):
    score = 0
    word_list = sentence.split()
    for word in word_list:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            score += 1
    return score

def get_neg(sentence):
    score = 0
    word_list = sentence.split()
    for word in word_list:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            score += 1
    return score

def get_net_score(pos_score, neg_score):
    net_score = pos_score - neg_score
    return net_score
        
resulting_data = open("resulting_data.csv","w")
resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resulting_data.write("\n")

with open("project_twitter_data.csv") as twitter_data:
    twitter_data.readline()
    positive_score = 0
    negative_score = 0
    net_score = 0
    word_list = []
    for line in twitter_data:
        word_list = line.strip().split(',')
        positive_score = get_pos(line)
        negative_score = get_neg(line)
        net_score = get_net_score(positive_score, negative_score)
        resulting_data.write(word_list[-2])
        resulting_data.write(", ")
        resulting_data.write(word_list[-1])
        resulting_data.write(", ")
        resulting_data.write(positive_score)
        resulting_data.write(", ")
        resulting_data.write(negative_score)
        resulting_data.write(", ")
        resulting_data.write(net_score)
        resulting_data.write("\n")
