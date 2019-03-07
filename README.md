# ChatBot_Weather
###### A simple chatBot that tells us the real time Humidity and Temperature via Sensor Connected to NodeMCU and local Host

### Measuring Temperature and Humidity
We used the following Components for measuring the temperature and humidity of the surrounding:-

- DHT-11 Sensor
- NodeMCU

NodeMCU is a module having a wifi module ESP8266 and associated circuit with it which helps to transfer any connected sensor data to any other device. ESP8266 has a microcontroller with wifi. With the help of Jumper wire, we connect the NodeMCU with the DHT-11 sensor(temperature and humidity measuring sensor) to measure the values of temperature and humidity of the surroundings.

This setup is connected to a PC/laptop in which the code for measuring both the temperature of humidity using the DHT library is present. The other libraries used are WifiClient, ESP8266 and ThingSpeak. The details of the wifi through which data will be uploaded is entered in the code and the Channel Key and the API Key available through the ThingSpeak’s website is entered in the code. The code is uploaded on NodeMCU and the sensors start generating and uploading the data to the cloud.

### Cloud Storage - Thingspeak
ThingSpeak is a free web service that lets you collect and store sensor data in the cloud and develop Internet of Things applications. We are using Thingspeak as temporary cloud storage. On the ThingSpeak channel, two fields are created one for temperature and the other for humidity. All the live data is stored on Thingspeak channel and from there it is fetched using Thingspeak API and displayed to the user accordingly.

### Interface - Website
For interface, we are using a web app built with the use of HTML, CSS and JavaScript. Initial conversation with the user is hardcoded into the interface. Data from Thingspeak is fetched with the help of the REST API of Thingspeak. The data is received in JSON format which is converted accordingly to the use. Once the user asks for weather conditions he is presented with a graphical representation of the current weather conditions as measured by the sensor and uploaded on Thingspeak. 
