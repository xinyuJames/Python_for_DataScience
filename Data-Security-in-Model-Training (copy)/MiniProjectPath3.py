#MiniProjectPath3
import numpy as np
import matplotlib.pyplot as plt
# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
#import models
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import copy
#denoise
from sklearn.decomposition import KernelPCA


rng = np.random.RandomState(1)
digits = datasets.load_digits()
images = digits.images
labels = digits.target

#Get our training data
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.6, shuffle=False)

def dataset_searcher(number_list,images,labels):
  #insert code that when given a list of integers, will find the labels and images
  #and put them all in numpy arrary (at the same time, as training and testing data)

  image_array = []
  label_array = []
  for i, label in enumerate(labels):
    if label in number_list:
      image_array.append(images[i])
      label_array.append(label)
  images_nparray = np.array(image_array)
  labels_nparray = np.array(label_array)

  return images_nparray, labels_nparray

def print_numbers(images,labels):
  #insert code that when given images and labels (of numpy arrays)
  #the code will plot the images and their labels in the title. 
  n = len(images)
  cols = 80
  rows = int(np.ceil(n / cols))
  plt.figure(figsize=(cols * 2, rows * 2))
  for i, image in enumerate(images):
      axes = plt.subplot(rows, cols, i + 1)
      axes.imshow(image, cmap='gray')
      axes.set_title(str(labels[i]))
      axes.axis('off')
  plt.tight_layout()
  plt.show()

class_numbers = [2,0,8,7,5]
#Part 1
class_number_images , class_number_labels = dataset_searcher(class_numbers, images, labels)
#Part 2
# print_numbers(class_number_images , class_number_labels)


model_1 = GaussianNB()

#however, before we fit the model we need to change the 8x8 image data into 1 dimension
# so instead of having the Xtrain data beign of shape 718 (718 images) by 8 by 8
# the new shape would be 718 by 64
X_train_reshaped = X_train.reshape(X_train.shape[0], -1)

#Now we can fit the model
model_1.fit(X_train_reshaped, y_train)
print("Model 1 trained...")
#Part 3 Calculate model1_results using model_1.predict()
model1_results = model_1.predict(X_test.reshape(X_test.shape[0], -1))


def OverallAccuracy(results, actual_values):
  #Calculate the overall accuracy of the model (out of the predicted labels, how many were correct?)
  Accuracy = np.mean(results == actual_values)
  return Accuracy


# Part 4
Model1_Overall_Accuracy = OverallAccuracy(model1_results, y_test)
print("The overall results of the Gaussian model with test data is " + str(Model1_Overall_Accuracy))


#Part 5
allnumbers = [0,1,2,3,4,5,6,7,8,9]
allnumbers_images, allnumbers_labels = dataset_searcher(allnumbers, images, labels)

