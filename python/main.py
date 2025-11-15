from arduino.app_utils import App, Bridge, Logger
from arduino.app_bricks.web_ui import WebUI
import time

# Logger initialisieren
logger = Logger("air-quality-dashboard")
logger.info("Starte Luftqualitäts-App...")

# WebUI starten
web_ui = WebUI()

# Globale Datenstruktur für aktuelle Werte
latest_data = {
    "co2": None,
    "voc": None,
    "timestamp": None
}

# REST-API-Endpunkt für JSON-Abruf
web_ui.expose_api("GET", "/air_quality", lambda: latest_data)
logger.info("API-Endpunkt /air_quality bereitgestellt")

# WebSocket: sende Daten bei Verbindung
def on_client_connect(sid):
    logger.debug(f"Client verbunden: {sid}")
    web_ui.send_message("air_quality", latest_data)

web_ui.on_connect(on_client_connect)


# Bridge-Funktion vom Mikrocontroller
def record_air_quality(co2: int, voc: int):
    logger.debug(f"Empfangen: CO₂={co2} ppm, VOC={voc} ppb")
    latest_data["co2"] = co2
    latest_data["voc"] = voc
    latest_data["timestamp"] = time.time()

    try:
        web_ui.send_message("air_quality", latest_data)
        logger.debug("Werte an WebUI gesendet")
    except Exception as e:
        logger.warning(f"WebUI-Sendung fehlgeschlagen: {e}")

# Bridge registrieren
Bridge.provide("record_air_quality", record_air_quality)
logger.info("Bridge-Funktion 'record_air_quality' registriert")

# App starten
App.run()
