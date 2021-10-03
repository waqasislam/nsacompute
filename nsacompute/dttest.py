from dt import DecisionTreeClassifier
import pandas as pd


dataset = pd.read_csv("music.csv") 
X = dataset.drop(columns=['genre'])
Y = dataset['genre']

model = DecisionTreeClassifier(max_depth = 5)
model.fit(X, Y)
predictions = model.predict([ [21,1], [22,0] ])
print(predictions)

