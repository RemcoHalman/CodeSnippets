#include <SPI.h>
#include <UIPEthernet.h>
#include <PubSubClient.h>

#define CLIENT_ID "arduino-Handjes-Control"

byte mac[] = {0xE, 0xD, 0xE, 0xF, 0xE, 0xE};

// Unique static IP address of this Arduino - change to adapt to your network
IPAddress ip(192, 168, 0, 130);
// IP Address of your MQTT broker - change to adapt to your network
IPAddress server(192, 168, 0, 121);

// Handle and convert incoming MQTT messages ----------------------------------------

void callback(char *topic, byte *payload, unsigned int length)
{
    // handle message arrived
    String content = "";
    char character;
    for (int num = 0; num < length; num++)
    {
        character = payload[num];
        content.concat(character);
    }
    Serial.println(topic);
    Serial.println(content); // message sent out by button actions is returned from broker and serial printed
}

EthernetClient ethClient;
PubSubClient client(server, 1883, callback, ethClient);

void setup()

{
    // Setup serial connection
    Serial.begin(9600);

    // Setup ethernet connection to MQTT broker
    Ethernet.begin(mac, ip);
    delay(1000);
    if (client.connect(CLIENT_ID))
    { // change as desired - clientname must be unique for MQTT broker
        client.publish("arduino", "hello world - here arduino");
        Serial.println("connected");
        client.subscribe("arduino");
    }
}

//----------------------------------------------

void loop()
{
    client.loop();
}

// End of sketch ---------------------------------