python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=index.py
echo "Your Flask application should be all set up. Try running `flask run`."