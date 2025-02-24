#import the panda library that which is used for handling tables and spreadsheet data
import pandas as pd # this basically is a read(csv)


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

data["steamspy_tags"] = data["steamspy_tags"].apply(lambda Gen: Gen.split(";") if isinstance(Gen, str) else []) #splitting the genres into a list of genres because the way they are printed out will mess alot of stuff up when searching them solo

##print(data.head())



