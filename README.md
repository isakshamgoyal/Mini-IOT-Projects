# ChatBot_Weather
###### A simple chatBot that tells us the real time Humidity and Temperature via Sensor Connected to NodeMCU and local Host

### Measuring Temperature and Humidity
We used the following Components for measuring the temperature and humidity of the surrounding:-

- DHT-11 Sensor
- NodeMCU

NodeMCU is a microcontroller with wifi module ESP8266 present On-board.Once connected to a power source and hotspot, to provide internet connection it can be used to transfer data to any cloud platform. We uploaded the Channel ID and WRITE_API_KEY of our ThingSpeak channel to the NodeMCU. Using this Channel ID and WRITE_API_KEY, the data collected from DHT11 sensor is uploaded on ThingSpeak.


Temperature of humidity is measured via DHT11 Module using the DHT library. The other libraries used are WifiClient, ESP8266 and ThingSpeak. The code is uploaded on NodeMCU and the sensors start generating and uploading the data to the cloud.

### Cloud Storage - ThingSpeak
ThingSpeak is an open-source IoT application that stores and retrieves data using HTTP protocol over a local network. In our chatbot, thingspeak is used to collect data.
We created two fields on the ThingSpeak channel one for temperature and the other for humidity. All the live data is stored on Thingspeak channel and from there it is fetched using Thingspeak API using the READ_API_KEY and displayed to the user accordingly.

### Web FrameWork - Flask 
Flask is a micro web framework. It supports various extensions that works as if it's part of it and provide multiple functionalities such as upload handling, form validation etc. 
Here we have used flask as server which handles the GET and POST requests from the webhooks of facebook messenger inorder to provide response to the user. Data from Thingspeak is fetched with the help of the REST API of Thingspeak. 
The data is received in JSON format which is converted according to the use. Once the user asks for weather conditions the current weather conditions as measured by the sensor and uploaded on Thingspeak are replied to the user.

### Natural Language Interface - Wit.ai
Wit.ai is an interface that is used as an interaction tool by developers to make apps interact with humans. With the help of this we can develop applications to which humans can talk or text to.
The same thing has been deployed on our chatbot. Using wit.ai our chatbot converts natural language into structured data that is used to determine what has been asked. Here the chatbot uses a trained wit.ai API to identify the following keywords:
‘temp ‘, ‘temperature’, etc. for Temperature.
‘Hum’, ‘humidity’, etc. for Humidity.
And similarly for greetings
Whenever the bot receives a message it is a JSON object which is then received by our app. From this the sender's id and the message is fetched by the app. The message received is in the text form which is then sent to the witIntegration file. This returns a different entity each for the keywords present in the message. Based on the entity, humidity and temperature data is retrieved from the sensor file. (Here by entity we mean an object that consists of the identifying keyword).

### Interface - Facebook Messenger
We integrated our ChatBot to the facebook messenger in order to help user interact to the chatbot easily with installing any extra app(Only in case if he has a facebook ID)


# Installation and Bot Setup

This file will walk you through the steps to setup your bot. Download the entire folder and the follow the steps below.

## Step 1: Install required packages

Install the required packages listed in the requirements.txt file. To install the required packages, please use the code below. I might have missed some packages to include in the requirements.txt file. __When you initiate the bot, it might fail that a particular module does not exist. Please install it and then initiate bot again, which will fix the issue.__

```sh
pip3 install -r requirements.txt
```
It would be recommended to use Python 3.5.x or 3.6.x version for this project. 

## Step 2: Create a Wit.ai account and train your bot for keywords

You can train for any keyword you like for. After that Go to Settings> Copy the Server Access Token.
Replace the Server access token in the WitIntegraion.py file to that of yours.

## Step 3: Creating a ThingSpeak account

Create a ThingSpeak account.
Create a new Channel and create 2 Fields.
Copy the CHANNEL ID and WRITE_API_KEY and replace them in the Arduino File(DHT11.ino).
Copy the CHANNEL ID and READ_API_KEY and replace them in the sensor.py file.

## Step 4: Install ngrok

Look at the URL mentioned below to download and launch the server at port 5000.

https://dashboard.ngrok.com/get-started


## Step 5: Create Facebook Messenger Bot 

Please follows the instructions in the link below to create and Integrate the chatBot with the Fasebook messenger.

https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-facebook?view=azure-bot-service-4.0

Copy the URL from ngrok terminal and paste it in the Callback URL and Verify_token from the app.py file.

## Step 6: Initiate Bot

Navigate to the folder where the app.py script exists and run the code below.

```sh
python3 app.py
```
This launches the Flask Server at port 5000 and allows user to interact with the bot via facebook messenger.
