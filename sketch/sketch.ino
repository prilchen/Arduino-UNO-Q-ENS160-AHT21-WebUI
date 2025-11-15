#include <Wire.h>
#include <SparkFun_ENS160.h>
SparkFun_ENS160 ens160;

void setup() {
  Wire.begin();
  Bridge.begin();
  ens160.begin();
  ens160.setOperatingMode(SFE_ENS160_RESET);
  delay(100);
  ens160.setOperatingMode(SFE_ENS160_STANDARD);
}

void loop() {
  if (ens160.checkDataStatus()) {
    int co2 = ens160.getECO2();
    int voc = ens160.getTVOC();
    Bridge.notify("record_air_quality", co2, voc);
  }
  delay(2000);
}
