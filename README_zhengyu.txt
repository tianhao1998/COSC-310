README

DESCRIPTION:// This a simple chatbot project that is built upon and implemented in python that allows users to have a conversation by prompting questions and answering them through a premade response dataset.

HOW TO COMPILE & RUN:// Make sure python is installed in the computer. Click run button to compile and run the code. To run the code, you have to say hi and your name to program. After this, you can just ask questions to program depend on keys which has been implemented in program. 

CLASS:// ¡°chatBot¡±: Store dataset, prompt questions and give responses, users¡¯ inputs validity check, help.     

HELP:// typing ¡°help¡± if you need help



UPDATE:// 1.For now, chatbot can understand even user input some spelling misktakes by using Stemmer.(eg. no matter input 'eatting' or 'eatten', it will be read as 'eat').
	  2.2 more topic are added in dataset.
	  3.If user enters something out of topics, chatbot will give several different reasonable responses.
	  4.program can be run many times until user input 'end'. 

FEATURES:// 1.using language toolkits(word_tokenize). now, every sentence that user inputs will be stored as words in an array. The computer can easily detect keywords.
		e.g user inputs "hello, who is your mother?" will be stored as ['hello','who','is','your','mother'].	

	    2.using PorterStemmer method. "Stemmers remove morphological affixes from words, leaving only the word stem." Now, Chatbot can understand words in different forms. 
		e.g input: "what are you eatting" or "what do you eat" output: "rice."		