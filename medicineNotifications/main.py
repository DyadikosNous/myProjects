from win10toast import ToastNotifier
import datetime
import time

# Φτιάχνουμε ενα λεξικό με το όνομα του φαρμάκου που θέλουμε
# και τις ώρες που πρέπει να το πάρουμε.
medicines = {
    "Αντιβίωση": ["09:00", "12:00", "15:00", "18:00"],
    "Χάπι της πίεσης": ["10:00", "13:00", "16:00", "19:00"],
    "Ινσουλίνη": ["11:00", "14:40", "14:41", "15:01"]
}

# Καλούμε το ToastNotifier που διαχειρίζεται τις ειδοποιήσεις των Windows.
toaster = ToastNotifier()

# Δημιουργούμε ενα infinite loop, έτσι ώστε να ελέγχει πάντα την ώρα
# και να τη συγκρίνει με τις ώρες στο dictionary.
while True:
    # Παίρνουμε την τωρινή ώρα σε μορφή ωρών και λεπτών.
    now = datetime.datetime.now().strftime("%H:%M")

    # Δημιουργούμε ενα For Loop για να περνάμε θέση-θέση το dictionary
    # και να ελέγχουμε αν το "τώρα" είναι μέσα στις τιμές.
    for medicine, times in medicines.items():
        if now in times:
            # Δημιουργία μηνύματος
            title = "Ειδοποίηση Φαρμάκου!"
            message = f"Είναι ώρα για {medicine}!"

            # Αποστολή ειδοποίησης
            toaster.show_toast(title, message, duration=10)

    # Το πρόγραμμα μας κάνει ενός λεπτού παύση.
    time.sleep(60)
