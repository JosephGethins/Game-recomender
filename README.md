This is a game reccomendation system using a large dataset from kaggle : https://www.kaggle.com/datasets/nikdavis/steam-store-games

Currently the code works as using a cosine filter using the genres as the 0's and 1's for the filtering and gives them a score depending on how close they are with the original genres of the game inputted
(working example at the bottom of this code)
It can display any n amount of games it is currently hardcoded in but extremely simple to change yourself if you would like to give it a try
Currently sorts in desc order 
Id like to add in price to the equation also maybe using a deviation from the original price set by the user or just a numerical value to be close to
and also the studio but this will be an easy change as I would just need to add a studio check in and see if the same ID is over mutliple games

Many online resources and Ai was used to explain online resources to furthe my understanding of dependancies like pandas and sklearn which were extremely beneficial

I would like to come back to this in the future and instead of using cosine filtering try and understand machine learning and using some sort of AI model to do this though this is probably a bit over my head

