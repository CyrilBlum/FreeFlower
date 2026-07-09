---
layout: default
title: SFTP-Upload-Anleitung für Webtechnologien
parent: Technische Seiten
nav_order: 3
permalink: /sftp-upload-anleitung.html
---

# SFTP-Upload-Anleitung für Webtechnologien

Diese Anleitung zeigt, wie Sie Ihre Website per SFTP auf den Kursserver hochladen und online verfügbar machen.

---

## 1. Was ist SFTP?

SFTP (SSH File Transfer Protocol) ist ein sicheres Protokoll zum Hochladen von Dateien auf einen Server. Ihre Daten und Ihr Passwort sind dabei verschlüsselt und sicher.

---

## 2. Installation: Cyberduck

Verwenden Sie **Cyberduck**, einen kostenlosen SFTP-Client.

**macOS:**
```bash
brew install --cask cyberduck
```

**Windows:**
```powershell
winget install -e --id iterateGmbH.Cyberduck --scope machine --silent --accept-package-agreements --accept-source-agreements
```

*(FileZilla ist eine Alternative mit ähnlicher Bedienung.)*

---

## 3. Verbindung einrichten

Öffnen Sie Cyberduck und erstellen Sie eine neue Verbindung mit diesen Daten:

| Feld | Wert |
|------|------|
| **Protokoll** | SFTP (SSH File Transfer Protocol) |
| **Server** | `webproj.in-form-atik.ch` |
| **Port** | 22 |
| **Benutzername** | `user1` (oder user2, user3, …) |
| **Passwort** | [von der Lehrperson] |

Speichern Sie die Verbindung für späteren Zugriff.

![CyberDuck-Settings](./assets/images/sftp/cyberduck.png)


---

## 4. Dateien hochladen

Nach dem Verbinden befinden Sie sich in Ihrem Benutzerverzeichnis. Laden Sie hier alle Dateien hoch:

1. **Drag & Drop:** Ziehen Sie Ihre Dateien in das Cyberduck-Fenster
2. **Alternativ:** Rechtsklick > «Datei hochladen»

**Wichtig:** Laden Sie alles direkt in Ihr Verzeichnis hoch, nicht in einen Unterordner.

---

## 5. index.html ist Pflicht

Die Startseite **muss** `index.html` heissen (kleingeschrieben, mit `.html`-Endung), sonst funktioniert nichts.

Falsch:
- `Start.html` / `Home.html` / `index.htm` / `INDEX.HTML`

---

## 6. Website aufrufen

Nach dem Upload ist Ihre Website unter dieser URL erreichbar:

```
https://webproj.in-form-atik.ch/2026/user1/
```

---

## 7. Änderungen veröffentlichen

Nach dem ersten Upload:

1. Datei lokal bearbeiten und speichern
2. Auf dem Server erneut hochladen
3. Browser aktualisieren mit `Cmd+Shift+R` (macOS) oder `Ctrl+Shift+F5` (Windows)

⚠️ Der Browser speichert alte Versionen im Cache – ein erzwungenes Neuladen hilft.

---

## 7. Typische Fehler

| Problem | Lösung |
|---------|--------|
| Dateiordner statt Website | `index.html` existiert nicht oder heisst anders |
| Bilder/CSS nicht sichtbar | Pfade prüfen: `<img src="bilder/logo.png">` und `<link href="style.css">` |
| Alte Version wird angezeigt | Browser-Cache leeren: `Cmd+Shift+R` oder `Ctrl+Shift+F5` |
| 404-Fehler | Dateien wurden nicht hochgeladen oder in falschen Ordner |
| Spezialzeichen in HTML falsch | HTML-Datei mit UTF-8 speichern, `<meta charset="UTF-8">` im `<head>` |

**Tipp:** Öffnen Sie die Entwicklertools (`F12`) im Browser – dort sehen Sie Fehler.
