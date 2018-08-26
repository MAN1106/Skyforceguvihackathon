import profanity as pf
import re

a = input()


text_file = open("toxic.txt", "r")
toxic = text_file.readlines()

text_file.close()

text_file = open("severe_toxic.txt", "r")
severe_toxic = text_file.readlines()

text_file.close()

text_file = open("threat.txt", "r")
threat = text_file.readlines()

text_file.close()

text_file = open("insult.txt", "r")
insult = text_file.readlines()

text_file.close()

text_file = open("identity_hate.txt", "r")
identity_hate = text_file.readlines()

text_file.close()

text_file = open("obsene.txt", "r")
obsene = text_file.readlines()

text_file.close()
print(insult)
ans="The Comment is :"
b= re.split("[^A-Za-z]+",a)
for b1 in b:
    print (b1)
    if (b1+'\n') in toxic:
        ans+="Toxic,"
    if (b1+'\n') in severe_toxic:
        ans+="Severe_Toxic,"
    if (b1+'\n') in obsene:
        ans+="Obsene,"
    if (b1+'\n') in threat:
        ans+="Threat,"
    if (b1+'\n') in insult:
        ans+="Insult,"
    if (b1+'\n') in identity_hate:
        ans+="Identity_hate,"
print(ans)
