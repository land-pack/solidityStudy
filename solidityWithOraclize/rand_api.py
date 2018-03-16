import random
import json
from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/hello', methods = ['GET'])
def api_hello():
    rand_number = random.sample([1,2,3,4,5,6,7,8,9,10], 4)
    print 'generate a rand number ==>', rand_number
    data = {
        'name'  : 'lottery',
        'number' : '-'.join([str(i) for i in rand_number])
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

if __name__ == '__main__':
	app.run(debug=True, port=5611)
