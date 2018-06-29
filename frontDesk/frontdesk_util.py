from tts import speak
from imagecapture import capture_image
from sendemail import send_email

speech_flag = True
candid = "dummy"
y_res = "dummy"
new_cand_flag = True


def front_response(user_message):
    global candid
    global y_res
    global new_cand_flag
    if hi_test(user_message):
        # speak("Hello, Welcome to JP Morgan Chase & Co., please provide your candidate Id (in format e.g. JPM12345):", speech_flag)
        # return "please provide your candidate Id (in format e.g. JPM12345):"

        speak("Hello, Welcome to J P Morgan Chase Recruitment Drive", speech_flag)
        speak("Are you a new candidate, or returning candidate and want to know previous interview feedback ? type (new/returned)", speech_flag)
        return "Are you a new candidate or returning candidate and want to know previous interview feedback ? type (new/returned)?"
    elif new_returning_candidate_test(user_message) in ["n","r"]:
        speak("Please provide your candidate Id (in format e.g. JPM12345), you can find your Candidate Id in the interview invitation email sent by our recruitment team.", speech_flag)
        return "Please provide your candidate Id (in format e.g. JPM12345):"
    elif new_returning_candidate_test(user_message)=="r":
        speak("Please wait... while I fetch your interview feedback..", speech_flag)
        speak("Your interview was conducted by Mr. Alice White, you have cleared the interview, please wait for your next round, recruitment team will call your name. Thankyou!", speech_flag)
        return "Your interview was conducted by Mr. Alice White, you have cleared the interview, please wait for your next round, recruitment team will call your name. Thankyou!"
    elif candidateid_test(user_message):
        candid = user_message
        speak("your candidate Id is " + candid, speech_flag)
        if new_cand_flag:
            speak("I am sending email to recruitment team to inform about your arrival, are you ok if I attach your photo? type (y/n)", speech_flag)
            return "I am sending email to recruitment team to inform about your arrival, are you ok if I attach your photo? type (y/n)"
        else:
            speak("Please wait... while I fetch your interview feedback..", speech_flag)
            speak("Your interview was conducted by Mr. Alice White, you have cleared the interview, please wait for your next round, recruitment team will call your name. Thankyou!", speech_flag)
            return "Your interview was conducted by Mr. Alice White, you have cleared the interview, please wait for your next round, recruitment team will call your name. <br>Thankyou!"
    elif yes_test(user_message) == "y":
        y_res = user_message
        speak("Please wait while I capture your photo, keep your head still and smile!!.......", speech_flag)
        capture_image(candid)
        speak("Please wait while I send email to the recruitment team.......", speech_flag)
        send_email(candid, True)
        speak("Recruitment team has been informed about your arrival. Your interview will start in about 20 minutes. Please be seated in the waiting area, recruitment team will call your name. Thankyou!", speech_flag)
        return "Recruitment team has been informed about your arrival.<br>Your interview will start in about 20 minutes.<br>Please be seated in the waiting area, recruitment team will call your name. <br>Thankyou!"
    elif yes_test(user_message) == "n":
        speak('No Problem, I have not captured your photo.', speech_flag)
        speak("Please wait while I send email to the recruitment team.......", speech_flag)
        send_email(candid, False)
        speak("Recruitment team has been informed about your arrival. Your interview will start in about 20 minutes. Please be seated in the waiting area, recruitment team will call your name. Thankyou!", speech_flag)
        return "Recruitment team has been informed about your arrival.<br>Your interview will start in about 20 minutes.<br>Please be seated in the waiting area, recruitment team will call your name.<br>Thankyou!"
    else:
        speak("Sorry, I am not trained for this input...", speech_flag)
        return "Sorry, I am not trained for this input..."


def hi_test(user_message):
    if user_message in ['Hi', 'hi', 'HI', 'hI']:
        return True
    else:
        return False


def candidateid_test(user_message):
    if "JPM" in user_message or "jpm" in user_message:
        return True
    else:
        return False


def yes_test(user_message):
    if user_message in ["y", "Y"]:
        return "y"
    elif user_message in ["n", "N"]:
        return "n"

def new_returning_candidate_test(user_message):
    global new_cand_flag
    if user_message in ["returned", "Returned", "RETURNED"]:
        new_cand_flag = False
        return "r"
    elif user_message in ["new", "New", "NEW"]:
        new_cand_flag = True
        return "n"
