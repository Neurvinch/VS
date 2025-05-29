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

