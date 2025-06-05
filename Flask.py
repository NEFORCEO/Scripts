from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/ru")
def hello():
 return """
 <html>
 <head>
   <title>🐍Мой сайт</title>
   <style>
   body {
  background-color: #18ffff;
  font-size: 30px;
  margin: 100px;
  padding: 0;
}
   h1 {
   text-align: center;
   color: black;
   padding: 0px;
   }
   p { 
   font-size: 40px;
   text-align: center;
   color: black;
   }
   
   a {
  display: flex;
  justify-content: flex-end;
  align-items: flex-start; 
  }
   </style>
 </head>
 
 <body>
 <h1>Никита Нефоров</h1>
 <p>Python разработчик</p>
 <a href="http://127.0.0.1:5000/en">🇱🇷EN</a>
 
 
 </body>
 </html>
 """
 




 
if __name__ == "__main__":
 app.run(debug=True)

