"""
NeuroGames Logging System
"The palest ink is better than the best memory" - Chinese Proverb

Dieses Modul implementiert ein umfassendes Logging-System für das NeuroGames-Projekt.
Referenzen: base (Anforderungen 1-6), VERSION.md (Versionstracking)
"""

import logging  # Standard-Bibliothek für Logging-Funktionalität
import os  # Betriebssystem-Interaktionen für Dateipfade
import datetime  # Datum und Zeit für Zeitstempel
from typing import Optional  # Type-Hints für optionale Parameter

class NeuroGamesLogger:
    """
    Zentrale Logging-Klasse für das NeuroGames-Projekt
    Referenz: base Zeile 1-3 (Kommentierungsanforderungen)
    """
    
    def __init__(self, log_file: str = "neurogames.log", log_level: int = logging.INFO):
        """
        Initialisiert den Logger mit Datei und Level
        
        Args:
            log_file (str): Pfad zur Log-Datei - Standard: "neurogames.log"
            log_level (int): Logging-Level - Standard: logging.INFO
            
        Referenz: base Zeile 2 (selbsterklärende Kommentare)
        """
        self.log_file = log_file  # Speichert den Dateipfad für Log-Ausgabe
        self.log_level = log_level  # Definiert minimales Logging-Level
        self.logger = self._setup_logger()  # Initialisiert Logger-Instanz
    
    def _setup_logger(self) -> logging.Logger:
        """
        Konfiguriert und erstellt Logger-Instanz
        
        Returns:
            logging.Logger: Konfigurierte Logger-Instanz
            
        Referenz: base Zeile 4 (maximal 50 Zeilen), private Methode für Setup
        """
        # Erstellt neuen Logger mit eindeutigem Namen
        logger = logging.getLogger(f"NeuroGames_{id(self)}")
        
        # Setzt Logging-Level (siehe __init__ Parameter)
        logger.setLevel(self.log_level)
        
        # Verhindert doppelte Handler bei mehreren Instanzen
        if not logger.handlers:
            
            # Erstellt Datei-Handler für Log-Datei (self.log_file)
            file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
            
            # Erstellt Konsolen-Handler für Terminal-Ausgabe
            console_handler = logging.StreamHandler()
            
            # Definiert Format für Log-Nachrichten mit Zeitstempel
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            
            # Wendet Formatter auf beide Handler an
            file_handler.setFormatter(formatter)  # Für Datei-Ausgabe
            console_handler.setFormatter(formatter)  # Für Konsolen-Ausgabe
            
            # Fügt Handler zum Logger hinzu
            logger.addHandler(file_handler)  # Datei-Logging aktivieren
            logger.addHandler(console_handler)  # Konsolen-Logging aktivieren
        
        return logger  # Gibt konfigurierten Logger zurück
    
    def info(self, message: str) -> None:
        """
        Loggt Info-Nachricht
        
        Args:
            message (str): Zu loggende Nachricht
            
        Referenz: base Zeile 1 (jede Zeile kommentiert)
        """
        self.logger.info(message)  # Schreibt Info-Level Nachricht
    
    def warning(self, message: str) -> None:
        """
        Loggt Warnung
        
        Args:
            message (str): Warn-Nachricht
            
        Referenz: Standard Logging-Level für Warnungen
        """
        self.logger.warning(message)  # Schreibt Warning-Level Nachricht
    
    def error(self, message: str) -> None:
        """
        Loggt Fehler-Nachricht
        
        Args:
            message (str): Fehler-Beschreibung
            
        Referenz: Für Fehlerbehandlung im NeuroGames-Projekt
        """
        self.logger.error(message)  # Schreibt Error-Level Nachricht
    
    def debug(self, message: str) -> None:
        """
        Loggt Debug-Information
        
        Args:
            message (str): Debug-Details
            
        Referenz: Für Entwicklung und Troubleshooting
        """
        self.logger.debug(message)  # Schreibt Debug-Level Nachricht
    
    def log_game_event(self, event_type: str, player_id: Optional[str] = None, 
                       details: Optional[str] = None) -> None:
        """
        Spezielle Methode für NeuroGames-Events
        
        Args:
            event_type (str): Art des Spielereignisses
            player_id (Optional[str]): Spieler-ID falls vorhanden
            details (Optional[str]): Zusätzliche Event-Details
            
        Referenz: base (NeuroGames-spezifische Anforderungen)
        """
        # Erstellt strukturierte Event-Nachricht
        event_msg = f"GAME_EVENT: {event_type}"  # Basis-Event-Info
        
        # Fügt Spieler-ID hinzu falls vorhanden (siehe player_id Parameter)
        if player_id:
            event_msg += f" | Player: {player_id}"
        
        # Ergänzt Details falls verfügbar (siehe details Parameter)
        if details:
            event_msg += f" | Details: {details}"
        
        # Loggt das strukturierte Game-Event
        self.info(event_msg)  # Verwendet info-Methode (Zeile 78-85)
    
    def get_log_stats(self) -> dict:
        """
        Gibt Statistiken über Log-Datei zurück
        
        Returns:
            dict: Log-Datei Statistiken
            
        Referenz: base Zeile 6 (Versions-Tracking-Unterstützung)
        """
        stats = {}  # Initialisiert leeres Statistik-Dictionary
        
        # Prüft ob Log-Datei existiert (self.log_file aus __init__)
        if os.path.exists(self.log_file):
            # Ermittelt Dateigröße in Bytes
            stats['file_size'] = os.path.getsize(self.log_file)
            
            # Zählt Zeilen in Log-Datei
            with open(self.log_file, 'r', encoding='utf-8') as f:
                stats['line_count'] = sum(1 for _ in f)  # Effizientes Zeilenzählen
            
            # Letzte Änderungszeit der Datei
            mod_time = os.path.getmtime(self.log_file)  # Unix-Timestamp
            stats['last_modified'] = datetime.datetime.fromtimestamp(mod_time)
        else:
            # Standard-Werte wenn Datei nicht existiert
            stats['file_size'] = 0  # Keine Datei = 0 Bytes
            stats['line_count'] = 0  # Keine Datei = 0 Zeilen
            stats['last_modified'] = None  # Keine Datei = kein Änderungsdatum
        
        return stats  # Gibt Statistik-Dictionary zurück

