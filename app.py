from flask import Flask, render_template, request
from custom_hash import custom_hash
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    custom_hash_result = ""
    sha256_result = ""
    input_text = ""
    
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        custom_hash_result = custom_hash(input_text)
        sha256_result = hashlib.sha256(input_text.encode()).hexdigest()
    
    return render_template('index.html',
                        custom_hash_result=custom_hash_result,
                        sha256_result=sha256_result,
                        input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)