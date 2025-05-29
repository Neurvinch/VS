from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "Win money now", "Limited time offer", "Hello friend", 
    "Earn cash quickly", "Meeting schedule", "Project discussion",
    "Free lottery win", "Lunch today", "Click here to claim"
]