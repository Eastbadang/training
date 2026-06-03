import pandas as pd
import numpy as np
import tensorflow as tf

data = pd.read_csv('gpascore.csv')

#print(data.isnull().sum())
data = data.dropna()
#print(data['gpa'].max())
#print(data['gpa'].count())
#data.fillna(100)  # 빈칸 채워줌
#print(data.isnull().sum())

y_data = data['admit'].values
x_data = []

for i, rows in data.iterrows():
    #print(rows['gre'])
    #print(rows['gpa'])
    #print(rows['rank'])
    x_data.append([ rows['gre'], rows['gpa'], rows['rank']])

#exit()

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x_data), np.array(y_data), epochs=1000)

#예측
pd = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(pd)
