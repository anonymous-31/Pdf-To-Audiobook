import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
book = open('mindset.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page= pdfreader.getPage(31)
text = page.extractText()
print(text)
# speaker.say("text")
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
speaker.setProperty('rate', 125)
voices = speaker.getProperty('voices')       #getting details of current voice
speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female 
pyttsx3.speak(text)
speaker.runAndWait()
