import tensorflow as tf
from tensorflow import keras 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import os
caminhoAtual = os.getcwd()
import sys
sys.path.append(f'{caminhoAtual}')

from lib.printers import *


def vizualiza_imagens(imagens, labels):
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(imagens[i], cmap=plt.cm.binary)
        plt.xlabel(nome_classes[labels[i][0]])
    plt.show()


(imagens_treino, labels_treino), (imagens_teste, labels_teste) = keras.datasets.cifar10.load_data()
nome_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

imagens_treino = imagens_treino/255.0
imagens_teste  = imagens_teste/255.0

vizualiza_imagens(imagens_treino, labels_treino)

modelo = keras.models.Sequential()

modelo.add(keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(32, 32, 3)))
modelo.add(keras.layers.MaxPooling2D((2,2)))

modelo.add(keras.layers.Conv2D(64, (3,3), activation='relu'))
modelo.add(keras.layers.MaxPooling2D((2, 2)))

modelo.add(keras.layers.Conv2D(64, (3,3), activation="relu"))
modelo.add(keras.layers.MaxPooling2D((2,2)))

modelo.add(keras.layers.Flatten())
modelo.add(keras.layers.Dense(64, activation="relu"))
modelo.add(keras.layers.Dense(10, activation="softmax"))

thematicBreakPrint(modelo.summary())

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=['accuracy'])

history = modelo.fit(imagens_treino,
                     labels_treino,
                     epochs=10,
                     validation_data=(imagens_teste, labels_teste))

nova_imagem = Image.open("modulo17/dados/nova_imagem.jpg")
thematicBreakPrint(nova_imagem.size)

nova_imagem = nova_imagem.resize((32, 32))
nova_imagem.show()

nova_imagem_array =  np.array(nova_imagem) / 255.0
nova_imagem_array = np.expand_dims(nova_imagem_array, axis=0)

previsoes = modelo.predict(nova_imagem_array)
thematicBreakPrint(previsoes)

classePrevista = np.argmax(previsoes)
nomeClassePrevista = nome_classes[classePrevista]

thematicBreakPrint(nomeClassePrevista)