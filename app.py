from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return "Hello, World! My Azure Web App is working!"
 
if __name__ == "__main__":
    app.run()
