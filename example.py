import pickle
import sklearn

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


print(loaded_model)

test = [[2, 1, 1, 1, 6, 6, 7]]

prediction = loaded_model.predict(test)

print(f'prediction: ', prediction[0])