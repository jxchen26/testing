from flask import Flask, render_template, request,redirect,url_for
import forms
import mlbstats
import ast

app = Flask('app')
app.config["SECRET_KEY"] = "1234"

@app.route('/', methods = ["GET","POST"])
def hello_world(data = None):

  form = forms.JsonStringInput()

  with open("data.txt", "w") as file:
      file.write("Helloworld")

#   with open("data.txt", "r") as file:
#       file_data = file.read()


  if form.validate_on_submit():
    userinput = request.form.to_dict(flat = False)["json"][0]
    endpoint= userinput.strip().split(",")[0]
    param= userinput.strip().split(",")[1]

    param = ast.literal_eval(param.strip(" "))
    print(endpoint  , type(endpoint))
    data = mlbstats.statsapi.get(endpoint,param)

    # data = mlbstats.get(endpoint,param)
    # os.system("clear")
    # mystuff.json_explorer(data)
    redirect(url_for('hello_world',data= data))

  return render_template("index.html",
                        title = "API TESTING",
                        type = type,
                        len = len,
                        bool = bool,
                        int = int,
                        str = str,
                        dict = dict,
                        list = list,
                        form = form,
                        data = data)
                        # fdata = file_data)

# app.run(debug = True)