# Quick testing ai chatbot capabilities (for flowers)

Personal project needs to be integrated with simple chatbot, that is capable of recognizing which plant speaker has in mind. 

With that simple (less than 100 lines) implementation, I can use that inside small ESP32 module. Within hosted simple application which will receive data (still didn't choose if we should use framework (django/fastapi/flask) or just work with simple raw TCP).

After receiving data, the chatbot will "guess" user's intent and send correct signal to the pump driver (which is basically just the distributor between correct places - where the plants are growing).

# Example interaction (without voice, just terminal)

```bash
Ty: podlewamy fikusa
Bot (rozpoznana intencja): water_1
Bot: Podlewam water_1!
Ty: fikus
Bot (rozpoznana intencja): water_1
Bot: Podlewam water_1!
Ty: podlej fikusa
Bot (rozpoznana intencja): water_1
Bot: Podlewam water_1!
Ty: proszę, podlej fikusa
Bot (rozpoznana intencja): water_1
Bot: Podlewam water_1!
Ty: podlewamy, czas na fikusa
Bot (rozpoznana intencja): water_1
Bot: Podlewam water_1!
Ty: podlej wszyskto
Bot (rozpoznana intencja): water_2
Bot: Podlewam water_2!
Ty: podlej piwonię
Bot (rozpoznana intencja): water_3
Bot: Podlewam water_3!
Ty: podlewamy piwonię, dawaj piwonię
Bot (rozpoznana intencja): water_3
Bot: Podlewam water_3!
Ty:
```

# How to run

1. Create venv
2. Activate it (`source vevn/bin/activate`)
3. Install dependencies (`pip install -r requirements.txt`)
4. Run the script (the script with chatbot is under file `script2.py`) so just run `python script2.py`
