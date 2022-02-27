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
við notuðum Mysql sem gagnagrunn okkar með þrem models fyrir userinn, fötin og posta, UserModelið geymir id sem er primary key, nafn, username, email, bio, dagsetning þegar userinn var gerður,link á profile mynd, password, og tengingar á föt og posta. 
Fata modelið geymir id sem er primary key, type, lýsingu, link á mynd af fatnaðnum, dagsetning þegar fatnaðurinn var bættur inn og foreign key á userinn sem bætti því inn.
Post modelið geymir id sem er primary key, foreign key á userinn sem postaði, like sem postinn hefur, dagsetning þegar það var postað, og margir foreign keys á mismunandi týpur af fatnaði.

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


#### Næstu skref
Við myndum bætta við að hægt væri að lika og commenta post, followa aðra Usera og sjá hvaða postar hefðu mestu like. 


#### Virkni
* Linkur á youtube: [Hér](https://youtu.be/BhC7eSogsvs)
* Mynd af [Forsíðu](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(40).png)
* Mynd af [Sidebar](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(41).png)
* Mynd af [What should i wear](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(42).png)
* Mynd af [Sign Up](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(43).png)
* Mynd af [Sidebar](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(44).png)
* Mynd af [User Dashboard](https://github.com/Vefthrounn-Verkefni/verkefna-repo/blob/main/Screenshot%20(45).png)
