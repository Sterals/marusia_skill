from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
	return'<h1>Heroku Deploy</h1>'

@app.route("/marusya", methods=['POST', 'GET'])
def marusya():
	return "Marusya"

@app.route("/main", methods=['POST', 'GET'])
def main():
	logging.info("Request: %r", request.json)
	card = {}
	buttons = []

	if request.json['session']['new']:
		text = "Привет! Назови любые несколько чисел, а я продолжу! Например: один, два, шесть!"
	elif request.json['request']['command'] == 'on_interrupt':
		text = 'Приходи еще изучать последовательность! Пока!'
	elif request.json['request']['command'] == 'debug':
		text = json.dumps(request.json)
	elif request.json['request']['command'] == 'играть':
		text = "Отлично! Попробуй угадай следующее число: 1, 4, 9, 16, 25..."
		card = {
				"type": "BigImage",
				"image_id": 457239017,
				"title": "Угадай последовательность",
				"description": "Угадай последовательность",
			} 
		buttons = [{'title':"36"}, {"title":"49"}]
	else:
		text = request.json['request']['command']
	response = {
		"version":request.json['version'],
		'session':request.json['session'],
		"response": {
			"end_session": False,
			"text" : text,
			"card" : card, 
			'buttons' : buttons 
		}

	}
	logging.info("response %r", response)

	return json.dumps (response, ensure_ascii=False, indent=2)

if __name__ == '__main__':
	app.run(debug=True)