# from flask import Flask, render_template
# from file import lokal
# import time
# import pandas as pd
# import matplotlib.pyplot as plt
# import csv
# ui = Flask(__name__)



# send = []
# v = lokal() 
# for b in v:
# 	send.append(b)
# print(send)


# @ui.route("/abc")
# def abc():
# 	return render_template("abc.html", send = send)




# @ui.route("/chart")
# def chart():
# 	x = []
# 	y = []

# 	with open('output.csv','r') as csvfile:
# 		plots = csv.reader(csvfile, delimiter = ',')
	
# 		for row in plots:
# 			x.append(row[0])
# 			y.append(int(row[2]))

# 	plt.bar(x, y, color = 'g', width = 0.72, label = "Age")
# 	plt.xlabel('Names')
# 	plt.ylabel('Ages')
# 	plt.title('Ages of different persons')
# 	plt.legend()
# 	plt.show()
# 	return render_template('chart.html')






# @ui.route('/home')
# def weather_dashboard():
#     filename = 'output.csv'
#     data = pd.read_csv(filename, header=0)
#     myData = list(data.values)
#     return render_template('home.html', myData=myData)





# import matplotlib.pyplot as plt
# import csv

# x = []
# y = []

# with open('output.csv','r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter = ',')
	
# 	for row in plots:
# 		x.append(row[0])
# 		y.append(row[1])

# plt.bar(x, y, color = 'g', width = 0.72, label = "Age")
# plt.xlabel('Names')
# plt.ylabel('Ages')
# plt.title('Ages of different persons')
# plt.legend()
# plt.show()










# @ui.route("/form")
# def form():
# 	return render_template("form.html")

if __name__ == "__main__":
	ui.run(debug=True)