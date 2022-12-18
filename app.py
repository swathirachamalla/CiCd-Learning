from flask import Flask,render_template,request
app = Flask(__name__) 

@app.route('/hello')
def helloworld():
    return "Hello world"
if __name__ == "__main__":
     app.run(debug=True)