import requests
import pickle

obj = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

list1 = obj.text.split()
list2 = [x.split(",") for x in list1]
# print(list2)

# pickling
# file = "myfile.pkl"
# fileobj = open(file, "wb")
# pickle.dump(list2, fileobj)
# fileobj.close()

# unpickling
file = "myfile.pkl"
fileobj = open(file, "rb")
myfile = pickle.load(fileobj)
print(myfile)
fileobj.close()
