from flask import Flask,render_template, url_for
from file import lokal
import matplotlib.pyplot as plt
import csv
import pandas as pd
import time

main = Flask(__name__)

print(lokal())
# APPEND STOCKS DATA
# send = []
# v = lokal() 
# for b in v:
# 	send.append(b)
# print(send)



# ABC ROUTE TEMPLATE
@main.route("/abc")
def abc():
	return render_template("abc.html", send = send)


# HOME ROUTE TEMPLATE SHOW STOCKS DATA

@main.route('/home')
def weather_dashboard():
    filename = 'output.csv'
    data = pd.read_csv(filename, header=0)
    myData = list(data.values)
    return render_template('home.html', myData=myData)



# FORM ROUTE HTML TEMPLATE
@main.route("/form")
def form():
	return render_template("form.html")




# MATPLOTLIB GRAF CODE
  
# x = []
# y = []
  
# with open('data.csv','r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#     	x.append(row[0])
#     	y.append((row[1]))
  
# plt.plot(x, y, color = 'green', linestyle = 'dashed',marker = 'o',
#          label = "Stocks Data")
  
# plt.xticks(rotation =40)
# plt.xlabel('X_xsiz')
# plt.ylabel('Y_xsiz')
# plt.title('Stocks Report', fontsize = 50)
# plt.savefig('static/images/Stocks.jpg', bbox_inches='tight',pad_inches=2,transparent=True)
# plt.grid()
# plt.legend()
# plt.show()




# SHOW MY MATPLOTLIB GRAF AND SELECT DIFFERENT OPTIONS FORM AND STOCKS DATA ROUTE HTML TEMPLATE
@main.route('/image')  
def image():
	filename = 'output.csv'
	data = pd.read_csv(filename, header=0)
	myData = list(data.values)
	return render_template("image.html" , myData=myData)  
 



if __name__ == '__main__':
	main.run(debug=True)
