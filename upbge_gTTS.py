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
    device = aud.Device()
    factory = aud.Sound.file('hello.mp3')
    handle = device.play(factory)
    handle.pitch =1.25

    
    
    
    
    
