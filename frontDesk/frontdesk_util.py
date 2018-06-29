from tts import speak
from imagecapture import capture_image
from sendemail import send_email

speech_flag = True
candid = "dummy"
y_res = "dummy"


def front_response(user_message):
    global candid
    global y_res
    if hi_test(user_message):
        speak("please provide your candidate Id (in format e.g. JPM12345):", speech_flag)
        return "please provide your candidate Id (in format e.g. JPM12345):"
    elif candidateid_test(user_message):
        candid = user_message
        speak("your candidate Id is " + candid, speech_flag)
        speak("Shall I take your Photo and send to Recruitment team to inform about your arrival ? select (y/n)", speech_flag)
        return "Shall I take your Photo and send to Recruitment team to inform about your arrival ? select (y/n)"
    elif yes_test(user_message) == "y":
        y_res = user_message
        speak("Please wait while we capture your photo, keep your head still and smile!!.......", speech_flag)
        capture_image(candid)
        speak("Please wait while we send email to the recruitment team.......", speech_flag)
        send_email(candid, True)
        speak("Thankyou, Recruitment team has been informed about your arrival. Your interview will start in about 20 mintes. Please be seated in the waiting area, recruitment team will call your name.", speech_flag)
        return "Thankyou, Recruitment team has been informed about your arrival.<br>Your interview will start in about 20 mintes.<br>Please be seated in the waiting area, recruitment team will call your name."
    elif yes_test(user_message) == "n":
        speak('No Problem! we have not captured your photo.', speech_flag)
        speak("Please wait while we send email to the recruitment team.......", speech_flag)
        send_email(candid, False)
        speak("Thankyou, Recruitment team has been informed about your arrival. Your interview will start in about 20 minutes. Please be seated in the waiting area, recruitment team will call your name.", speech_flag)
        return "Thankyou, Recruitment team has been informed about your arrival.<br>Your interview will start in about 20 minutes.<br>Please be seated in the waiting area, recruitment team will call your name."
    else:
        speak("Sorry, I am not trained for this input...", speech_flag)
        return "Sorry, I am not trained for this input..."


def hi_test(user_message):
    if user_message in ['Hi', 'hi', 'HI', 'hI']:
        return True
    else:
        return False


def candidateid_test(user_message):
    if "JPM" in user_message:
        return True
    else:
        return False


def yes_test(user_message):
    if user_message in ["y", "Y"]:
        return "y"
    elif user_message in ["n", "N"]:
        return "n"
