from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
	bmi = 0.0
	if request.method == 'POST' and 'weight' in request.form :
		weight = float(request.form.get('weight'))
		height_cm = float(request.form.get('height'))
		height_m = height_cm/100;
		bmi = weight/(height_m*height_m)
	return render_template('index.html', bmi=bmi)
app.run()