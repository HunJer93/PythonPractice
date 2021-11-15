# sightWords.py
# the purpose of this program is to use lists to create a running list of sight words for a classroom.
# Jeremy Hunton
# 9/20/2021



# createSentence passes a list of sight words and returns a string
def createSentence(sightWords):
    # declare the sentence start and end
    sentenceStart = 'The ' + str(len(sightWords)) + ' new sight words for this week are '
    sentenceEnd = ''
    # if the length of sightWords is not 0...
    if(len(sightWords) > 2):
        for word in sightWords:
            # if not at the end of the list..
            if(sightWords.index(word) < len(sightWords) -1):
                # concat to the end of the sentence
                sentenceEnd += word + ', '
            # else the end of the sentence
            else:
                # concat the last word to the end, the whole sentence, and then return it
                sentenceEnd += 'and ' + word + '.'
                sentenceStart += sentenceEnd
                return sentenceStart
    #else if there is only 1 word in the list, print that there is only 1 word
    elif(len(sightWords) == 1):
        return 'The only sight word for this week is ' + sightWords[0]
    # else if there are only 2 words, create a sentence and remove the oxford comma
    elif(len(sightWords) ==2):
        sentenceStart += sightWords[0] + ' and ' + sightWords[1] +'.'
        return sentenceStart
    # else if there are no words, return no new sight words
    else:
        return 'There are no new sight words for this week!'



# declare the words for each week
week1 = ['new', 'barn','shark','hold','art','only','eyes']
week2 = ['subtract','add']
week3 = ['girl','house','best','thing','easy','wrong','right','again','above']
week4 = ['question']
week5 = []

print(createSentence(week1))
print(createSentence(week2))
print(createSentence(week3))
print(createSentence(week4))
print(createSentence(week5))


# Question:
# After the following code is executed, what is the value of animals? Is the animals list sorted? Why or why not?
# animals = ['dog', 'cat', 'horse', 'elephant', 'bear', 'fox']
# def sortList(inputList):
#   inputList.sort()
# sortList(animals)

#Answer:
# The value of animals will be sorted in alphabetical order.
