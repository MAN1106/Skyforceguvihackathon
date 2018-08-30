import nltk
import pickle

'''s= " HCL G Sda"
sen = nltk.word_tokenize(s)
print(sen)
part = nltk.pos_tag(sen)
print (part)'''
'''
def learnDefault(sen):
    word = nltk.word_tokenize(sen)
    tagger = nltk.DefaultTagger("NN")
    pos = tagger.tag(word)
    print ('1')
    print (pos)
    aa

def learnE(sen):
    custom = [(r'.*ing$','Adjective'),
              (r'.*ly$','Adverb'),
              (r'.*ion$','Noun'),
              (r'.*ate$|.*en|is$','Verb')]
    tagger = nltk.RegexpTagger(custom)
    word = nltk.word_tokenize(sen)
    pos = tagger.tag(word)
    print ('2')
    print(pos)

def learnL(sen):
    mapping = {'.':'.','place':'NN','on':'IN','earth':'NN','Mysore':'NNP','is':'VBZ','an':'DT','amazing':'JJ'}
    tagger = nltk.UnigramTagger(model = mapping)
    word = nltk.word_tokenize(sen)
    pos = tagger.tag(word)
    print ('3')
    print(pos)
'''
def sampleData():
    return ["Palani is a Devotional place on earth. I Have visited palani 2 times",
            "Devakottai is a Traditional place on earth. I Have visited many times"
            "Pudukkottai is an amazing place on earth. I live there"
            "Chennai is an amazing place on earth, which is a capital of TN"]

def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        pos = nltk.pos_tag(nltk.word_tokenize (sent))
        for tag in pos:
            value= tag[0]
            pos = tag[1]
            dictionary[value]=pos
    return dictionary

def save(tagger,filename):
    fileH = open(filename,"wb")
    pickle.dump(tagger,fileH)
    fileH.close()

def savet(filename):
    tagger = nltk.UnigramTagger (model = buildDictionary())
    save(tagger,filename)

def load(filename):
    return pickle.load(open(filename,'rb'))


sen = "Mysore is an amazing place on earth. I Have visited mysore 10 times"
filename = "mytagger.pickle"

savet(filename)
mytagger= load(filename)
print(mytagger.tag(nltk.word_tokenize (sen)))

'''learnDefault(sen)
learnE(sen)
learnL(sen)'''
