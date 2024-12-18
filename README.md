Here's a short README explaining the provided code for receipt generation:

---

# Receipt Generation Script

This Python script generates a PDF receipt for a given set of payment details using the `reportlab` library. It calculates the start and end date of the previous week based on the provided receipt date and creates a PDF receipt with the payment information.

## Requirements

- Python 3.x
- `reportlab` library

To install the required dependencies, run:
```bash
pip install requirements.txt
```

## Functions

### 1. `calcola_settimana(data_ricevuta)`
Calculates the start and end dates of the previous week based on the provided receipt date.

- **Input**: A string `data_ricevuta` representing the receipt date in `dd/mm/yy` format.
- **Output**: A tuple `(data_inizio, data_fine)` where both dates are formatted as `dd/mm/yyyy`.

### 2. `crea_pdf_dinamico(output_file, data)`
Generates a PDF receipt using the provided `data` dictionary, which contains various details such as the name, address, payment amount, and the company details.

- **Input**: 
  - `output_file`: The output PDF file path.
  - `data`: A dictionary containing the following keys:
    - `nome`, `indirizzo`, `cap_citta`, `codice_fiscale`, `data_nascita` (Personal details)
    - `azienda`, `azienda_indirizzo`, `tax_number` (Company details)
    - `data_ricevuta`, `importo_lordo`, `data_pagamento`, `descrizione_attivita`, `data_inizio`, `data_fine` (Receipt and payment details)
- **Output**: A PDF receipt is saved at the specified path.

## Example Usage

The script uses the following basic data:

```python
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
```

The script calculates the start and end date of the previous week for each payment in the `pagamenti` list, and generates a receipt for each payment:

```python
pagamenti = [
    ("xxxx,xx", "8/10/24"),
]
```

For each payment, it generates a PDF receipt saved in the `output_files/` directory, named as `ricevuta_scaleai_8-10-24.pdf`, and prints a message confirming the PDF generation.

## Output

The generated PDF receipt contains:
- Personal details of the receiver.
- Company details (including tax number).
- Payment amount and details.
- A statement of responsibility.
- Signature and receipt date.

Each receipt is created for the payment period from the previous week, as calculated from the provided `data_ricevuta`.

---

