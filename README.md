![image](https://github.com/user-attachments/assets/93928d9d-4dd7-4156-83df-67d6b758dbc0)

In dieser Bilbiothek ist sind alle Dateien rund um meine Maturarbeit. In der Maturarbeit steht eine Anleitung zum Nachbau der Wortuhr. 

Um den Code auszuführen Müssen die LEDs gemäss Schaltplan mit dem MOSI Pin19 des Raspberry Pis verbunden sein. Wenn man keinen Knopf anschliessen will kann dieser weggelassen werden und der entsprechende Code entfernt werden. Weiter braucht der Code die Pi5Neo Bibliothek (https://pypi.org/project/Pi5Neo/) die man im Terminal mit diesem Befehl installieren kann:

pip install pi5neo --break-system-packages

Um das Programm beim Boot auszuführen muss die .bashrc Datei bearbeitet werden:

sudo nano /home/pi/.bashrc

Am Ende der Datei diesen Code mit dem korrekten Dateipfad einfügen:

echo Running at boot 
sudo python /home/pi/wordclock.py

Die Uhr sollte leuchten sobald der Knopf gedrückt wird.

![Aufbau Schema](https://github.com/user-attachments/assets/068d869a-4121-4520-8055-b86aa158f5be)
