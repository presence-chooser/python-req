from flask import Flask, jsonify, request
import deff_time
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def helloWorld():
   if request.method == 'GET':
      res = deff_time.realtime()
      return (jsonify(res))
   if request.method == 'POST':
      reza2 = deff_time.reza()
      return (jsonify(reza2))
      
      
@app.route('/cpuusage', methods=['GET','POST'])
def time2():
   if request.method == 'GET':
      res = deff_time.cpuusage()
      return (jsonify(res))
      
#
      
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)