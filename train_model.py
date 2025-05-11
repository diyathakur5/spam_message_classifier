# train_model.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import joblib

# Sample data
data = pd.DataFrame({
    'text': [
        'Congratulations, you won a lottery!',
        'Free entry to win a brand new car!',
        'Urgent! You have won a $1000 gift card.',
        'Let’s meet tomorrow.',
        'hi my name is ',
        'You are selected for a prize!',
        'can i call you',
        'lottery! ',
        'how are you',
    ],
    'label': [1, 1, 1, 0, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam
})

X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Optional: Evaluate
X_test_vec = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))
