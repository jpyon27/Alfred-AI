from RealtimeSTT import AudioToTextRecorder
import assistant
import time
import action

if __name__ == '__main__':
    recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en", post_speech_silence_duration=0.1)
    # create recorder variable to constanly listen to mic and transcribes to txt
    
    hot_words = ["alfred"] # array for hotwords
    skip_hotword_check = False
    
    print("Awaiting command for Alfred...")
    while True: #loop to keep listening
        current_text = recorder.text() #everything user says
        print(current_text) #shows in termal everything being said
        
        # if the hotword is in current_text looping for hot_word in original variable
        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hotword_check:
            if current_text: # check if there is a current text
                print("User: " + current_text) # what is going to be said to assistant
                recorder.stop() # assistant will stop listening while ai is talking
                
                current_text = current_text + " " + time.strftime("%Y-m-%d %H-%M-%S") # get time
                response = assistant.directive_to_memory(current_text)
                print(response)
                speech = response.split('#')[0]
                done = assistant.get_tts(speech)
                skip_hotword_check = True if "?" in response else False
                if len(response.split('#')) > 1:
                    cmd = response.split('#')[1]
                    action.parse_cmd(cmd)
                
                recorder.start()