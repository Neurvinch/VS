from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

texts = [
    "Free offer now", "Win money lottery", "Project deadline tomorrow",
    "Discuss meeting today", "Click to win prizes", "Your invoice attached",
    "Earn money easily", "See you at office", "Free entry in contest"
]
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1]  # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)


X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=0)

# Initialize and train the Multinomial Naive Bayes model
mnb = MultinomialNB()
mnb.fit(X_train, y_train)

# Predict
y_pred = mnb.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

