from ShazamAPI import Shazam
import youtube_dl
import os
import PythonYoutube
from moviepy.editor import *
from pydub import AudioSegment
import math
import sys

class Rick():
	def __init__(self,url,file_way,temp_file_way,char1):
		self.url = url
		self.file_way = file_way
		self.temp_file_way = temp_file_way
		self.char1= char1

	def RickRollChecker(self):

		file156 = open(self.file_way+"\\rickrollpast.txt", "r+", encoding="utf-8")
		ExRicks = [i for i in file156.readlines()]

		url=self.url

		if url in ExRicks:
			return True

		os.chdir(self.file_way)
		song_there = os.path.isfile('control.mp3')
		try:
			if song_there:
				os.remove('control.mp3')
		except PermissionError:
			print("Wait for the current playing music to end or use the 'stop' command")
		ydl_opts = {
					'format': 'bestaudio/best',
					'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '192',
					}],
				}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		for file in os.listdir("./"):

			if file.endswith(".mp3"):
				os.rename(file, "control.mp3")

		self.audio_download()
		os.chdir(self.temp_file_way)

		for file in os.listdir("./"):
			if file.endswith(".mp3"):
				value = self.ShazamRick(ExRicks=ExRicks,file156=file156,rick_file_nm=file)
				if value == True:
					print("Bu rickroll")

					sys.exit()


		youtube_link = PythonYoutube.YoutubeCommentFounder(url)

		isThisRick = youtube_link.CommentGetter()

		if isThisRick:
			print("RickRoll detected")
			return True
		else:
			print("No Rickroll")
			return False

	def audio_download(self):
		sFile = AudioSegment.from_mp3(file="control.mp3")

		total_minute = math.ceil(sFile.duration_seconds/60)
		for i in range(0,total_minute,1):
			split_fl = str(i)+"_"+"control.mp3"
			self.audio_split(sFile,i,i+1,split_fl)

			if i == total_minute-1:
				pass

	def audio_split(self,audio_name,start_min,end_min,new_filename):
		st = start_min*60000
		et = end_min*60000
		splt_aud = audio_name[st:et]
		splt_aud.export(self.temp_file_way+"\\"+new_filename,format="mp3")


	def delete_audio(self):
		os.chdir(self.temp_file_way)
		for file in os.listdir("./"):
			if file.endswith(".mp3"):
				os.remove(file)

	def ShazamRick(self, ExRicks : list,file156,rick_file_nm):
		url = self.url
		mp3_file_content_to_recognize = open(rick_file_nm, 'rb').read()

		shazam = Shazam(mp3_file_content_to_recognize)
		recognize_generator = shazam.recognizeSong()
		while True:
			asas = str(next(recognize_generator))

			if 'Rick' in asas or 'Astley' in asas :
				ExRicks.append(url)
				for i in ExRicks:
					file156.write(i)
				file156.close()
				return True
			else:
				return False