###--->Creating a Search Engine

text=input("Enter your text:")  
#Here it takes the data you want to search from. For example we can search from wikipedia

word=input("Enter your word: ")
#Here it takes the word you want to search from the data given above

def search(text,word):
    if word in text:    #If thew word we searched in the databsae is found it will return the word
        return(word)
    else:               #If the word is not in database it returns with the statement.
        return("Oops, Sorry!")

print(search(text,word))