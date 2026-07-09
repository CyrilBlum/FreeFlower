#!/bin/bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
    echo "Verwendung: $0 ANZAHL_USER"
    echo "Beispiel: $0 24"
    exit 1
fi

COUNT="$1"
WEBROOT="/var/www/webproj.in-form-atik.ch/public_html/2026"
GROUP="webtech2026"
OUTPUT_CSV="zugangsdaten_webtech2026.csv"

if ! [[ "$COUNT" =~ ^[0-9]+$ ]] || [ "$COUNT" -lt 1 ]; then
    echo "Fehler: ANZAHL_USER muss eine positive ganze Zahl sein."
    exit 1
fi

groupadd -f "$GROUP"

echo "username,password,url" > "$OUTPUT_CSV"

for i in $(seq 1 "$COUNT"); do
    USER="user$i"
    PASS="$(openssl rand -base64 18 | tr -d '/+= ' | cut -c1-16)"
    USERDIR="$WEBROOT/$USER"

    echo "Erstelle $USER"

    if ! id "$USER" >/dev/null 2>&1; then
        useradd \
            -g "$GROUP" \
            -d "$USERDIR" \
            -s /usr/sbin/nologin \
            "$USER"
    fi

    echo "$USER:$PASS" | chpasswd

    mkdir -p "$USERDIR"

    chown "$USER:www-data" "$USERDIR"
    chmod 750 "$USERDIR"

    if [ ! -f "$USERDIR/index.html" ]; then
        cat > "$USERDIR/index.html" <<EOF
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>$USER</title>
</head>
<body>
  <h1>Website von $USER</h1>
</body>
</html>
EOF
        chown "$USER:www-data" "$USERDIR/index.html"
        chmod 640 "$USERDIR/index.html"
    fi

    echo "$USER,$PASS,https://webproj.in-form-atik.ch/2026/$USER/" >> "$OUTPUT_CSV"
done

echo
echo "Fertig."
echo "Zugangsdaten gespeichert in: $OUTPUT_CSV"