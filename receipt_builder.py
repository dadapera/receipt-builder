from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta


# Funzione per calcolare la settimana precedente
def calcola_settimana(data_ricevuta):
    """
    Calcola la data di inizio e fine della settimana precedente alla data della ricevuta.
    :param data_ricevuta: Data della ricevuta come stringa (es. '16/10/24')
    :return: (data_inizio, data_fine) in formato stringa 'gg/mm/aaaa'
    """
    data_ricevuta_dt = datetime.strptime(data_ricevuta, "%d/%m/%y")
    data_fine_dt = data_ricevuta_dt - timedelta(days=1)  # Giorno prima della data della ricevuta
    data_inizio_dt = data_fine_dt - timedelta(days=7)  # 6 giorni prima per coprire 7 giorni totali
    return data_inizio_dt.strftime("%d/%m/%Y"), data_fine_dt.strftime("%d/%m/%Y")


# Funzione per creare il PDF
def crea_pdf_dinamico(output_file, data):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Titolo e intestazioni (sinistra)
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 50, data['nome'])
    c.drawString(50, height - 65, data['indirizzo'])
    c.drawString(50, height - 80, data['cap_citta'])
    c.drawString(50, height - 95, data['codice_fiscale'])
    c.drawString(50, height - 110, data['data_nascita'])

    # Intestazione azienda (destra)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(width - 200, height - 50, "Spett.le")
    c.setFont("Helvetica", 10)
    c.drawString(width - 200, height - 65, data['azienda'])
    c.drawString(width - 200, height - 80, data['azienda_indirizzo'])
    c.drawString(width - 200, height - 95, f"TAX Number: {data['tax_number']}")

    # Ricevuta
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 180, "RICEVUTA DEL {}".format(data['data_ricevuta']))

    c.drawString(50, height - 220, f"Il sottoscritto {data['nome']}")

    # Somma dichiarata
    c.drawString(50, height - 240, f"dichiara di ricevere la somma lorda di euro {data['importo_lordo']}")
    c.drawString(50, height - 260, f"in data {data['data_pagamento']} per l’attività {data['descrizione_attivita']}")
    c.drawString(50, height - 280, f"svolta nel periodo {data['data_inizio']} - {data['data_fine']}.")

    # Dichiarazione responsabilità
    c.drawString(50, height - 320,
                 "Il sottoscritto dichiara inoltre sotto la propria responsabilità che la prestazione è stata resa")
    c.drawString(50, height - 340, f"alla {data['azienda']} in completa autonomia con carattere occasionale.")

    # Firma e data
    c.drawString(50, height - 400, f"{data['data_ricevuta']}")
    c.drawString(50, height - 420, "In fede")
    c.drawString(50, height - 440, data['nome'])

    # Salva il PDF
    c.save()


# Dati principali
dati_base = {
    "nome": "Nome Cognome",
    "indirizzo": "Via Roma, n. 69",
    "cap_citta": "40141 Bulagna",
    "codice_fiscale": "ABCDEF12G34H567I",
    "data_nascita": "12/31/1970",
    "descrizione_attivita": "Mansione",
    "azienda": "Company, Inc.",
    "azienda_indirizzo": "Str. Larg",
    "tax_number": "12-3456789"
}

# Lista dei pagamenti (importo lordo e data fattura/pagamento)
pagamenti = [
    ("xxxx,xx", "8/10/24"),
]

# Generazione dei PDF
for idx, (importo, data_pagamento) in enumerate(pagamenti, start=1):
    data_inizio, data_fine = calcola_settimana(data_pagamento)
    dati_fattura = dati_base.copy()
    dati_fattura.update({
        "data_ricevuta": data_pagamento,
        "importo_lordo": importo,
        "data_pagamento": data_pagamento,
        "data_inizio": data_inizio,
        "data_fine": data_fine
    })
    output_filename = f"output_files/ricevuta_scaleai_{data_pagamento.replace('/', '-')}.pdf"
    crea_pdf_dinamico(output_filename, dati_fattura)
    print(f"PDF generato: {output_filename}")