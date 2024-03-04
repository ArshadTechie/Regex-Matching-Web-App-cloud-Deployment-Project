from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    num_matches = len(matches)
    digit_or_string_count = sum(1 for char in test_string if char.isdigit() or char.isalpha())

    explanation = "The regex pattern searches for sequences of characters that match the specified pattern. " \
                  "In this case, it looks for sequences that match the pattern '{}' in the test string. " \
                  "The pattern matches {} times in the test string. " \
                  "Additionally, the test string contains {} digits or strings.".format(regex_pattern, num_matches, digit_or_string_count)
    # You can replace the above explanation with a more detailed explanation based on your regex pattern.

    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches, num_matches=num_matches, digit_or_string_count=digit_or_string_count, explanation=explanation)


@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    is_valid = re.match(regex_pattern, email) is not None
    result_message = "Valid email address." if is_valid else "Invalid email address."
    return jsonify({'email': email, 'is_valid': is_valid, 'result_message': result_message})

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=5000)