model1_all_results = model_1.predict(allnumbers_images.reshape(allnumbers_images.shape[0], -1))
# print_numbers(allnumbers_images, model1_all_results)
Model1_Overall_Accuracy = OverallAccuracy(model1_all_results, allnumbers_labels)
print("The overall results of the Gaussian model with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(Model1_Overall_Accuracy))


#Part 6
#Repeat for K Nearest Neighbors
model_2 = KNeighborsClassifier(n_neighbors=10)
model_2.fit(X_train_reshaped, y_train)
print("Model 2 trained...")
model2_results = model_2.predict(X_test.reshape(X_test.shape[0], -1))
Model2_Overall_Accuracy = OverallAccuracy(model2_results, y_test)
print("The overall results of the KNN model is " + str(Model2_Overall_Accuracy))

model2_all_results = model_2.predict(allnumbers_images.reshape(allnumbers_images.shape[0], -1))
# print_numbers(allnumbers_images, model2_all_results)
Model2_Overall_Accuracy = OverallAccuracy(model2_all_results, allnumbers_labels)
print("The overall results of the KNN model with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(Model2_Overall_Accuracy))


#Repeat for the MLP Classifier
model_3 = MLPClassifier(random_state=0)
model_3.fit(X_train_reshaped, y_train)
print("Model 3 trained...")
model3_results = model_3.predict(X_test.reshape(X_test.shape[0], -1))
Model3_Overall_Accuracy = OverallAccuracy(model3_results, y_test)
print("The overall results of the MLP model is " + str(Model3_Overall_Accuracy))

model3_all_results = model_3.predict(allnumbers_images.reshape(allnumbers_images.shape[0], -1))
# print_numbers(allnumbers_images, model3_all_results)
Model3_Overall_Accuracy = OverallAccuracy(model3_all_results, allnumbers_labels)
print("The overall results of the MLP model with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(Model3_Overall_Accuracy))


#Part 8
#Poisoning
# Code for generating poison data. There is nothing to change here.
noise_scale = 10.0
poison = rng.normal(scale=noise_scale, size=X_train.shape)

X_train_poison = X_train + poison


#Part 9-11
#Determine the 3 models performance but with the poisoned training data X_train_poison and y_train instead of X_train and y_train

# Initialize variables
X_train_poison_reshape = X_train_poison.reshape(X_train_poison.shape[0], -1)
X_test_reshape = X_test.reshape(X_test.shape[0], -1)
allnumbers_images_reshape = allnumbers_images.reshape(allnumbers_images.shape[0], -1)

# GaussianNB model train
model1_poison = GaussianNB().fit(X_train_poison_reshape, y_train)
print("Model 1 poison trained...")

# GaussianNB result for test set
model1_poison_result_testset = model1_poison.predict(X_test_reshape)
model1_poison_accuracy_testset = OverallAccuracy(model1_poison_result_testset, y_test)
print("The overall results of the Gaussian model poison is " + str(model1_poison_accuracy_testset))

# GaussianNB result for numbers
model1_poison_result_allnumber = model1_poison.predict(allnumbers_images_reshape)
model1_poison_accuracy_allnumber = OverallAccuracy(model1_poison_result_allnumber, allnumbers_labels)
print_numbers(allnumbers_images[:200], model1_poison_result_allnumber[:200])
print("The overall results of the Gaussian model poison with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model1_poison_accuracy_allnumber))

# KNN model train
model2_poison = KNeighborsClassifier(n_neighbors=10).fit(X_train_poison_reshape, y_train)
print("Model 2 poison trained...")

# KNN result for test set
model2_poison_result_testset = model2_poison.predict(X_test_reshape)
model2_poison_accuracy_testset = OverallAccuracy(model2_poison_result_testset, y_test)
print("The overall results of the KNN model poison is " + str(model2_poison_accuracy_testset))

# KNN result for numbers
model2_poison_result_allnumber = model2_poison.predict(allnumbers_images_reshape)
model2_poison_accuracy_allnumber = OverallAccuracy(model2_poison_result_allnumber, allnumbers_labels)
print_numbers(allnumbers_images[:200], model2_poison_result_allnumber[:200])
print("The overall results of the KNN model poison with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model2_poison_accuracy_allnumber))


# MLP model train
model3_poison = MLPClassifier(random_state=0, max_iter=500).fit(X_train_poison_reshape, y_train)
print("Model 3 poison trained...")

# MLP result for test set
model3_poison_result_testset = model3_poison.predict(X_test_reshape)
model3_poison_accuracy_testset = OverallAccuracy(model3_poison_result_testset, y_test)
print("The overall results of the MLP model poison is " + str(model3_poison_accuracy_testset))

# MLP result for numbers
model3_poison_result_allnumber = model3_poison.predict(allnumbers_images_reshape)
model3_poison_accuracy_allnumber = OverallAccuracy(model3_poison_result_allnumber, allnumbers_labels)
print_numbers(allnumbers_images[:200], model3_poison_result_allnumber[:200])
print("The overall results of the MLP model poison with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model3_poison_accuracy_allnumber))

# Part 10, 11...

print("Samples of poisoned training sets:")
# print_numbers(X_train_poison[:20], y_train[:20])


#Part 12-13
# Denoise the poisoned training data, X_train_poison. 
# hint --> Suggest using KernelPCA method from sklearn library, for denoising the data. 
# When fitting the KernelPCA method, the input image of size 8x8 should be reshaped into 1 dimension
# So instead of using the X_train_poison data of shape 718 (718 images) by 8 by 8, the new shape would be 718 by 64

# Denoise...
kpca = KernelPCA(
  n_components=None,
  kernel='rbf',
  gamma=0.001,
  fit_inverse_transform=True,
  alpha=5e-3,
  random_state=42
)
X_train_kpca = kpca.fit_transform(X_train_poison_reshape)
X_train_denoised = kpca.inverse_transform(X_train_kpca)
print("Some denoised training samples:")
# print_numbers(X_train_denoised.reshape(-1, 8, 8)[:20], y_train[:20]) # ???


#Part 14-15
#Determine the 3 models performance but with the denoised training data, X_train_denoised and y_train instead of X_train_poison and y_train
#Explain how the model performances changed after the denoising process.

# GaussianNB model train
model1_denoised = GaussianNB().fit(X_train_denoised, y_train)
print("Model 1 denoised trained...")

# GaussianNB result for test set
model1_denoised_result_testset = model1_denoised.predict(X_test_reshape)
model1_denoised_accuracy_testset = OverallAccuracy(model1_denoised_result_testset, y_test)
print("The overall results of the Gaussian model denoised is " + str(model1_denoised_accuracy_testset))

# GaussianNB result for numbers
model1_denoised_result_allnumber = model1_denoised.predict(allnumbers_images_reshape)
model1_denoised_accuracy_allnumber = OverallAccuracy(model1_denoised_result_allnumber, allnumbers_labels)
# print_numbers(allnumbers_images[:200], model1_denoised_result_allnumber[:200])
print("The overall results of the Gaussian model denoised with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model1_denoised_accuracy_allnumber))

# KNN
model2_denoised = KNeighborsClassifier(n_neighbors=10).fit(X_train_denoised, y_train)
print("Model 2 denoised trained...")
model2_denoised_result_testset = model2_denoised.predict(X_test_reshape)
model2_denoised_accuracy_testset = OverallAccuracy(model2_denoised_result_testset, y_test)
print("The overall results of the KNN model denoised is " + str(model2_denoised_accuracy_testset))
model2_denoised_result_allnumber = model2_denoised.predict(allnumbers_images_reshape)
model2_denoised_accuracy_allnumber = OverallAccuracy(model2_denoised_result_allnumber, allnumbers_labels)
# print_numbers(allnumbers_images[:200], model2_denoised_result_allnumber[:200])
print("The overall results of the KNN model denoised with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model2_denoised_accuracy_allnumber))

# MLP
model3_denoised = MLPClassifier(random_state=0).fit(X_train_denoised, y_train)
print("Model 3 denoised trained...")
model3_denoised_result_testset = model3_denoised.predict(X_test_reshape)
model3_denoised_accuracy_testset = OverallAccuracy(model3_denoised_result_testset, y_test)
print("The overall results of the MLP model denoised is " + str(model3_denoised_accuracy_testset))
model3_denoised_result_allnumber = model3_denoised.predict(allnumbers_images_reshape)
model3_denoised_accuracy_allnumber = OverallAccuracy(model3_denoised_result_allnumber, allnumbers_labels)
# print_numbers(allnumbers_images[:200], model3_denoised_result_allnumber[:200])
print("The overall results of the MLP model denoised with the numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] is " + str(model3_denoised_accuracy_allnumber))

