from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "Win money now", "Limited time offer", "Hello friend", 
    "Earn cash quickly", "Meeting schedule", "Project discussion",
    "Free lottery win", "Lunch today", "Click here to claim"
]

labels = [1, 1, 0, 1, 0, 0, 1, 0, 1]

vectorizer = CountVectorizer(binary=True)
x= vectorizer.fit_words(texts)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

bnb = BernoulliNB()

bnb.fit(X_train, y_train)

y_pred = bnb.predict(X_test);

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))