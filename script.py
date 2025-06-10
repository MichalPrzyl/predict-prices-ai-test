from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("Starting")


from sklearn.linear_model import LinearRegression


X = [[50], [60], [80], [100]]  # powierzchnia
y = [180, 220, 230, 400]       # cena

model = LinearRegression()

model.fit(X, y)

predicted_price = model.predict([[70]])

print(f"Przewidywana cena domu o powierzchni 70 m2: {predicted_price[0]:.2f} tys. zł")


plt.scatter([x[0] for x in X], y, color='blue', label='Dane treningowe')

import numpy as np
X_range = np.linspace(40, 110, 100).reshape(-1, 1)
y_pred = model.predict(X_range)
plt.plot(X_range, y_pred, color='red', label='Linia regresji')

plt.scatter(70, predicted_price, color='green', label='Przewidywana cena (70 m2)')

plt.xlabel('Powierzchnia domu (m2)')
plt.ylabel('Cena domu (tys. zł)')
plt.title('Regresja liniowa: przewidywanie ceny domu')
plt.legend()
plt.grid(True)

#plt.show()
plt.savefig("wykres.png")

