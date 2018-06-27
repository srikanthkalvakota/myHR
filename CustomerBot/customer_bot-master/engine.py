#Murali
intent_response_dict = {
    "intro": ["I am a  Phoenix Chatbot who can respond to your HR and Recruitment related queries"],
    "greet":["Hey","Hello","Hi","Howdy"],
    "goodbye":["Bye","It was nice talking to you","See you","cu later"],
    "affirm":["Great","I know you would like it"],
	"event-name":["Please provide PF link", "minimum years of experience for testing and QA"]

}

reqinfo_response_dict = {
    "Recruitment": "a@1234ltd Recruitment services",
    "req_link":'You can requirement at <a href="http://recruitment/a@1234ltd/developer/reqid=12345</a>',
	"event-name":"Please provide PF link, minimum years of experience for testing and QA"
}

hr_query_value_dict = {
    "pf":"pf link, pf password",
    "finance":"pay slips, tax computation",
	"event-name":"Please provide PF link, minimum years of experience for testing and QA"
}
def hr_info(entities):
    if entities == None:
        return "Could not find out specific information about this ..." +  reqinfo_response_dict["req_link"]
    if len(entities) == 1:
        return reqinfo_response_dict[entities[0]]
    return "Sorry.." + reqinfo_response_dict["faq_link"]

def req_query(entities):
    if entities == None:
        return "Could not query this ..." + reqinfo_response_dict["req_link"]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        if qtype == "event_name":
            return hr_query_value_dict[qval]

        return reqinfo_response_dict[entities[0]]
    return "Sorry.." + reqinfo_response_dict["req_link"]