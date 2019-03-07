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
