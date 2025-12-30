from sklearn.naive_bayes import GaussianNB

# Data: [study_hours]
X = [[1], [2], [3], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass", "Pass"]

model = GaussianNB()
model.fit(X, y)

# Predict
print(model.predict([[55]]))  # Fail
print(model.predict([[5]]))  # Pass


#≠===========

# Install scikit-learn if not already
# pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
messages = [
    "Win a free iPhone now",
    "Claim your free prize",
    "Hello friend, how are you",
    "Meeting at 5 PM",
    "You won a lottery",
    "Are you coming to class",
    "Get free tickets today",
    "Homework submission is tomorrow"
]

labels = ["Spam", "Spam", "Not Spam", "Not Spam", "Spam", "Not Spam", "Spam", "Not Spam"]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Function to predict new messages
def check_spam(message):
    msg_vector = vectorizer.transform([message])
    prediction = model.predict(msg_vector)
    return prediction[0]

# Example usage
while True:
    user_input = input("\nEnter a message (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = check_spam(user_input)
    print(f"Prediction: {result}")
