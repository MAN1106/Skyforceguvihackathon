import nltk
import re
import pandas
import csv
def ap():
    df=pandas.read_csv("train.csv")
    df1=pandas.read_csv("en.csv")
    #print (df['comment_text'])

    df3=df1['en_bad_words'].tolist()
    df1=df['toxic']
    df2=df['severe_toxic']
    df4=df['obscene']
    df5=df['insult']
    df6=df['threat']
    df7=df['identity_hate']
    toxic =set()
    severe_toxic =set()
    hate =set()
    threat =set()
    identity_hate =set()
    insult =set()
    count = 0
    

    for d in df['comment_text']:
        b= re.split("[^A-Za-z]+",d)    
        count+=1
        
        if count>159550:
            count-=1000
        if df1[count]==1:
            for b1 in b:
                if b1 in df3:               
                    toxic.add(b1)
            
        if df2[count]==1:
            for b1 in b:
                if b1 in df3:
                    severe_toxic.add(b1)            
        if df4[count]==1:
            for b1 in b:
                if b1 in df3:
                    hate.add(b1)
        if df5[count]==1:
            for b1 in b:
                if b1 in df3:
                    insult.add(b1)            
        if df6[count]==1:
            for b1 in b:
                if b1 in df3:
                    threat.add(b1)            
        if df7[count]==1:
            for b1 in b:
                if b1 in df3:
                    identity_hate.add(b1)            
        
    
    with open('toxic.txt', 'w+') as filehandle:
        for t in toxic:
            filehandle.write("%s\n" % t)
    with open('severe_toxic.txt', 'w+') as filehandle:
        for t in severe_toxic:
            filehandle.write("%s\n" % t)
    with open('obsene.txt', 'w+') as filehandle:
        for t in hate:
            filehandle.write("%s\n" % t)
    with open('insult.txt', 'w+') as filehandle:
        for t in insult:
            filehandle.write("%s\n" % t)
    with open('threat.txt', 'w+') as filehandle:
        for t in threat:
            filehandle.write("%s\n" % t)
    with open('identity_hate.txt', 'w+') as filehandle:
        for t in identity_hate:
            filehandle.write("%s\n" % t)
            
ap()
