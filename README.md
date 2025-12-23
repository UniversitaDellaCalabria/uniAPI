# Guida all'Autenticazione API tramite JWT (JSON Web Token)

Questa guida spiega come autenticare le richieste verso le nostre API utilizzando lo standard **JWT**. Questo metodo garantisce sicurezza e scalabilità, permettendoti di interagire con le risorse protette in modo efficiente.

## 1. Panoramica del Flusso

L'autenticazione si basa su un sistema a due fasi:

1. **Ottenimento del Token**: Invii le tue credenziali e ricevi un *access token* (breve durata) e un *refresh token* (lunga durata).
2. **Utilizzo del Token**: Includi l'access token nell'intestazione (header) di ogni richiesta successiva.

---

## 2. Ottenere i Token

Per iniziare, devi effettuare una richiesta `POST` all'endpoint di login fornendo il tuo username e la tua password.

* **Endpoint:** `/token` (o l'URL comunicato dal tuo amministratore)
* **Metodo:** `POST`
* **Body (JSON):**

```json
{
    "username": "tuo_username",
    "password": "tuo_password"
}

```

**Risposta di successo (200 OK):**

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI..."
}

```

---

## 3. Utilizzo dell'Access Token

Per accedere alle risorse protette, devi inserire l'access token nell'header HTTP delle tue richieste utilizzando il prefisso **Bearer**.

* **Header Key:** `Authorization`
* **Header Value:** `Bearer <tuo_access_token>`

### Esempio con cURL:

```bash
curl -H "Authorization: Bearer <tuo_access_token>" https://api.esempio.it/v1/risorsa-protetta

```

---

## 4. Rinnovo del Token (Refresh)

L'access token ha una durata limitata (es. 60 minuti). Quando scade, riceverai un errore `401 Unauthorized`. Invece di richiedere nuovamente le credenziali all'utente, puoi usare il **refresh token** per ottenere un nuovo access token.

* **Endpoint:** `/token/refresh`
* **Metodo:** `POST`
* **Body (JSON):**

```json
{
    "refresh": "<tuo_refresh_token_precedente>"
}

```

**Risposta:** Riceverai un nuovo access token valido.

---

## 5. Note Importanti sulla Sicurezza

* **Scadenza:** Il refresh token ha una durata maggiore ma scadrà anch'esso dopo un periodo prestabilito. In quel caso, sarà necessario effettuare nuovamente il login.
* **Archiviazione:** Non memorizzare mai i token in file di testo in chiaro o in archivi non protetti.
* **HTTPS:** Tutte le chiamate API devono essere effettuate esclusivamente su protocollo **HTTPS** per evitare l'intercettazione dei token.

---

## Supporto Tecnico

Se riscontri problemi di autenticazione o errori `403 Forbidden` nonostante il token sia corretto, verifica che il tuo account abbia i permessi necessari per la risorsa richiesta o contatta il nostro team di supporto.
