"""
NeuroGames Hauptprogramm
"In the beginning was the Word, and the Word was with Code" - Anonymous

Haupteinstiegspunkt für das NeuroGames-Projekt mit vollständigem Logging
Referenzen: log.py (Logging-System), VERSION.md (Aktuelle Version 1.1.0)
"""

import log  # Importiert unser eigenes Logging-Modul (siehe log.py)
import sys  # System-spezifische Parameter und Funktionen
import traceback  # Für detaillierte Fehlerbehandlung

def main():
    """
    Hauptfunktion des NeuroGames-Projekts
    
    Referenz: base Zeile 1-3 (Kommentierungsanforderungen)
    """
    # Startet Anwendung mit Info-Log (verwendet log.py Zeile 144)
    log.log_info("=== NeuroGames Anwendung gestartet ===")
    
    try:
        # Loggt Spielstart-Event (verwendet log.py Zeile 151-154)
        log.log_game_event("APPLICATION_START", None, "Hauptprogramm initialisiert")
        
        # Hier würde Ihre Hauptlogik stehen
        simulate_game_flow()  # Simuliert Spielablauf (siehe Funktion unten)
        
        # Erfolgreicher Abschluss
        log.log_info("Anwendung erfolgreich beendet")  # Info-Level Logging
        
    except Exception as e:
        # Fehlerbehandlung mit detailliertem Logging
        error_msg = f"Kritischer Fehler: {str(e)}"  # Erstellt Fehlermeldung
        log.log_error(error_msg)  # Error-Level Logging (log.py Zeile 147)
        
        # Loggt vollständigen Stacktrace für Debugging
        log.log_error(f"Stacktrace: {traceback.format_exc()}")
        
        # Beendet mit Fehlercode (Exit Code 1)
        sys.exit(1)

def simulate_game_flow():
    """
    Simuliert einen typischen NeuroGames Spielablauf
    
    Referenz: base Zeile 4 (maximal 50 Zeilen), demonstriert Log-Verwendung
    """
    # Simuliert Spieler-Login
    player_id = "player_demo_123"  # Beispiel Spieler-ID
    log.log_game_event("PLAYER_LOGIN", player_id, "Spieler angemeldet")
    
    # Simuliert Spielstart
    log.log_game_event("GAME_START", player_id, "Neues Spiel begonnen")
    
    # Simuliert Spielaktionen
    for round_num in range(1, 4):  # Drei Spielrunden
        # Loggt jede Runde (round_num aus for-loop)
        log.log_game_event("ROUND_START", player_id, f"Runde {round_num} gestartet")
        
        # Simuliert Rundenergebnis
        score = round_num * 100  # Beispiel-Punktzahl
        log.log_game_event("ROUND_END", player_id, f"Runde {round_num} beendet, Punkte: {score}")
    
    # Spielende
    log.log_game_event("GAME_END", player_id, "Spiel abgeschlossen")
    
    # Zeigt Log-Statistiken
    show_log_statistics()  # Siehe Funktion unten

def show_log_statistics():
    """
    Zeigt aktuelle Log-Statistiken an
    
    Referenz: log.py Zeile 123-144 (get_log_stats Methode)
    """
    # Holt Statistiken vom Logger (log.py default_logger)
    stats = log.default_logger.get_log_stats()
    
    # Loggt Statistik-Informationen
    log.log_info(f"Log-Datei Größe: {stats.get('file_size', 0)} Bytes")
    log.log_info(f"Anzahl Log-Einträge: {stats.get('line_count', 0)} Zeilen")
    
    # Zeigt letzte Änderung falls verfügbar
    if stats.get('last_modified'):
        log.log_info(f"Letzte Änderung: {stats['last_modified']}")

# Programmstart - wird nur ausgeführt wenn Datei direkt gestartet wird
# Referenz: log.py Zeile 156-161 (ähnliches __name__ Pattern)
if __name__ == "__main__":
    main()  # Startet Hauptfunktion (siehe Zeile 12-35)
