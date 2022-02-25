# Verkefna skýrsla

### Tækniskólinn, Tölvubraut, VEFÞ2VÞ05DU Vefforritun II
#### Höfundar:
* Hákon Garðarsson
* Þórður Ingi Sigurjónsson
* Máni Sverrisson

### Verkefnalýsing

### Lýsing Vefkerfis

Við notuðum Flask framworkið í python sem við notuðum fyrir alla backenda vinnu. Einnig var notað Semantic Ui css library fyrir lookið. MySql var notaður til að hýsa lang flest gögn, við notuðum SqlAlchemy library til þess að tala við MySql. Við notuðum json fyrir outfit_styles sem eru bara static gögn. við notuðum flask wtforms til þess að búa til öll html formin. 

#### Gagnagrunns hönnun 
við notuðum Mysql sem gagnagrunn okkar með þrem models fyrir userinn
#### Listi yfir python librarys sem við notuðum:
* flask
* flask_wtf(wtforms) + email_validator
* flask_sqlalchemy
* flask_login
* werkzeug.security 
* Json
* os
* uuid 
* shutil
