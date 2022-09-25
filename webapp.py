from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    users = [ 'Jenkins','GitHUB','Nexus' ]
    return render_template('index.html', title='Welcome', members=users)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
