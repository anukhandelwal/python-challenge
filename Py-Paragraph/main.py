#Paragraph Analysis
#-----------------

# Dependencies
import os
import csv
import re
import numpy



# create path for file budget_data_2.csv
csvpath = os.path.join('paragraph_2.txt')
# open and read file from new line
with open(csvpath, newline="") as csvfile:
#	print(csvfile.read())
#	csv_reader = csv.reader(csvfile, delimiter=",")
	
	#Find all words in the paragraph. counts hyphenated words as 2 words.
	words=re.findall(r'\w+', csvfile.read())
	
	print("Paragraph Analysis")
	print("--------------------")
	print("In the file : " + csvpath)
	print("Approximate Word count: "+ str(len(words) - 1))

with open(csvpath, newline="") as csvfile:
	#split the paragraph into sentences at .
	sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', csvfile.read())
	
	
	#print(sentences)
	print("Approximate Sentence Count: " + str(len(sentences) - 1))
	
	#Create empty list of Total_Letter_Count to findaverage letter count later
	Total_letter_count = []

	#Create empty list of Total_word_Count to findaverage word count later
	Total_word_count = []

	for i in range(0, len(sentences)-1):
		
		#create a list of words by sentence splitting
		words = sentences[i].split()

		#Find Letter count for each word in the sentence
		letter_count_per_word = [len(w) for w in words]

		#find average of the letter count of each word in the list
		average = numpy.mean(letter_count_per_word)

		#add the averages of the letter count of words of each sentence to this list
		Total_letter_count.append(average)
		Total_word_count.append(int(len(words)))
		
		# Code to find average letter count per word per Sentence, just in case is needed
		#print("Sentence: "+ str(i+1))
		#print("--------------")
		#print(words)
		#print(len(words))
		#print("Approximate Letter Count per Word: " + str(average))
		#print(letter_count_per_word)
		#print(Total_letter_count)

	#Find the average of letter count of words for each senetence from the list created	
	average_letter_count=numpy.mean(Total_letter_count)


	#Find the average of word count of each senetence from the list created	
	average_word_count=numpy.mean(Total_word_count)

	#print average letter count across all sentence
	print("Approximate Letter Count per Word: " + str(average_letter_count))
		
	#print average word count across all sentence
	print("Approximate word Count per sentence: " + str(average_word_count))






