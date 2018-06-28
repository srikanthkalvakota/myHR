import cv2
from imagecapture import capture_image
from sendemail import send_email
from tts import speak

speech_flag = True

print("Hello, welcome to JP Morgan Chase & Co. (Say 'Hi' to begin) ")
speak("Hello, welcome to JP Morgan Chase & Co. (Say 'Hi' to begin) ", speech_flag)

input()

print("please provide your candidate Id :")
speak("please provide your candidate Id :", speech_flag)
candid = input()
speak(candid, speech_flag)

# send email, photo to HR, interviewer intimating candidate has arrived.
print("Shall I take your Photo and send to Recruitment team to inform about your arrival ? select (y/n)")
speak("Shall I take your Photo and send to Recruitment team to inform about your arrival ? select (y/n)", speech_flag)
res = input()
speak(res, speech_flag)

print("Please wait while we capture your photo, keep your head still and smile!!.......")
speak("Please wait while we capture your photo, keep your head still and smile!!.......", speech_flag)

if res == 'y':
    capture_image(candid)

    print("Please wait while we send email to the recruitment team.......")
    speak("Please wait while we send email to the recruitment team.......", speech_flag)

    send_email(candid)
else:
    print('\nNo Problem! we have not captured your photo.')
    speak('\nNo Problem! we have not captured your photo.', speech_flag)

print("\nThankyou, Recruitment team has been informed about your arrival")
print("Your interview will start in about 20 mintes.")
print("Please be seated in the waiting area, recruitment team will call your name.")

speak("\nThankyou, Recruitment team has been informed about your arrival.", speech_flag)
speak("Your interview will start in about 20 mintes.", speech_flag)
speak("Please be seated in the waiting area, recruitment team will call your name.", speech_flag)
