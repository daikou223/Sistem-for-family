from mainapp import app
from flask import render_template,request,send_file
import random
idr = ""
ret_deta = {}

@app.route("/") #ここから開始
def reqrogin():
	return render_template("rogin.html",s = 0) #rogin.htmlへ移動



@app.route("/user",methods = ["POST"]) #ID,Passwordを入力後実行される
def  maind():
	global idr,ret_deta
	files = open("file.txt","r")
	ret_deta = {}
	for k in files:
		al = k.split()
		ret_deta[al[0]] = al[1]
	files.close()
	print(ret_deta)
	passes = {"001":"cX041","002":"m7MIZ","003":"rlrUq","004":"K0GVE",}
	idr = request.form["ID"]
	passw = request.form["Pass"]
	if idr in passes:
		if passes[idr] == passw:
			return render_template("user.html",user = id,corrent = ret_deta)
		else:
			return render_template("rogin.html",s = 1)
	else:
		return render_template("rogin.html",s = 1)


@app.route("/dir",methods = ["POST"])
def newdir():
	return render_template("new.html")

@app.route("/retarn",methods = ["POST"])
def retarn():
	global idr,ret_deta
	files = open("file.txt","w")
	ret_deta[idr] = "1"
	for lines in ["001","002","003","004"]:
		b = lines + " " + ret_deta[lines]
		files.write(b + "\n")
	return render_template("user.html",user = id,corrent = ret_deta)


@app.route("/goto",methods = ["POST"])
def goto():
	global idr,ret_deta
	files = open("file.txt","r")
	ret_deta = {}
	for k in files:
		al = k.split()
		ret_deta[al[0]] = al[1]
	files.close()
	print(idr)
	files = open("file.txt","w")
	ret_deta[idr] = "0"
	print(ret_deta)
	for lines in ["001","002","003","004"]:
		b = lines + " " + ret_deta[lines]
		files.write(b + "\n")
	return render_template("user.html",user = id,corrent = ret_deta)	

	
	
	
	


