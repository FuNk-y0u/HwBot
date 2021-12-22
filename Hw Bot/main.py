import discord 
import random
import json
from datetime import date


client = discord.Client()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="hw"))
	print("Loged in as {0.user}".format(client))

@client.event

async def on_message(message):
	if message.author == client.user:
		return	
	if message.content.startswith("!hws"):
		with open("hws.json", "r") as json_file:
			file = json.load(json_file)

		if message.content == "!hws":
			if str(date.today()) in file:
				await message.channel.send(f'''
```
HWS OF {str(date.today())}
SOCIAL:{file[str(date.today())]["social"]}
HPE:{file[str(date.today())]["hpe"]}
COMPUTER:{file[str(date.today())]["comp"]}
OPT:{file[str(date.today())]["Optional.M"]}
ENGLISH:{file[str(date.today())]["Eng"]}
NEPALI:{file[str(date.today())]["Nep"]}
SCIENCE:{file[str(date.today())]["Sci"]}
MATHS:{file[str(date.today())]["Maths"]}
```
''')
			else:
				await message.channel.send("Incorrect date format, Hws of the date doesnot contain in data base or Data base hasnt been updated")

		else:
			msg = message.content
			msg = msg.split(" ")
			constDate = msg[1]
			if constDate in file:
				await message.channel.send(f'''
```
HWS OF {constDate}
SOCIAL:{file[constDate]["social"]}
HPE:{file[constDate]["hpe"]}
COMPUTER:{file[constDate]["comp"]}
OPT:{file[constDate]["Optional.M"]}
ENGLISH:{file[constDate]["Eng"]}
NEPALI:{file[constDate]["Nep"]}
SCIENCE:{file[constDate]["Sci"]}
MATHS:{file[constDate]["Maths"]}
```
''')
			else:
				await message.channel.send("Incorrect date format, Hws of the date doesnot contain in data base or Data base hasnt been updated")
	

	if message.content.startswith("!add"):
		if str(message.author) == "FuNk#1817" or str(message.author) == "067#9370":
			with open("hws.json", "r") as json_file: 
				file = json.load(json_file)
			msg2 = message.content.split(",")
			hw_update = {"social":msg2[1],"hpe":msg2[2],"comp":msg2[3],"Optional.M":msg2[4],"Eng":msg2[5],"Nep":msg2[6],"Sci":msg2[7],"Maths":msg2[8]}
			file.update({str(date.today()):hw_update})
			with open('hws.json', 'w') as json_file:
				json.dump(file,json_file) 
			await message.reply("Hws added sucessfully") 

		

	if message.content.startswith("!copy"):
		msg3 = message.content
		msg3 = msg3.split(" ")
		subject = msg3[1].lower()
		with open("copies.json", "r") as json_file:
			file = json.load(json_file)
		if subject in file:
			try:
				await message.channel.send(file[subject]["file"])
			except:
				await message.channel.send("Hw hasnt been uploaded!")

	if message.content.startswith("!cadd"):
		msg4 = message.content
		msg4 = msg4.split(" ")
		subject = msg4[1].lower()
		pdf = msg4[2]
		with open("copies.json","r") as json_file:
			file = json.load(json_file)
		copy_update = {"file":pdf}
		file.update({subject:copy_update})
		with open("copies.json","w") as json_file:
			json.dump(file,json_file)
		await message.channel.send("Copies added sucessfully")



			 

client.run("")

