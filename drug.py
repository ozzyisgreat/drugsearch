import requests
import json
import warnings
import os

drug = input("Drug Search: ")

warnings.filterwarnings("ignore")

r = requests.get(f"http://tripbot.tripsit.me/api/tripsit/getDrug?name={drug}", verify=False)
dat = json.loads(r.text)

os.system("clear")

if dat["err"] == True:
	print("error, drug doesnt exist")
	exit()

try:

	name = dat["data"][0]["name"]
	summary = dat["data"][0]["properties"]["summary"]
	duration = dat["data"][0]["properties"]["duration"]
	onset = dat["data"][0]["properties"]["onset"]
	aliases = dat["data"][0]["properties"]["aliases"]

	names = ""
	for i in aliases:
		names = names + i + " "

	effects = dat["data"][0]["properties"]["effects"]

	dose = dat["data"][0]["formatted_dose"]

except:
	pass


if "name" in locals():
	print(f"Name: {name}\n")

if "names" in locals():
        print(f"Aliases: {names}\n")

if "summary" in locals():
	print(f"Summary: {summary}\n")

if "dose" in locals():
        print(f"Dosage: {dose}\n")

if "effects" in locals():
        print(f"Effects: {effects}\n")

if "onset" in locals():
        print(f"Onset: {onset}\n")

if "duration" in locals():
	print(f"Duration: {duration}\n")

