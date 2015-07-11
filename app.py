from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html',page="home")
	elif request.method == 'POST':
		if 'image1' in request.form:
			image1 = request.form['image1']
			app.logger.info(repr(image1))
		if 'image2' in request.form:
			image2 = request.form['image2']
			app.logger.info(repr(image2));

		#image urls stored in image1 & image2	
			
		return render_template('index.html',page="home")

if __name__ == '__main__':
    app.run(debug=True)
