# %%
# Gerekli kütüphaneleri yükleyin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential, Model, load_model
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping

# %%
data = pd.read_csv("cardio_train.csv",sep=";")

# Veri setini incele
print(data.head())

# %%
X = data.drop("cardio", axis=1)  # Özellikler
X = X.drop("id",axis=1)
y = data["cardio"]  # Etiketler

print(X)
# Eğitim ve test setlerini ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
model = RandomForestClassifier() 
# Rastgele Ormanlar kullanarak bir sınıflandırıcı modeli seçin
model.fit(X_train, y_train)

# Test seti üzerinde modelin performansını değerlendirin
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluğu:", accuracy)

# %%
model2 = Sequential([
    Dense(32, activation='relu', input_shape=(11,)),

    Dense(64, activation='softmax'),
    Dense(128, activation='softmax'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='softmax'),
    Dense(1, activation='sigmoid')
])

model2.summary()

optimizer1= keras.optimizers.Adam(learning_rate=0.2)
model2.compile(optimizer=optimizer1, loss="categorical_crossentropy", metrics=["accuracy"])

history = model2.fit(X_train,y_train, epochs=1, batch_size=1, validation_split=0.2)

# %%
model2.save("./Ellidogruluk.keras")



# %%
yenimodel=load_model("Ellidogruluk.keras")
testdata = [6935,1,171,60,110,90,0,0,0,0,1]

import numpy as np
testdata = np.array(testdata)
testdata = testdata.reshape(1, 11)

sonuc = yenimodel.predict(testdata)

# accuracy = accuracy_score(y_test[0], sonuc)
print(sonuc[0])





# %%
