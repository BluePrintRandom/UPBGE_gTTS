"""
Copyright <2020> <Jacob Merrll / BluePrintRandom1@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import bpy,pip,subprocess,bge, aud
own = bge.logic.getCurrentController().owner

if bge.logic.getCurrentController().sensors['Always'].positive or bge.logic.getCurrentController().sensors['Play'].positive:
    pybin = bpy.app.binary_path_python
    subprocess.check_call([pybin, '-m', 'pip', 'install', 'gTTS'])    
    print('installed gTTS')

    from gtts import gTTS   
    
     
    # Controls all audio that plays during game

    if not bge.logic.getCurrentController().sensors['Play'].positive:
        tts = gTTS('Good morning.',lang='en-au',slow=True)
    else:
         tts = gTTS(own['input'],lang='en-uk',slow=True)
            
        
    tts.save('hello.mp3')
    if 'device' not in own:
        device = aud.Device()
        own['device']=device
    else:
        device =   own['device']  
    factory = aud.Sound.file('hello.mp3')
    handle = device.play(factory)
    handle.pitch =1.25

    
    
    
    
    
