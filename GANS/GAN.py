# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 03:30:13 2020

@author: Samsung
"""

from keras.layers import Dense, Dropout, Input, ReLU
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train=(x_train.astype(np.float32)-127.5)/127.5 #[-1,0] arasına sıkıştırma işlemi.

print(x_train.shape) # 60000 tane 28'e 28 resmim var
plt.imshow(x_test[2])

#CREATE GENERATOR 

def create_generator():
    generator = Sequential()
    generator.add(Dense(units=512, input_dim =100))
    generator.add(ReLU())
    
    generator.add(Dense(units=512))
    generator.add(ReLU())
    
    generator.add(Dense(units=1024))
    generator.add(ReLU())
    
    generator.add(Dense(units=784, activation="tanh"))
    generator.compile(loss="binary_crossentropy",
                      optimizer = Adam(lr = 0.0001, beta_1 = 0.5))
    
    return generator

g=create_generator()
g.summary()

#CREATE DISCRIMINATOR

def create_discriminator():
    discriminator=Sequential()
    discriminator.add(Dense(units=1024, input_dim =784))
    discriminator.add(ReLU())
    discriminator.add(Dropout(0.4))
    discriminator.add(Dense(units=512))
    discriminator.add(ReLU())
    discriminator.add(Dropout(0.4))
    discriminator.add(Dense(units=256))
    discriminator.add(ReLU())
    
    discriminator.add(Dense(units=1, activation = "sigmoid"))
    
    discriminator.compile(loss="binary_crossentropy",
                      optimizer = Adam(lr = 0.0001, beta_1 = 0.5))
    
    return discriminator

d=create_discriminator()
d.summary()


 #GANS
 
def create_gan(discriminator, generator):
     discriminator.trainable=False
     gan_input = Input(shape=(100,))
     x=generator(gan_input)
     gan_output=discriminator(x)
     gan= Model(inputs= gan_input, outputs= gan_output)
     gan.compile(loss="binary_crossentropy",
                      optimizer = "adam")
     
     return gan
 
gan=create_gan(d,g)
gan.summary()
     
#train
epochs = 20
batch_size = 256
for e in range (epochs):
    for _ in range(batch_size):
        
        noise = np.random.normal(0,1, [batch_size,100])
        
        generated_images = g.predict(noise)
            
        image_batch = x_train[np.random.randint(low =0, high = x_train.shape[0], size = batch_size)]
        
        x = np.concatenate([image_batch, generated_images])
        
        y_dis = np.zeros(batch_size*2)
        y_dis[:batch_size]=1
        
        d.trainable=True
        d.train_on_batch(x,y_dis)
        
        noise = np.random.normal(0,1, [batch_size, 100])
        
        y_gen = np.ones(batch_size)
        
        d.trainable=False
        gan.train_on_batch(noise, y_gen)
        
    print("epochs: ", e)
    
g.save_weights('gan_model.h5')