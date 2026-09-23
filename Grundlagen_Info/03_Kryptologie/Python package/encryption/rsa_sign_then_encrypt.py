# ------------------------------------------------------------
# Sign-then-Encrypt (RSA): Signieren und Verschlüsseln
# ------------------------------------------------------------

# Klartext-Nachricht
m = 4

# Schlüssel von Alice
e_A = 3   # Öffentlicher Schlüssel (Exponent)
n_A = 33  # Modul von Alice
d_A = 7   # Privater Schlüssel

# Schlüssel von Bob
e_B = 3   # Öffentlicher Schlüssel (Exponent)
n_B = 55  # Modul von Bob
d_B = 27  # Privater Schlüssel

# 1. Alice signiert die Nachricht mit ihrem privaten Schlüssel
s = m ** d_A % n_A
print("1. Erstellte Signatur s:", s)

# 2. Alice verschlüsselt Nachricht und Signatur mit Bobs öffentlichem Schlüssel
c_m = m ** e_B % n_B
c_s = s ** e_B % n_B
print(f"2. Verschlüsselte Chiffrate: c_m = {c_m}, c_s = {c_s}")

# 3. Bob entschlüsselt Nachricht und Signatur mit seinem privaten Schlüssel
m_ent = c_m ** d_B % n_B
s_ent = c_s ** d_B % n_B
print("3. Entschlüsselte Nachricht m:", m_ent)
print("   Entschlüsselte Signatur s:", s_ent)

# 4. Bob prüft die Signatur mit Alices öffentlichem Schlüssel
m_pruef = s_ent ** e_A % n_A
print("4. Aus Signatur berechneter Wert m':", m_pruef)
print("   Signatur gültig?", m_pruef == m_ent)
