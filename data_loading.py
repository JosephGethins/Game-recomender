
#import the panda library that which is used for handling tables and spreadsheet data
import pandas as pd # this basically is a read(csv)

#Import the CountVectorizer from the sklearn library
from sklearn.feature_extraction.text import CountVectorizer #this is a tool that converts text/String into numbers so genres that have the same numbers will be easier to reccomend instead of slowing down the process with comparing Strings

#Import the cosine_similarity (talked about below) from the sklearn library
from sklearn.metrics.pairwise import cosine_similarity

#Load the steam data from the csv file
def load_steam_data():
	
	data = pd.read_csv('data/steam.csv') #reads the csv file and stores it in the variable data
	
	return data

if __name__ == "__main__": #was having trouble loading steam data randomly and using this it ensures it only loads when this specific file is run
	data = load_steam_data() #lets us use the dataset after it has loaded?

#print(data.head()) #prints the first few rows of the dataset

#print(data.columns)

#print(data.isnull().sum()) # Check for missing values

data = data [['name', 'release_date', 'english', 'developer', 'publisher', 'platforms', 'required_age', 'categories', 'steamspy_tags' , 'price' ]]

data["steamspy_tags"] = data["steamspy_tags"].apply(lambda Genre: Genre.split(";") if isinstance(Genre, str) else []) #splitting the genres into a list of genres because the way they are printed out will mess alot of stuff up when searching them solo

data["steamspy_tags"] = data["steamspy_tags"].apply(lambda Genre: " ".join(Genre)) #joins genres back together so they can be used as a string

vector = CountVectorizer() # this is like an object using CountVectorizer whuch is an encoder that turns strings into numbers? 

genres_matrix = vector.fit_transform(data["steamspy_tags"]) #this is the matrix that will be used to compare genres

#print(genres_matrix.toarray()) #prints the matrix this came out in the form of a bunch of zeros in a matrix so do I have to assign them each a number somehow? (answered yes below you compare them and assign them a value this is basically just creating like.... memory?)

# theres this thing called cosine similarity and apparently most reccomendation systems use it
# its a mathematical tech to measure two items based on like variables and similarities
# commonly used in reccomendation systems (im referncing a book similairty code similar to this one)
# wait this is a forumla from maths lecutre so its the (dot product)/the magnitude of two vectors or like ||x||||y||
# so basically since games have mutiple genres it compares each genre to the other game so if it is an action game it would have 1 and 0 if its a horror etc etc
# so it does the dot product comparing each so like mh wilds is action so 1, but smth like webfishing would have 0 for action genre as its not listed as action on the csv
# so you do the dot product of every single game and each of its genres so while the above games would have (1 X 0) for action
# they both have fishing in it (just an example) so the fishing genre would be (1 X 1)
# so the dot product would be (1 X 0) + (1 X 1) = 1
# then you compute the magnitudes so same thing for webfishing it would be sqrt(0^2 (for action) + 1^2 (for fishing)) = sqrt(1)
# so then if magnitude of mh wilds is sqrt(2) and webfishing is sqrt(1) 
# then it would be 1(the dot product) / sqrt(2) * 1 ) = 0.7071067811865475
# so this means the games are 70% similar in terms of genres but not the same
# ^^^^^^^^^^^This is incredibly intuitive save this above somewhere^^^^^^^^^^^ (maybe for matching game I could use this somehow)



# somemore reccomendation stuff to consider:
#       Pearson Correlation 
#		Matrix Factorization
#	    Neaurl Networks (i dont think I can do this one but research it)
# 		graph based reccomendation systems (not something that makes sense here but I think this was done in second semester data science lab)




# Back to code

# Compute cosine similarity between all games (so its doing what I worked through above)
similarity_matrix = cosine_similarity(genres_matrix)
# so each row will represent a game
# AND each column will represent how similar it is to all other games!!!

#print(similarity_matrix[:5, :5])  # making sure it works (it looks like it works seems but I dont see the unique value each game has so I need to see where/how it compares them``)










