from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from estimate_lai import getEstimation

app = Flask(__name__, static_folder="static")

res = "0"

@app.route('/upload', methods=['POST'])
def handle_upload():
    print('Received POST request at /upload')

    try:
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'status': 'error', 'message': 'No selected file'})

        print('Received file:', file.filename)
        print('File content type:', file.content_type)

        res = getEstimation(file)

        response_data = {'status': 'success', 'estimated_lai':res}
        return jsonify(response_data)
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'status': 'error', 'message': 'An error occurred'})

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)
