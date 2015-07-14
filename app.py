from flask import Flask, request, render_template, redirect, flash
import cv2 ,os
import numpy as np
import Image
import urllib2, urllib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html',page="home", percent = 0, image1 = "//:0", image2 = "//:0")
	elif request.method == 'POST':
		if 'image1' in request.form:
			image1 = request.form['image1']
			app.logger.info(repr(image1))
		if 'image2' in request.form:
			image2 = request.form['image2']
			app.logger.info(repr(image2))

		# image urls stored in image1 & image2	
		try:
			f = open('image1.jpg','wb')
			f.write(urllib.urlopen(image1).read())
			f.close()

			f = open('image2.jpg','wb')
			f.write(urllib.urlopen(image2).read())
			f.close()	
		except:
			app.logger.info("Unable to convert Image")

		##code for comparing
		if image1 and image2:
			img_rgb = cv2.imread('image1.jpg')
			img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
			template = cv2.imread('image2.jpg',0)
			w, h = template.shape[::-1]

			res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
			threshold = 0.8
			loc = np.where( res >= threshold)
			for pt in zip(*loc[::-1]):
				cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
			percent =abs(max_val*100)

			if percent >= 98:
				sim = "Excatly Similar"
			elif percent >=50:
				sim = "Almost Similar"
			elif percent >= 10:
				sim = "Not much similar"
			else:
				sim = "Completely Different Images"

		else: 
			app.logger.info("image not found")

		return render_template('index.html',page="home",percent = percent, sim = sim,image1 = image1, image2 = image2)

if __name__ == '__main__':
    app.run(debug=True)
