---
layout: default
title: GitHub einrichten
parent: Technische Seiten
nav_order: 3
permalink: /github-setup.html
---

# GitHub einrichten

Diese Seite führt Sie Schritt für Schritt durch die grundlegende Einrichtung von GitHub, Git und SSH für ein neues Projekt.

## Git installieren

Öffnen Sie ein Terminal (MacOS) bzw. PowerShell (Windows, muss als Administrator ausgeführt werden) und installieren Sie Git mit dem passenden Befehl für Ihr System.

MacOS:
```bash
brew install git
```

Windows:
```bash
winget install --id Git.Git -e --source winget
```

Prüfen Sie danach die Installation mit:

```bash
git --version
```

## GitHub-Account erstellen

Öffnen Sie [github.com](https://github.com) und klicken Sie auf Sign up. Folgen Sie den Schritten, um einen neuen Account zu erstellen.


> 🏆 Challenge: SSH-Schlüssel erstellen und hinterlegen
>
> Damit Sie Änderungen später ohne Passwortabfrage zu GitHub pushen können, erstellen Sie ein SSH-Schlüsselpaar und hinterlegen den Public Key auf GitHub.
> Führen Sie diese Befehle im Terminal aus (**ersetzen Sie zuvor die Email-Adressse durch Ihre echte Email-Adresse**):
> ```bash
> ssh-keygen -t ed25519 -C "vorname.nachname@stud.edu.zh.ch" # SSH-Schlüsselpaar erstellen
> ```
> Danach müssen Sie den öffentlichen Schlüssel aus der Datei `~/.ssh/id_ed25519.pub` kopieren. Nutzen Sie dafür diesen Befehl:
>
>Für MacOS/Linux:
>```bash
>pbcopy < ~/.ssh/id_ed25519.pub
>```
>Für Windows:
>```bash
>cat ~/.ssh/id_ed25519.pub | clip
>```
>
>
>Kopieren Sie den ausgegebenen Public Key und fügen Sie ihn auf GitHub unter Settings > SSH and GPG keys > New SSH key ein.
>
>Testen Sie danach die Verbindung:
>
>```bash
>ssh -T git@github.com
>```
>
>Sollte eine Willkommensnachricht von GitHub erscheinen, die bestätigt, dass die Verbindung funktioniert.

## Git konfigurieren

Setzen Sie einmalig Ihren Namen und Ihre E-Mail-Adresse, damit Commits korrekt zugeordnet werden.

```bash
git config --global user.name "Vorname Nachname"
git config --global user.email "vorname.nachname@stud.edu.zh.ch"
```

## Neues Repository anlegen

Erstellen Sie auf GitHub über das Plus-Symbol oben rechts ein neues Repository. Wählen Sie einen passenden Namen und entscheiden Sie, ob das Repository public oder private sein soll.

## Projekt vorbereiten

Wechseln Sie in den Ordner Ihres Projekts und legen Sie eine passende `.gitignore` an. Darin sollten Dateien und Ordner ausgeschlossen werden, die nicht versioniert werden sollen, zum Beispiel:

```
__pycache__/ # Python-Cache-Ordner
*.pyc # Python-Cache-Dateien
.venv/ # Virtuelle Umgebung
.DS_Store # macOS-spezifische Datei 
.vscode/ # VS Code-Einstellungen
```

## Initialisieren, committen und pushen

Wenn Ihr lokales Projekt noch nicht mit Git verbunden ist, führen Sie diese Befehle aus:

```bash
git init
git add .
git commit -m "Erster Commit"
git branch -M main
git remote add origin git@github.com:<user>/<repo>.git
git push -u origin main
```

Falls das Repository bereits auf GitHub existiert, ist das Klonen oft der sauberste Start.

## Im Alltag arbeiten

Öffnen Sie Ihr Projekt in VS Code, ändern Sie Dateien lokal und verwenden Sie die Source-Control-Ansicht zum Stagen, Committen und Pushen. Vor dem Arbeiten ist ein `git pull` sinnvoll, damit Sie den aktuellen Stand aus dem Remote-Repository haben.

Ein typischer Ablauf sieht so aus:

```bash
git status
git add .
git commit -m "Kurze, aussagekräftige Nachricht"
git push
```

All diese Schritte können direkt in VS Code mit der Source-Control-Ansicht durchgeführt werden. Vor jedem commit können alle Änderungen überprüft und gezielt gestaged werden.

![GitHub in VS Code](assets/images/git/github-vscode.png)

## Allgemeine Tipps

- Schreiben Sie klare, aussagekräftige Commit-Nachrichten.
- Committen Sie häufig, damit Änderungen nachvollziehbar bleiben.
- Nutzen Sie Branches für neue Features oder größere Änderungen, um die Hauptentwicklungslinie stabil zu halten.
- Ziehen Sie regelmäßig Änderungen vom Remote-Repository, um Konflikte zu vermeiden.

# GitHub Issues und Projects
## Task-Listen mit `GitHub Issues`
GitHub Issues bieten eine einfache Möglichkeit, Aufgaben zu organisieren und zu verfolgen. Sie können Issues für Fehler, neue Features oder allgemeine Aufgaben erstellen. Später können Sie Ihre Aufgaben übersichtlich visualisieren, zum Beispiel mit einem Kanban-Board oder einem GANTT-Chart.

Erstellen Sie ein neues Issue in Ihrem Repository und fügen Sie eine Task-Liste hinzu:

```
- [ ] Aufgabe 1: ... 
- [ ] Aufgabe 2: ... 
- [ ] Aufgabe 3: ... 
```

## Visualisierung mit GitHub Projects
GitHub Projects ermöglicht es Ihnen, Issues und Pull Requests in einem Kanban-Board oder GANTT-Chart zu organisieren. Sie können Spalten für verschiedene Phasen Ihres Projekts erstellen (z.B. To Do, In Progress, Done) und Issues per Drag-and-Drop verschieben. 

Ein Projekt kann folgendermassen erstellt werden:
![GitHub Project erstellen](assets/images/git/create-project.png)

Ein Kanban-Board könnte zum Beispiel so aussehen:
![GitHub Projects Kanban-Board](assets/images/git/kanban.png)