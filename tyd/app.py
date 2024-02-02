from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls and mention the caller's city"""

    # Get the caller's information from Twilio's request to our app

    pais_origen = request.values['FromCountry']
    pais_destino= request.values['ToCountry']
    incoming_number = request.values['From']

    print("Pais origen: " + pais_origen)
    print("Incoming Number: " + incoming_number)
    print("Pais destino: " + pais_destino)


    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say('tu pais es, {}!'.format(pais_origen))

    # Play an audio file for the caller
    resp.play('https://demo.twilio.com/docs/classic.mp3')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
