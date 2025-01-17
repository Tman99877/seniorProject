from flask import Flask, render_template, request
import os           
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER



@app.route("/")
def Display_IMG():
     storage = os.path.join(app.config['UPLOAD_FOLDER'], 'storage.jpg')
     return render_template("homepage.html", user_image=storage)



@app.route("/")                
def home():                    
    return render_template("homepage.html")

@app.route("/CPU")
def Open_IMG():
     ryzen = os.path.join(app.config['UPLOAD_FOLDER'], 'ryzen.jpg')
     return render_template("CPU.html", user_image=ryzen)


@app.route("/CPU")                
def CPU():                    
    return render_template("CPU.html")

@app.route("/GPU")
def Show_IMG():
     rtx4090 = os.path.join(app.config['UPLOAD_FOLDER'], 'rtx4090.png')
     return render_template("GPU.html", user_image=rtx4090)


@app.route("/GPU")                
def GPU():                    
    return render_template("GPU.html")



@app.route("/ram")
def view_IMG():
     ram = os.path.join(app.config['UPLOAD_FOLDER'], 'ram.jpg')
     return render_template("ram.html", user_image=ram)


@app.route("/ram")                
def ram():                    
    return render_template("ram.html")



@app.route("/ps")
def wide_IMG():
     ps = os.path.join(app.config['UPLOAD_FOLDER'], 'ps.jpg')
     return render_template("ps.html", user_image=ps)


@app.route("/ps")                
def ps():                    
    return render_template("ps.html")
                                        
                                           
    
if __name__== "__main__":
    app.run(debug=True,port=8080,use_reloader=False)