# Global verfügbare Logger-Instanz für das gesamte Projekt
# Referenz: base (zentrale Logging-Lösung), VERSION.md (Projekt-Standard)
default_logger = NeuroGamesLogger()

# Convenience-Funktionen für schnellen Zugriff
# Referenz: base Zeile 2 (selbsterklärende Funktionsnamen)
def log_info(message: str) -> None:
    """Schnelle Info-Logging Funktion - verwendet default_logger"""
    default_logger.info(message)  # Delegiert an globale Logger-Instanz

def log_error(message: str) -> None:
    """Schnelle Error-Logging Funktion - verwendet default_logger"""
    default_logger.error(message)  # Delegiert an globale Logger-Instanz

def log_game_event(event_type: str, player_id: Optional[str] = None, 
                   details: Optional[str] = None) -> None:
    """Schnelle Game-Event Logging Funktion - verwendet default_logger"""
    # Verwendet default_logger.log_game_event (Zeilen 101-121)
    default_logger.log_game_event(event_type, player_id, details)

def main() -> None:
    """
    Hauptfunktion für Log-Modul
    
    Kann über 'import log; log.main()' aufgerufen werden
    Referenz: base (Benutzeranforderung für einfache Verwendung)
    """
    # Initialisiert und testet Logger-Funktionalität
    log_info("NeuroGames Logger durch log.main() gestartet")  # Start-Nachricht
    
    # Demonstriert verschiedene Log-Level
    log_info("INFO: Logger erfolgreich initialisiert")  # Info-Level Test
    default_logger.warning("WARNING: Test-Warnung")  # Warning-Level Test
    default_logger.debug("DEBUG: Debug-Information")  # Debug-Level Test
    
    # Zeigt Game-Event-Logging
    log_game_event("SYSTEM_START", "system", "Log-System aktiviert")  # System-Event
    log_game_event("TEST_EVENT", "admin", "Logger-Test durchgeführt")  # Test-Event
    
    # Gibt aktuelle Log-Statistiken aus
    stats = default_logger.get_log_stats()  # Holt Log-Datei Statistiken
    print(f"\n=== Log-Statistiken ===")  # Header für Statistik-Ausgabe
    print(f"Dateigröße: {stats.get('file_size', 0)} Bytes")  # Zeigt Dateigröße
    print(f"Zeilen: {stats.get('line_count', 0)}")  # Zeigt Zeilenzahl
    print(f"Letzte Änderung: {stats.get('last_modified', 'Unbekannt')}")  # Änderungszeit
    
    # Bestätigung der erfolgreichen Initialisierung
    log_info("Log-System erfolgreich getestet und bereit")  # Abschluss-Nachricht
    print("\nLog-System ist einsatzbereit!")  # Konsolen-Bestätigung

# Beispiel-Verwendung bei direktem Aufruf
# Referenz: base Zeile 4 (maximal 50 Zeilen pro Änderung)
if __name__ == "__main__":
    # Ruft main-Funktion auf wenn Datei direkt ausgeführt wird
    main()  # Verwendet die neue main-Funktion (Zeilen 162-182)