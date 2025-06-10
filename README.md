# Quick testing ai chatbot capabilities (for flowers)

Personal project needs to be integrated with simple chatbot, that is capable of recognizing which plant speaker has in mind. 

With that simple (less than 100 lines) implementation, I can use that inside small ESP32 module. Within hosted simple application which will receive data (still didn't choose if we should use framework (django/fastapi/flask) or just work with simple raw TCP).

After receiving data, the chatbot will "guess" user's intent and send correct signal to the pump driver (which is basically just the distributor between correct places - where the plants are growing).


