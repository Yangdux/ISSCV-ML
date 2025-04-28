import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
data = pd.read_csv('safe_unsafe_code.csv')

# Features and labels
X = data['code']
y = data['label']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the code snippets
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate
accuracy = model.score(X_test_vec, y_test)
print(f"Test accuracy: {accuracy * 100:.2f}%")

# Save model and vectorizer
joblib.dump(model, 'linter_model.pkl')
joblib.dump(vectorizer, 'linter_vectorizer.pkl')

print("✅ Linter model and vectorizer saved successfully!")
