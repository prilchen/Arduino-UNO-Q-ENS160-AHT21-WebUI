# Arduino-UNO-Q-ENS160-AHT21-WebUI

**Luftqualitätsmessung mit ENS160 und AHT21 - WebUI Dashboard für Arduino UNO Q**

Dieses Projekt zeigt die Leistungsfähigkeit des Arduino UNO Q durch die Kombination von Echtzeit-Sensorauslesung (MCU) und einem modernen Web-Dashboard (MPU). Luftqualitätswerte werden live über eine WebUI im Browser angezeigt.

![Arduino UNO Q](https://prilchen.de/wp-content/uploads/2025/11/image-7.png)

## 📋 Projektübersicht

Der Arduino UNO Q ist nicht einfach nur ein UNO mit neuem Namen - er verfügt über zwei "Gehirne":
- **Qualcomm Dragonwing QRB2210 Quad-Core ARM-Prozessor (MPU)** als Linux-System für clevere Aufgaben
- **Klassischer STM32U585 Mikrocontroller (MCU)** für Echtzeit-Operationen

Dieses Projekt nutzt beide Welten optimal:
1. Der **MCU** liest kontinuierlich Sensordaten aus (ENS160 für CO₂/VOC, AHT21 für Temperatur/Luftfeuchtigkeit)
2. Der **MPU** hostet einen Webserver mit Dashboard
3. Die **Arduino Bridge RPC-Bibliothek** verbindet beide Komponenten nahtlos

## ✨ Features

- 🌡️ **Temperatur- und Luftfeuchtigkeitsmessung** mit AHT21 Sensor
- 💨 **Luftqualitätsüberwachung** mit ENS160 Sensor (CO₂ und VOC)
- 🌐 **WebUI Dashboard** - Echtzeit-Anzeige im Browser
- 🔄 **Automatische Updates** alle 5 Sekunden
- 🎯 **MCU/MPU Bridge** - C++ und Python arbeiten Hand in Hand
- 📊 **REST API** für externe Abfragen
- 🔌 **WebSocket** für Live-Updates

## 🏗️ Projektstruktur

```
Arduino-UNO-Q-ENS160-AHT21-WebUI/
├── sketch/
│   └── sketch.ino          # C++ Sketch für MCU (Sensorauslese)
├── python/
│   └── main.py        # Python Webserver für MPU
├── assets/
│   └── index.html     # WebUI Dashboard
└── README.md          # Diese Datei
```

## 🔧 Hardware-Anforderungen

- **Arduino UNO Q** (Version mit 2GB/16GB oder 4GB/32GB)
- **ENS160 Luftqualitätssensor** (I2C)
- **AHT21 Temperatur-/Feuchtigkeitssensor** (I2C)
- Netzteil: USB-C 5V 5A (z.B. Raspberry Pi Netzteil)
- Optional: USB-C Hub mit HDMI für direkten Betrieb

### Verkabelung

| Sensor Pin | Arduino UNO Q Pin |
|------------|------------------|
| SDA        | D20 (SDA)        |
| SCL        | D21 (SCL)        |
| VCC        | 3.3V             |
| GND        | GND              |

## 📚 Bibliotheken

Folgende Arduino-Bibliotheken werden benötigt:
- `Wire.h` - I2C Kommunikation
- `SparkFun_ENS160.h` - ENS160 Sensor
- `Adafruit_AHTX0.h` - AHT21 Sensor
- `ArduinoBridge.h` - MCU/MPU Kommunikation

## 🚀 Installation und Verwendung

### Vorbereitung

1. **Arduino App Lab** installieren und Linux-Image auf dem UNO Q aktualisieren:
   - [Arduino App Lab Getting Started](https://docs.arduino.cc/software/app-lab/tutorials/getting-started/)
   - [Flashing a New Image to the UNO Q](https://docs.arduino.cc/tutorials/uno-q/update-image/)

2. **Neue App erstellen** in Arduino App Lab unter "My Apps"

3. **Dateien hinzufügen**:
   - `sketch.ino` im Root-Verzeichnis
   - `python/main.py` im python-Ordner
   - `assets/index.html` im assets-Ordner

4. **Bibliotheken hinzufügen** in App Lab:
   - SparkFun_ENS160
   - Adafruit_AHTX0
   - ArduinoBridge

5. **WebUI Brick** hinzufügen für Web-Interface Support

### Starten der Anwendung

1. In der App Lab auf den **Run**-Button klicken
2. Die Anwendung wird kompiliert und gestartet
3. WebUI ist erreichbar unter: `http://<IP-Adresse-des-UNO-Q>/`
4. Die IP-Adresse wird in der App Lab angezeigt

### Alternative: SSH Zugriff

Für erweiterte Konfiguration per SSH verbinden:
```bash
ssh arduino@<ip-adresse>
# oder mit Hostname:
ssh arduino@prilchensq.local
```

## 💻 Funktionsweise

### MCU (Mikrocontroller) - sketch.ino

Der Arduino Sketch läuft auf dem STM32U585 MCU und:
- Initialisiert die I2C-Sensoren (ENS160 und AHT21)
- Liest alle 2 Sekunden Messwerte aus
- Sendet Daten via **Bridge.notify()** an den MPU

```cpp
Bridge.notify("record_air_quality", co2, voc);
```

### MPU (Prozessor) - main.py

Das Python-Script läuft auf dem Quad-Core ARM CPU und:
- Empfängt Sensordaten über die Arduino Bridge
- Hostet einen Webserver mit WebUI
- Stellt REST API bereit (`/air_quality`)
- Sendet Live-Updates via WebSocket an verbundene Clients

### WebUI - index.html

Das Dashboard im Browser:
- Zeigt CO₂ und VOC Werte in Echtzeit an
- Aktualisiert sich automatisch alle 5 Sekunden
- Responsives Design für Desktop und Mobile
- Zeitstempel der letzten Aktualisierung

![Luftqualität Dashboard](https://prilchen.de/wp-content/uploads/2025/11/Bildschirmfoto-2025-11-09-um-15.42.32.png)

## 📖 Tutorial und weitere Informationen

Dieses Projekt basiert auf dem ausführlichen Tutorial:

**[Arduino Next Level – Der UNO Q](https://prilchen.de/arduino-next-level-der-uno-q/)**

Das Tutorial behandelt:
- Einführung in die Dual-Architektur des Arduino UNO Q
- Erste Schritte mit Arduino IDE und App Lab
- LED Matrix Anzeige als Alternative
- Mini-PC Betrieb mit Debian Linux
- Remote-Zugriff und SSH-Konfiguration

### Weitere Arduino UNO Q Projekte

1. **[LED Matrix Scrolltext](../Arduino-UNO-Q-LED-Matrix-Scrolltext)** - Laufschrift auf der 12x8 LED Matrix
2. **[ENS160/AHT21 LED Matrix](../Arduino-UNO-Q-ENS160-AHT21-LED-Matrix)** - Sensorwerte als Lauftext anzeigen

## 🔍 Sensoren-Details

### ENS160 - Luftqualitätssensor
- **CO₂ Äquivalent (eCO₂)**: 400-65000 ppm
- **Total Volatile Organic Compounds (TVOC)**: 0-65000 ppb
- **I2C Adresse**: 0x53 (Standard)
- Betriebsspannung: 3.3V

### AHT21 - Temperatur- und Feuchtigkeitssensor
- **Temperaturbereich**: -40 bis +85°C (±0.3°C Genauigkeit)
- **Feuchtigkeitsbereich**: 0-100% RH (±2% Genauigkeit)
- **I2C Adresse**: 0x38 (Standard)
- Betriebsspannung: 3.3V

## 🛠️ Bekannte Probleme und Lösungen

### Problem: Serieller Monitor zeigt nichts an
Dies ist ein bekanntes Problem in frühen Versionen. **Lösung**: LED Matrix zur Visualisierung verwenden (siehe zweites Projekt).

### Problem: Assets-Ordner fehlt
Beim Hinzufügen des WebUI Brick wird manchmal der assets-Ordner nicht erstellt.
**Lösung**: Manuell über File Manager oder per SSH anlegen:
```bash
mkdir -p /ArduinoApps/co2-monitor/assets
```

## 🌟 Erweiterungsmöglichkeiten

- 📊 Datenlogging mit Zeitreihen-Diagrammen
- 🚨 Alarm-Benachrichtigungen bei schlechter Luftqualität
- 📱 Mobile App Integration
- 🏠 Smart Home Integration (MQTT, Home Assistant)
- 🤖 KI-basierte Vorhersagen
- ☁️ Cloud-Upload der Messwerte

## 📚 Referenzen

- [Arduino UNO Q Dokumentation](https://docs.arduino.cc/hardware/uno-q/)
- [Arduino App Lab](https://docs.arduino.cc/software/app-lab/tutorials/getting-started/)
- [UNO Q Benutzerhandbuch](https://docs.arduino.cc/tutorials/uno-q/user-manual/)
- [Prilchen's Blog](https://prilchen.de/)

## 📝 Lizenz

Dieses Projekt ist Open Source und steht unter der MIT-Lizenz.

## 🤝 Beiträge

Verbesserungsvorschläge und Pull Requests sind willkommen!

## ✍️ Autor

**Prilchen**  
🌐 [prilchen.de](https://prilchen.de/)  
📺 [YouTube](https://www.youtube.com/@prilchen)  
🐦 [TikTok](https://www.tiktok.com/@prilchen.de)

---

*Erstellt mit dem Arduino UNO Q - Where MCU meets MPU! 🚀*
