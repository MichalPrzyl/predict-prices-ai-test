# Testing chatbot for our little automatic planting
# project.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


data = {
    "Podlej wszystkie kwiatki": "water_all",
    
    "Fikus": "water_1",
    "Podlej fikusa": "water_1",
    "Podlewamy fikusa": "water_1",
    
    "Stokrotka": "water_2",
    "Podlej stokrotkę": "water_2",
    "Podlewamy stokrotkę": "water_2",
    
    "Piwonia": "water_3",
    "Podlej piwonię": "water_3",
    "Podlewamy piwonię": "water_3",    
}

training_sentences = list(data.keys())

training_labels = list(data.values())


vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_sentences)


classifier = LogisticRegression()
classifier.fit(X_train, training_labels)


while True:
    user_input = input("Ty: ")
    X_test = vectorizer.transform([user_input])
    predicted_intent = classifier.predict(X_test)[0]
    print(f"Bot (rozpoznana intencja): {predicted_intent}")

    # Możesz dodać proste odpowiedzi na podstawie intencji:
    if predicted_intent == "water_1":
        print("Bot: Podlewam water_1!")
    elif predicted_intent == "water_2":
        print("Bot: Podlewam water_2!")
    elif predicted_intent == "water_3":
        print("Bot: Podlewam water_3!")
    elif predicted_intent == "water_all":
        print("Bot: Podlewam wszystkie roślinki!")
    else:
        print("Bot: Nie rozumiem.")
