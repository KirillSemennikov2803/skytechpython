from flask import Flask,render_template,request

app = Flask(__name__)
def TheWays(start,end):
    #нужно вставить определитель всех точек и вернуть их массивом
    return [start,end]

def setApi(point):
    points =""
    for i in range(0,len(point)):
        points+="waypoint"+str(i)+":"+""+str(point[i])+""
        if i != len(point) -1:
            points +=","
    return points
@app.route('/')
def hello_world():
    return render_template("choose.html")
@app.route('/map',methods = ['POST'])
def map():
  data=request.form
  point = TheWays(data['start'],data['end'])
  points = setApi(point)


  return render_template("map/demo.html",points=points)

if __name__ == '__main__':
    app.run()
