from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()
print(iris_dataset.keys())

# split data into training and test data
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# train the model
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# any new data
new_data = [1, 2, 3, 0.2]
X_new = np.array([new_data])

# using the model we predict the species of the new values
prediction = knn.predict(X_new)
print(f'Prediction for input {new_data}:', *iris_dataset['target_names'][prediction])
