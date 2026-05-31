from flask import Flask, app, render_template, request, jsonify
import google.generativeai as genai
app = Flask(__name__)



# Create the model object
model = genai.GenerativeModel(
        "gemini-2.5-flash",
system_instruction=
         ( "You are a helpful assistant that answers questions in a concise and informative manner. "
         )
         )
genai.configure(api_key="AIzaSyDk9dvwN00HO_YgeCjhWzomsPY5aaW78mQ")
@app.route("/ask", methods=["POST"])

def ask():
        user_input = request.json.get("question")
        response = model.generate_content(user_input)   
        return jsonify({"answer": response.text})
    
    



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "<h1> Login Successful </h1>"
    else:
        return render_template("index.html")
    

if  __name__ == "__main__":
    app.run(debug=True)