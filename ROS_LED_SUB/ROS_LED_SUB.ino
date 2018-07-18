#include <ros.h>
#include <std_msgs/UInt16.h>
//#include <string.h>

ros::NodeHandle nh;
const int motorIn1 = 4;
const int motorIn2 = 5;
const int motorIn3 = 6;      
const int motorIn4 = 7;
const int DELAY = 100;

void led_cb( const std_msgs::UInt16 & led_msg){
  
switch(led_msg.data){
    case 56:
      forward();
      break;
    case 53:
      backward();
      break;
    case 52:
      left();
      break;
    case 54:
      right();
      break;
    default:
      motorstop();
      break;    
  
    }
  
  
 
}  

ros::Subscriber<std_msgs::UInt16> sub("chatter", led_cb);

void setup() {
  pinMode(13, OUTPUT);
  pinMode(motorIn1, OUTPUT);
  pinMode(motorIn2, OUTPUT);
  pinMode(motorIn3, OUTPUT);
  pinMode(motorIn4, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);

}

void loop() {
  nh.spinOnce();
  delay(1);

}

void motorstop()
{
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
  digitalWrite(motorIn3, LOW);
  digitalWrite(motorIn4, LOW);
  
}

void forward()
{
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
  digitalWrite(motorIn3, HIGH);
  digitalWrite(motorIn4, LOW);
  delay(DELAY);
  motorstop();
}

void backward()
{
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, HIGH);
  digitalWrite(motorIn3, LOW);
  digitalWrite(motorIn4, HIGH);
  delay(DELAY);
  motorstop();
}

// Let right motor keep running, but stop left motor
void right()
{
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
  digitalWrite(motorIn3, LOW);
  digitalWrite(motorIn4, LOW);
  delay(DELAY);
  motorstop();
}

// Let left motor keep running, but stop right motor
void left()
{
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
  digitalWrite(motorIn3, HIGH);
  digitalWrite(motorIn4, LOW);
  delay(DELAY);
  motorstop();
}
