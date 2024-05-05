
| Projektbezeichnung | Eventmanagement |
| ------------------ | --------------- |
| Projektleitung     |                 |
| Erstellt am        | 15.04.2024      |
| Letzte Änderung am |                 |
| Status             | In Bearbeitung  |
| Aktuelle Version   | 1.0             |

## Änderungsverlauf

| Datum      | Änderung         | Autor             |
| ---------- | ---------------- | ----------------- |
| 17.04.2024 | Einleitung       | Richard Repenning |
| 17.04.2024 | Auftrag          | Richard Repenning |
| 19.04.2024 | Auftrag - Profil | Richard Repenning |
| 05.05.2024 | Anpassungen      | Richard Repenning |


## 1. Einleitung

Dieses Software-Pflichtenheft dient als Leitfaden für die Entwicklung einer Eventmanagement-Plattform. Die Plattform zielt darauf ab, Besuchern die Möglichkeit zu bieten, Tickets für verschiedene Veranstaltungen zu erwerben. Tickets können bis zum Veranstaltungstag storniert werden. Administratoren können neue Veranstaltungen anlegen und verwalten.

Das Pflichtenheft skizziert die grundlegenden Anforderungen und Funktionen, die in die Entwicklung der Plattform einfließen sollen.

## 2. Auftrag

Die Eventmanagement-Plattform soll eine Reihe von Funktionen umfassen, darunter:

#### Event
Ein Event kann von einem Administrator angelegt werden. Ein Event wird einer Location zugewiesen. Die maximale Teilnehmeranzahl des Events darf nicht die maximale Personenzahl der Location übersteigen.

- ID: Eine automatisch vergebene UID, die das Event eindeutig identifiziert.
- title: Der Titel eines Events
- location: An welchem Ort die Veranstaltung stattfindet.
- date_from: Zeitpunkt des Starts der Veranstaltung.
- date_to: Zeitpunkt des Endes der Veranstaltung.
- description: Eine Textbeschreibung für das Event
- max_participants: Maximale Teilnehmerzahl.
- tickets_sold: Verkaufte Tickets, die nicht storniert wurden.
- event_status: Der Status des Events z.B. "aktiv", "inaktiv", "abgesagt", "ausverkauft" und weitere.
- base_price: Der zu bezahlende Preis für das Event
- slug: Eine eindeutige URL für das Event.

Events werden auf der Seite in einer Eventübersicht angezeigt. Die Eventübersicht ist aufsteigend nach Datum sortiert, d.h. das am nächsten gelegene Event wird als erstes angezeigt. Events, die bereits abgelaufen sind oder "inaktiv" Status haben, werden nicht mehr angezeigt und automatisch archiviert. Ein Event besitzt einen Status ("abgesagt", "ausverkauft"). Der Status kann im Adminbereich verändert werden. Ein neues Event hat standardmäßig den status "inaktiv". Ist die maximale Anzahl an Tickets verkauft, wird der Status des Events automatisch auf "ausverkauft" gesetzt. Ein Event mit diesem Status, das noch nicht stattgefunden hat wird in der Übersicht noch angezeigt, der Ticketkauf ist nicht mehr möglich.

#### Ticket

Ein Ticket wird bei erfolgreichem Kauf einem Event zugeordnet und belegt einen Platz bei den verkauften Tickets.
Für den Kauf eines Tickets benötigt der Käufer einen Account. Das gekaufte Ticket wird dem Account zugeordnet und ist personalisiert.
Hat das Event noch nicht stattgefunden kann das Ticket bis 24 Stunden vor Beginn des Events storniert werden. Wurde ein Ticket storniert ist das Ticket zum Kauf wieder verfügbar.

Ein Ticket hat die folgenden Daten:
- ID: Eindeutige Ticket-ID
- event_id: Die ID des Events.
- user_id: Die ID des Käufers.
- status: Ein Ticketstatus wie z.B. ("bezahlt", "storniert")

#### Location
Eine Location ist der Ort der Veranstaltung. Eine Location wird von einem Admin der Eventmanagement App angelegt. Eine Location wird einem Event zugeordnet. Ein Event kann nur eine Location haben. Eine Location hat eine maximale Personenanzahl. Die maximale Personenanzahl darf nicht kleiner als die maximale Teilnehmeranzahl eines Events sein.
Eine Location wird mit den folgenden Daten angelegt:

- name: Name der Location
- street: In welcher Straße sich die Location befindet.
- zip_code: Postleitzahl der Location.
- city: Stadt der Location.
- max_capacity: Die maximale Personenzahl für die Location.

#### Benutzer
Um ein Ticket für ein Event zu kaufen, muss vor dem Kauf ein Benutzer Account erstellt werden oder der Besucher muss sich in seinen bestehenden Account einloggen. Dies kann er entweder direkt auf der Seite machen oder im Checkout-Prozess des Ticketkaufs. Hat der Benutzer noch keinen Account, kann er sich einen erstellen.
Ein Benutzeraccount hat die folgenden Informationen:

- username: Der Benutzername zum anmelden.
- password: Das Passwort des Benutzers.
- email: Die E-Mail Adresse des Benutzers.
- first_name: Der Vorname des Benutzers.
- last_name: Der Nachname des Benutzers.

#### Profil
Das Profil eines Nutzers ist direkt mit dem Benutzer verbunden. Sobald ein Besucher einen Benutzer-Account erstellt wird auch ein Profil erstellt. Das Profil enthält die persönlichen Informationen des Benutzers. Wird ein Benutzer gelöscht so wird auch das zugehörige Profil gelöscht. Die Profilinformationen können vom Benutzer bearbeitet werden.
Ein Profil hat die folgenden Informationen:

- user: Der verknüpfte Benutzer-Account
- street: Straße der Wohnadresse
- zip_code: Postleitzahl der Wohnadresse
- city: Stadt der Wohnadresse
- birth_date: Geburtsdatum des Benutzers