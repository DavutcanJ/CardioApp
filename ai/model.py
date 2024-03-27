# Gerekli kütüphaneleri yükleyin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential, Model, load_model

# Veri setini yükleyin
data = pd.read_csv("cardio_train.csv",sep=";")

# Veri setini inceleyin
print(data.head())

# Gereksiz sütunları kaldırın veya veri setini temizleyin
# Örneğin, gereksiz sütunları kaldırmak için:
# data.drop(["sütun_adı"], axis=1, inplace=True)

# Özellikler ve etiketleri ayırın
X = data.drop("cardio", axis=1)  # Özellikler
y = data["cardio"]  # Etiketler

# Eğitim ve test setlerini ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitin
# model = RandomForestClassifier() 
# # Rastgele Ormanlar kullanarak bir sınıflandırıcı modeli seçin
# model.fit(X_train, y_train)

# # Test seti üzerinde modelin performansını değerlendirin
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print("Model Doğruluğu:", accuracy)


# Modeli kaydedin ve dağıtın
# Modelinizi Docker konteynerinde paketleyerek ve Azure gibi bir bulut servisine yükleyerek dağıtabilirsiniz.


model2 = Sequential()

model2.add(layers.Input(shape=(11,)))
model2.add(layers.Dense(32,activation="softmax"))
model2.add(layers.Dropout(rate=0.2))
model2.add(layers.Dense(64,activation="softmax"))
model2.add(layers.Dense(64,activation="softmax"))
model2.add(layers.Flatten())

model2.summary()