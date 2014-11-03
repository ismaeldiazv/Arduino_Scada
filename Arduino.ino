// Declaro las variables tipo int
int sensor_temp, valor;

void setup()
{
  pinMode(2,INPUT);  // Declaro el pin 2 como entrada
  pinMode(3,OUTPUT);  // Declaro el pin 3 como salida
  Serial.begin(115200);  // Habilito el puerto serial a 115200 baudios
}

void loop()
{
  if(Serial.available()>0)  // Si hay algo en el bufer de recepcion
  {
    valor=Serial.read();  // Leemos el puerto serie
    if (valor=='a')  // Si valor es a
    {
      digitalWrite(3,HIGH);  // Pongo a 1 la salida 3
    }
    if (valor=='b')  // Si valor es b
    {
      digitalWrite(3,LOW);  // Pongo a 0 la salida 3
    }
  }
  
  sensor_temp = analogRead(A1);  // Leo el valor de la entrada analogica A1
  sensor_temp=map(sensor_temp,0,1023,0,12);  // Escalo el valor de la entrada analogica
  
  if(digitalRead(2)==true)  // Si la entrada 2 esta a 1
  {
    valor=1;
  }
  
  if(digitalRead(2)==false)
  {
    valor=0;
  }
  
  // Mando por puerto serie el string
  String var=("valor= " + String(valor) + ",sensor= "+ String(sensor_temp) + "\n");
  Serial.print(var);
  
  // Retardo de 400ms
  delay(400);
} 
