import random
import sys
import nltk
from rake_nltk import Rake
import socket
from nltk.stem import PorterStemmer
r=Rake()
pst=PorterStemmer()
#initialize the questions 
mytext='''major':['math','art','physics','computer science'],
'birthday':['october 10th 2000','today,june 17th 1997'],
'food':['pudding','cake','spaghetti','Kung pao chicken'],
'drink':['blood','7 up','Pepsi','orange juice'],
'sport':['soccer','badminton','basketball','archery'],
'color':['red','black','green','yellow'],
'weather':['sunny','snowy','rainy'],
'breakfast':['burger','cereal','corn','bread'],
'homework':['I haven''t finished it yet','Yesterday','uhhh, let''s change a topic'],
'sleep':['at 12:00 pm','at 3:00 am','I have sleep disorder yesterday...'],
'gym':['last month','yesterday','a week ago, I guess....'],
'coffee':['yesterday'],
'class':['no, I am a good student','uhh, maybe.''I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'homework':['about 10 hours','about 2 hours'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
'math':'steve',
'art':'Ronny',
'drama':'Abie',
'CS':'Aron',
'Social':'Aaron',
'History':'summer',
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['vancouver','ontario'],
'game':'LOL',
'Car':'Audi'''

Questions=[
  "major",'birthday','food','drink','breakfast','homework','sleep','university','hometown','Sports'
]
Answers=[
'math','october 10th 2000','Kung pao chicken','Pepsi','sunny','burger and cereal','I haven''t finished it yet','I have sleep disorder yesterday...','UBC','Vancouver','Ping Pong ball'
]
# function for giving question
def list_faq():
    for i in range(len(Questions)):
        print(str(i)+":"+Questions[i])

def check_for_Q(sentence):
    if "major" in sentence:
        return Answers[0]
    elif"birthday" in sentence:
        return Answers[1]
    elif "food" in sentence:
        return Answers[2]
    elif "drink"in sentence:
        return Answers[3]
    elif "weather"in sentence:
        return Answers[4]
    elif "breakfast"in sentence:
        return Answers[5]
    elif "homework"in sentence:
        return Answers[6] 
    elif "sleep"in sentence:
        return Answers[7]
    elif "university"in sentence:
        return Answers[8]
    elif "hometown"in sentence:
        return Answers[9]
    else:
        print("I can not understand your question ")
#main body for program
answer=input("Hi, I am chatBot\n")
while answer!="HI" and answer!="hi":
    print("I said hi to you please say something, please try again")
    answer=input("Hi, I am chatBot\n")
#ask user input       
name=input("What is your name\n")
print("Nice to meet you "+name+"\n")
print("Ask me some questions "+name+"\n")
r.extract_keywords_from_text(mytext)
r.get_ranked_phrases_with_scores()
tokens = nltk.word_tokenize(mytext)
#print("if you do not know what to ask, type help")
answer = input("if you do not know what to ask, type help ,at the meanwhile I will initialize with my data")
if answer=="help":
    print(tokens)
    list_faq()
print("\n")
questiona=[]

#conversation begins 
while True:
    sentence=input("You: ")
    response=check_for_Q(sentence)
    print("YourBot: "+response)

    if "end" in sentence:
        break