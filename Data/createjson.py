import json
import os
with open("data.txt","r") as f :
	# try:
	x = f.read()
	print(len(x))
	jsonData = {}
	if len(x) != 0 :
		jsonData = eval(x)
		
	f.close()
	#windows ppl make forward slash to backward
	os.remove(os.getcwd()+"/data.txt")
	print(jsonData)
	


		
	
	while True:
		mode = input("Enter i to insert d to delete v to view e to exit")
		if mode == "i":
			question = input("Enter qs: ")
			answer = input("Enter ans: ")
			source = input("Enter source :")
			jsonData[question] = {"answer":answer, "source":source}
			

		elif mode == "d":
			word = input("Enter first word of question to delete")
			for key in jsonData.keys() :
				if key.split(' ')[0] == word:
					del jsonData[key]
			json.dump(jsonData, f)
		elif mode == "v":
			print(json.dumps(jsonData, indent=4))

		elif mode == "e":
			# os.remove(os.getpwd()+"/data.json")
			with open("data.txt", "w+") as ff:
				ff.write(str(jsonData))

			break
		else:
			print("Pls try again....")
	# except:
	# 	with open("error.json", "w+") as ff:
	# 		json.dump(jsonData, ff)


	print("Bye")