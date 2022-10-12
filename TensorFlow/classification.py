import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
fashion_mnist = tf.keras.datasets.fashion_mnist

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images.shape

train_images = train_images / 255.0
test_images = test_images / 255.0

class TensorFlow:
    def __init__(self) -> None:
        self.model = None
        self.probability_model = None
        self.predictions = None
    def plot():
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(class_names[train_labels[i]])
        plt.show()
    def setupLayers(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(28,28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
    def compandTrain(self):
        self.model.compile(optimizer='adam',
                           loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                           metrics=['accuracy'])
        self.model.fit(train_images,train_labels,epochs=30)
        test_loss, test_acc = self.model.evaluate(test_images, test_labels,verbose=2)
        print('\nTest accuracy:',test_acc)
    def predictionModels(self):
        self.probability_model = tf.keras.Sequential([self.model, tf.keras.layers.Softmax()])
        self.predictions = self.probability_model.predict(test_images)
    
    def plot_image(i, predictions_array, true_label, img):
        true_label, img = true_label[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions_array)
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                    100*np.max(predictions_array),
                    class_names[true_label],
                    color=color))
    def plot_value_array(i, predictions_array, true_label):
        true_label = true_label[i]
        plt.grid(False)
        plt.xticks(range(10))
        plt.yticks([])
        thisplot = plt.bar(range(10), predictions_array, color="#777777")
        plt.ylim([0,1])
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')
    def showImage(self):
        i = 2
        plt.figure(figsize=(6,3))
        plt.subplot(1,2,1)
        TensorFlow.plot_image(i, self.predictions[i], test_labels, test_images)
        plt.subplot(1,2,2)
        TensorFlow.plot_value_array(i, self.predictions[i], test_labels)
        plt.show()
    def useModel(self):
        img = test_images[15]
        img = (np.expand_dims(img,0))
        predictions_single = self.probability_model.predict(img)
        TensorFlow.plot_value_array(1, predictions_single[0], test_labels)
        _ = plt.xticks(range(10), class_names, rotation=45)
        plt.show()

newTense = TensorFlow()
newTense.setupLayers()
newTense.compandTrain()
newTense.predictionModels()
newTense.useModel()