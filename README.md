# flask-chat-1

# Setup
These instructions are a simplified version of the Flask [installation instructions](https://flask.palletsprojects.com/en/1.1.x/installation/) and [quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/). If you have any questions, feel free to reach out to me.

1. Clone this repository using `git clone` and `cd` from your command line into the folder.
2. Make sure you have Python 3 installed. You can check this by seeing if the command `python3` works in your command line. If you don't have Python 3 installed, follow [these instructions](https://realpython.com/installing-python/)
3. Python 3 comes with virtualenv, a "virtual environment" to manage packages like `Flask` that you'll need to run your application. When you first clone this repository, run `python3 -m venv` from the root of the repository to create a virtual environment for your application. This will create a few folders and files related to virtualenv, including `/bin`, `/include`, `/lib`, and `pyvenv.cfg`.
4. Once you've set up a virtual environment, whenever you're about to work on your app, make sure to run `. ./bin/activate` from the root of the repository. You should then see `(venv)` prefixed in your command line to show that you're using the virtual environment. After you do this, you should be able to download packages and run your application.
5. Once you are using the virtual environment, make sure you install all the dependencies for this application by running `pip install -r requirements.txt` (if you're using Python 3, you might need to use `pip3` instead of `pip`. You only need to do this once and don't need to again when you want to run your application.
6. Once you have `Flask` properly installed, make sure you set your environment variables so Flask knows what file to start with. In this repository, the app starts with the file `hello.py`. So once you're in the virtual environment and installed `Flask`, run the following command: `export FLASK_APP=hello.py`. If you rename `hello.py` or want to use a different file as the entrypoint, you'll have to run `export FLASK_APP={FILENAME}` and replace `{FILENAME}` with the correct filename to make sure the app runs.
7. Once you have everything setup, you should be able to run `flask run` and your server should start listening. Go to a browser at `localhost:5000` and you should see your app running.
