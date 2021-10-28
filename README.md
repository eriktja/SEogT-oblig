# SEogT-oblig
Repository for obligatoriske innleveringer i emnet Software Engineering &amp; Testing - høst 2021

Forklaring til innlevering:
Laget et github repository og la til koden fra oblig2.

Valgte "Actions" på github.com og la til en python workflow template som lå der. 
Den jeg valgte ligger under "Continuous integration workflows" og heter "Python Package".

Etter å ha commitet workflow fikk jeg en feilmelding om at syntax i koden ikke var god nok.
Jeg var nødt til å bytte "is" i testene til "=="
eks:  "assert is_four_hundred(400) is 0" måtte byttes til "assert is_four_hundred(400) == 0" 

Etter å ha gjort de nødvendige endringene i test_is_leap_year.py fungerte workflowen fint. 
Alle tester blir kjørt ved hver push. 
