#include<stdio.h>
#include<wiringPi.h>
int main()
{
	int i;
	if(wiringPiSetup()==-1) return -1;

	pinMode(21,OUTPUT);
	digitalWrite(21,1);
	delay(1000);
	return 0;
}
