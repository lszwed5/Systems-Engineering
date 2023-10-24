p³eæ(dominika,k).
p³eæ(jakub,m).
p³eæ(³ukasz,m).
p³eæ(milena,k).
p³eæ(iwona,k).
p³eæ(justyna,k).
p³eæ(jerzy,m).
p³eæ(kamil,m).
p³eæ(danuta,k).
p³eæ(jacek,m).
p³eæ(józef,m).
p³eæ(natalia,k).
p³eæ(henryk,m).
p³eæ(halina,k).
p³eæ(wac³aw,m).
p³eæ(katarzyna,k).
p³eæ(franciszek,m).
p³eæ(el¿bieta,k).
p³eæ(zbigniew,m).
p³eæ(karolina,k).

matka(iwona,³ukasz).
matka(iwona,dominika).
matka(justyna,milena).
matka(natalia,jerzy).
matka(danuta,iwona).
matka(danuta,justyna).
matka(halina,józef).
matka(katarzyna,natalia).
matka(el¿bieta,danuta).
matka(karolina,jacek).

ojciec(jerzy,³ukasz).
ojciec(jerzy,dominika).
ojciec(kamil,milena).
ojciec(józef,jerzy).
ojciec(jacek,iwona).
ojciec(jacek,justyna).
ojciec(henryk,józef).
ojciec(wac³aw,natalia).
ojciec(franciszek,danuta).
ojciec(zbigniew,jacek).

rodzic(X,Y):-matka(X,Y);ojciec(X,Y).

dziecko(X,Y):-rodzic(Y,X).
syn(X,Y):-dziecko(X,Y),p³eæ(X,m).
córka(X,Y):-dziecko(X,Y),p³eæ(X,k).

m¹¿(jakub,dominika).
m¹¿(jerzy,iwona).
m¹¿(kamil,justyna).
m¹¿(jacek,danuta).
m¹¿(józef,natalia).
m¹¿(henryk,halina).
m¹¿(wac³aw,katarzyna).
m¹¿(franciszek,el¿bieta).
m¹¿(zbigniew,karolina).

¿ona(X,Y):-m¹¿(Y,X).

babcia(X,Y):-matka(X,Z),matka(Z,Y).
dziadek(X,Y):-ojciec(X,Z),ojciec(Z,Y).
wnuk(X,Y):-babcia(Y,X);dziadek(Y,X).
brat(X,Y):-matka(Z,X),matka(Z,Y),ojciec(W,X),ojciec(W,Y),p³eæ(X,m),X\=Y.
siostra(X,Y):-matka(Z,X),matka(Z,Y),ojciec(W,X),ojciec(W,Y),p³eæ(X,k),X\=Y.
stryj(X,Y):-brat(X,Z),ojciec(Z,Y).
wuj(X,Y):-brat(X,Z),matka(Z,Y).
ciotka(X,Y):-siostra(X,Z),rodzic(Z,Y).
kuzyn(X,Y):-dziecko(X,Z),dziecko(Y,W),(siostra(Z,W);brat(Z,W)).

przodek(X,Y):-rodzic(X,Y).
przodek(X,Y):-rodzic(X,Z), przodek(Z,Y).

potomek(X,Y):-dziecko(X,Y).
potomek(X,Y):-dziecko(X,Z), potomek(Z,Y).

liczba_dzieci(X,Y):-aggregate_all(count,dziecko(Z,Y), X).
