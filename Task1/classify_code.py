import joblib

# Load model and vectorizer
model = joblib.load('vuln_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def classify_code(code_snippet):
    # Preprocess input
    features = vectorizer.transform([code_snippet])
    # Predict
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # probability of vulnerable
    
    if prediction == 1:
        print(f"⚠️ The code is likely vulnerable! (Confidence: {probability * 100:.2f}%)")
    else:
        print(f"✅ The code looks safe. (Confidence: {(1 - probability) * 100:.2f}%)")

if __name__ == "__main__":
    print("Paste your code snippet below:")
    user_code = ""
    print("(Enter END in a new line to finish)")
    while True:
        line = input()
        if line.strip() == "END":
            break
        user_code += line + "\n"

    classify_code(user_code)
