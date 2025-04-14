####################### DEPENDENCIES ########################

############# FOR RUNNING POPPY.EXE BY ITSELF ###############
		Python Packages:
			None! They are all installed in the .exe file thanks to PyInstaller!!!
			
		Other Dependencies:
			Flac utility: https://xiph.org/flac/download.html
			FFMpeg: https://phoenixnap.com/kb/ffmpeg-windows 

		With Flac and FFMpeg installed everything should work fine. Just double click poppy.exe to start her up!
		
	
	
######## FOR RUNNING POPPY.PY SOURCE CODE IN AN IDE #########
		Python Packages: (pip install <package name>)
			PyAudio
			SpeechRecognition
			pydub
			gtts
			pyjokes
			webbrowser

		Other Dependencies:
			Python: https://www.python.org/downloads/
			flac utility: https://stackoverflow.com/questions/65939571/installing-flac-command-line-tool-on-windows
			FFMpeg: https://phoenixnap.com/kb/ffmpeg-windows

		With all of those installed, along with a Python interpreter, you just have to run Poppy.py she she should just work!




########################## USAGE ############################

	When you first run Poppy, she will give you an intro message, and then begin silently listening to your microphone in the background.
	In order to talk to her and give her commands, you need to activate her by saying "Hey Poppy."
	Once you do, you can give her one of several commands.
	
	Available commands:
		"Help" or "List Commands": 	Poppy will list out all of her available commands.
		"Hello" or "Hi": 			Poppy will say hello back.
		"Time": 					Poppy will tell you the current time and date.
		"Set a timer for...": 		Poppy will look for a specified number of hours, minutes, and seconds in the same command, and set a timer for that length of time. (ex: "Set a timer for 2 hours 30 minutes and 10 seconds") NOTE: I plan to edit this a bit in the future to make it a bit more robust and work if someone says something like "Set a timer for 2 and a half hours." I also plan to make it so she still listens to you while the timer is going.
		"Joke": 					Poppy will tell you a random computer tech joke from the PyJokes library
		"Search for...": 			Poppy will open a browser window and search for whatever is following the words "Search for"
		"Show me...": 				Poppy will open a browser window and search for pictures of whatever is following the words "Search for"
		"Never Mind" or "Nothing": 	Poppy will go back to listening silently and wait for you to say her activation phrase "Hey Poppy" again.
		"Shut Down":				Poppy will shut down entirely and stop listening to your microphone.
		
