import sys
import joblib

# Load model and vectorizer
model = joblib.load('linter_model.pkl')
vectorizer = joblib.load('linter_vectorizer.pkl')

def lint_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    warnings = []
    for idx, line in enumerate(lines, start=1):
        # Skip empty lines
        if line.strip() == '':
            continue

        # Vectorize the line
        line_vec = vectorizer.transform([line])

        # Predict
        prediction = model.predict(line_vec)

        if prediction[0] == 1:
            warnings.append((idx, line.strip()))

    # Print results
    if warnings:
        print(f"⚠️  Found {len(warnings)} potential vulnerabilities:")
        for lineno, code in warnings:
            print(f"Line {lineno}: {code}")
    else:
        print("✅ No issues found. Your code looks safe!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ml-linter.py my_code.py")
        sys.exit(1)

    filename = sys.argv[1]
    lint_file(filename)
