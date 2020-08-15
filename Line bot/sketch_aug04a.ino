#include <BH1750.h>
#include <DHT.h>
#include <Wire.h>

#define dhtPin A1      //讀取DHT11 Data
#define dhtType DHT11 //選用DHT11   
#define SLAVE_ADDRESS 0x27

int number = 0;
int state = 0;

DHT dht(dhtPin, dhtType); // Initialize DHT sensor 
BH1750 lightMeter(0x03);

void setup() {
  pinMode(7,OUTPUT); //繼電器的接腳
  pinMode(8, OUTPUT); //溫度計的接腳
  Serial.begin(9600); // 初始化 I2C
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData); //I2C訊號接收時，啟用函式
  Wire.onRequest(sendData);  //主機要求讀取時，啟用函式
  
  lightMeter.begin();
  Serial.println(F("BH1750 Test begin"));//光照度的模組
  
  
  Serial.println("DHTxx test!");
  dht.begin();//啟動DHT
}


void loop() {

  
  delay(1000);  //延遲時間，可自行調整
  int sensorValue = analogRead(A0); //土壤濕度感測器的接腳，讀取數值
  Serial.println(sensorValue);
  if(sensorValue > 200){   //判斷是不是太乾燥了。600只是參考值，可依不同環境及土壤，設定不同的數值。
    digitalWrite(7,HIGH);   //如果太乾燥，就啟動抽水泵給水
  }else{
   digitalWrite(7,LOW);    //如果濕度夠了就停止給水
   
  }

  

  delay(1000);
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();  //取得溫度C



  //顯示在監控視窗裡
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C ");
  
}

void receiveData(int byteCount){
while(Wire.available()) {  //當I2C的buffer中有資料時進入迴圈
  number = Wire.read();   //指定nubmer 等於讀取的訊息
  Serial.print("data received: ");
  Serial.println(number);

  if (number == 1){  
    if (state == 0){
      digitalWrite(13, HIGH); // 致使 LED on
      state = 1;
    }else{
      digitalWrite(13, LOW); // 致使 LED off
      state = 0;
    }
  }
  }
}

// callback for sending data
void sendData(){
Wire.write(number);
}
