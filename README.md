## eems
Cистема автоматизации предприятия на Django: система позволяет диспетчерам вести учет заявок в электронном журнале, инженерный персонал может отслеживать историю заявок, контролировать частоту сбоев, делать отчеты по выбранным лифтам, контролировать выполнение плановых работ электромехаников.

### Технологии и таблетки
- django autocomplete light
- django bootstrap3
- django filter
- django tables2

### Сборка docker образа
```sh
docker build -t dzanto/eems:0.0.1 .
docker save -o dzanto.eems.0.0.1.tar dzanto/eems:0.0.1
docker load -i dzanto.eems.0.0.1.tar
```
