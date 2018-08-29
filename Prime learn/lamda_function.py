def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "whatismotivationalquotes":
        return fun_math(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to motivational quotes! " \
                    "You can know interesting facts about motivational quotes by saying Tell me about motivational quotes
    repromptText =  "You can know interesting facts about motivational quotes by saying Tell me about motivational quotes"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def quotes(intent, session):
    import random
    index = random.randint(0,len(q)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "quotes that is actually a math fact is that " + q[index] 
    repromptText = "You can know interesting facts about motivational quotes by saying Tell me motivational quotes"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using prime learn Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



q =[ "Motivation is the reason for people's actions,desires and needs.",
" Motivation is one's direction to behavior or what causes a person to want to repeat a behavior.",
"It is an important part of human psychology. It arouses a person to act towards a desired goal.It is a driving force which promotes action.",
"The process of motivation consists of three stages.First, a felt need. Second,a stimulus in which the need is to be aroused and third, when needs are satisfied the satisfaction of goals.",
"Good,better,best.Never let it rest.Til your good is better and your better is best.It help us in achieving the aims of our lives.",
"Life is ten percent what happens to you and ninty percent how you react. This help us in knowing our inner weakness and working on it to be better in our life.",
"Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence."

        ]
