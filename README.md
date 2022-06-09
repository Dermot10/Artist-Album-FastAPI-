# Artist-Album-FastAPI-
API with endpoints adhering to conventional  HTTP protocol. 
Program allows for albums to be created and linked to associated artist, creating a catalogue.

Utilising fastAPI's automatic model documentation endpoints can easily be instantiated and then tested. 
Additional API testing software like Postman can be utilised to more strignently construct and analyse
the aforementioned endpoints. 

Type hints in addition to the pydantic library were utilised for better data validation. 

PostgresSQL is the integrated database holding the associated information. Adhering to standard CRUD
functionality, the endpoints follow this criteria. 
The models for the database were created in python (classes) and were handled with the ORM SQL-alchemy for beter
database program-database communication. 
