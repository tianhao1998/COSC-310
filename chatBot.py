#initialize our chat sentences
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
'class':['no, I am a good student','uhh, maybe.''I refuse to answer this question.'],
'semester':['five courses','4 courses'],
'homework':['about 10 hours','about 2 hours'],
'games':['a whole day','5 hours'] ,
'job':['no, I have no time to work.''yes, I have.'],
'father':['his name is ChatbotA'],
'math':'steve',
'friend':['I do not have friend except you','her name is annie, another chatbot'],
'hometomn':['kelowna','Mars'],
'summer':['vancouver','ontario']
}
dataKey=list(data.keys())

print("These are the sentences in my dataset,please have a look\n")
print(data)
print("\n")

answer=input("Hi, I am chatBot\n")
while answer!="HI" and answer!="hi":
    print("I can not answer your question, please try again")
    answer=input("Hi, I am chatBot\n")

#ask user input       
name=input("What is your name\n")
print("Nice to meet you "+name+"\n")
print("Ask me some questions "+name+"\n")
#print("if you do not know what to ask, type help")
answer = input("if you do not know what to ask, type help")
if answer=="help":
    print(data.keys())
print("\n")
print('here is a sample question:what''s your major\n')
question=input("What you want to ask")

if question in dataKey :
    print((data[question])[1])
    
#play=True

#while play==True:
   
#play=input("Do you still want to play ?")   
# question=input("What you want to ask")

