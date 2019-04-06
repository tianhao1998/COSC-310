#initialize our chat sentences
from nltk.tokenize import  word_tokenize
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag



from tkinter import *


import random
data={
'major':['math','art','physics','computer science'],
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
'class':['no, I am a good student','uhh, maybe.','I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'mother':['Her name is Sara'],
'cousin':['Her name is Sam'],
'sister':['Her name is Amy'],
'math':['steve'], 
'art':['Ronny'],
'drama':['Abie'],
'CS':['Aron'],
'Social':['Aaron'],
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['i will stay at Vancouver','ontario'],
'game':['LOL','Dota'],
'Car':['Audi'],
# Add an extra topic to your agent's repertoire.
'book':['Grimm''s Fairy Tales','The Kite Runner','game of Thrones'],
'eat':['rice','eggs','pineapple']

}

outOfRange=[
        'I can not understand the question ','let talk something else','I refuse to answer this question','do you want talk about my father?'
        ,'I have no idea what are you talking about'
    ]


dataKey=list(data.keys())

print("These are the sentences in my dataset,please have a look\n")
print(data)
print("\n")
pst=PorterStemmer()
#


def say_hello():
    name_of_user=entry_1.get()
    string_to_display="Hi, "+name_of_user +" I am chatBot\n"
    label_2=Label(my_window)
    label_2['text']=string_to_display
    label_2.grid(row=1,column=1)
    
my_window=Tk()
label_1=Label(my_window,text="name: ")
entry_1=Entry(my_window)
button1=Button(my_window,text='click', command=say_hello)


label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button1.grid(row=1,column=0)
my_window.mainloop()
# refer from video https://www.youtube.com/watch?v=qCnBkZLb-E4



answer=input("Hi, I am chatBot\n")
while answer!="HI" and answer!="hi":
    print("I can not answer your question, please try again")
    answer=input("Hi, I am chatBot\n")

#ask user input       
name=input("What is your name\n")
print("Nice to meet you "+name+"\n")
print("Ask me some questions "+name+"\n")
#print("if you do not know what to ask, type help")
answer = input("if you do not know what to ask, type help ")
if answer=="help":
    print(data.keys())
print("\n")
print('here is a sample question:what''s your major ')
question=input("What you want to ask\n ")

#convert string to a list of words
question=word_tokenize(question)

questiona=[]
for x in question:
    questiona.append(pst.stem(x)); #normalize words
    
afterTag=pos_tag(question)
print(afterTag)
    
outOfRangecount=0;
answerexist=False;
for x in dataKey:
    if questiona.__contains__(x):
        print((data[x])[random.randint(0,len(data[x])-1)])
        answerexist=True

if answerexist==False:
     print(outOfRange[outOfRangecount])
     outOfRangecount=outOfRangecount+1


play=True;
while play:
    answer=input("Do you still want to play ? ")
    if answer=='yes':
        question=input("What you want to ask \n")
        answerexist2=False;
        question=word_tokenize(question)
        questiona2=[]
        for x in question:
            questiona2.append(pst.stem(x)); #normalize words
            
        for x in dataKey:
           if questiona2.__contains__(x):
               print((data[x])[random.randint(0,len(data[x])-1)])
               answerexist2=True
        if answerexist2==False:
            print(outOfRange[outOfRangecount])
            outOfRangecount=outOfRangecount+1;
    else:
        play=False;
        break;
        
       
print("thank you!")        