from gtts import gTTS
import os
text1 = 'Good Morning Students. Today we are going to study about Logic gate Logic gates are electronic circuits that take one or more inputs and give only one output.And the relationship between these inputs and output is based on some logic.Some commonly known logic gates are OR gate, AND gate, NOR gate etc...The output of OR gate is high if at least one of the inputs is high the output of AND gate is low if at all there an input which is low The output of nor gate is opposite to the input. If input is low output will be high and vice versa.That’s it for today we will meet in the next class.'
language = 'en'
myobj = gTTS(text=text1, lang=language, slow=False)
myobj.save("ibmclass.mp3")
os.system("mpg321 ibmclass.mp3")
