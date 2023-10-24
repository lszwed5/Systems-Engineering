p�e�(dominika,k).
p�e�(jakub,m).
p�e�(�ukasz,m).
p�e�(milena,k).
p�e�(iwona,k).
p�e�(justyna,k).
p�e�(jerzy,m).
p�e�(kamil,m).
p�e�(danuta,k).
p�e�(jacek,m).
p�e�(j�zef,m).
p�e�(natalia,k).
p�e�(henryk,m).
p�e�(halina,k).
p�e�(wac�aw,m).
p�e�(katarzyna,k).
p�e�(franciszek,m).
p�e�(el�bieta,k).
p�e�(zbigniew,m).
p�e�(karolina,k).

matka(iwona,�ukasz).
matka(iwona,dominika).
matka(justyna,milena).
matka(natalia,jerzy).
matka(danuta,iwona).
matka(danuta,justyna).
matka(halina,j�zef).
matka(katarzyna,natalia).
matka(el�bieta,danuta).
matka(karolina,jacek).

ojciec(jerzy,�ukasz).
ojciec(jerzy,dominika).
ojciec(kamil,milena).
ojciec(j�zef,jerzy).
ojciec(jacek,iwona).
ojciec(jacek,justyna).
ojciec(henryk,j�zef).
ojciec(wac�aw,natalia).
ojciec(franciszek,danuta).
ojciec(zbigniew,jacek).

rodzic(X,Y):-matka(X,Y);ojciec(X,Y).

dziecko(X,Y):-rodzic(Y,X).
syn(X,Y):-dziecko(X,Y),p�e�(X,m).
c�rka(X,Y):-dziecko(X,Y),p�e�(X,k).

m��(jakub,dominika).
m��(jerzy,iwona).
m��(kamil,justyna).
m��(jacek,danuta).
m��(j�zef,natalia).
m��(henryk,halina).
m��(wac�aw,katarzyna).
m��(franciszek,el�bieta).
m��(zbigniew,karolina).

�ona(X,Y):-m��(Y,X).

babcia(X,Y):-matka(X,Z),matka(Z,Y).
dziadek(X,Y):-ojciec(X,Z),ojciec(Z,Y).
wnuk(X,Y):-babcia(Y,X);dziadek(Y,X).
brat(X,Y):-matka(Z,X),matka(Z,Y),ojciec(W,X),ojciec(W,Y),p�e�(X,m),X\=Y.
siostra(X,Y):-matka(Z,X),matka(Z,Y),ojciec(W,X),ojciec(W,Y),p�e�(X,k),X\=Y.
stryj(X,Y):-brat(X,Z),ojciec(Z,Y).
wuj(X,Y):-brat(X,Z),matka(Z,Y).
ciotka(X,Y):-siostra(X,Z),rodzic(Z,Y).
kuzyn(X,Y):-dziecko(X,Z),dziecko(Y,W),(siostra(Z,W);brat(Z,W)).

przodek(X,Y):-rodzic(X,Y).
przodek(X,Y):-rodzic(X,Z), przodek(Z,Y).

potomek(X,Y):-dziecko(X,Y).
potomek(X,Y):-dziecko(X,Z), potomek(Z,Y).

liczba_dzieci(X,Y):-aggregate_all(count,dziecko(Z,Y), X).
