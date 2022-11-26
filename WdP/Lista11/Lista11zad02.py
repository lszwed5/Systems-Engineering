import sqlite3


db = sqlite3.connect("base.db")
cursor = db.cursor()

cursor.execute("""DROP TABLE IF EXISTS instrumenty""")
cursor.execute("""DROP TABLE IF EXISTS magazyn""")

cursor.execute("CREATE TABLE IF NOT EXISTS instrumenty ("
               "id INTEGER PRIMARY KEY ASC,"
               "nazwa varchar NOT NULL,"
               "rodzaj varchar NOT NULL,"
               "typ char NOT NULL)")

cursor.execute("CREATE TABLE IF NOT EXISTS magazyn ("
               "id INTEGER PRIMARY KEY ASC,"
               "sektor varchar NOT NULL,"
               "instrumenty_id INTEGER NOT NULL,"
               "FOREIGN KEY(instrumenty_id) REFERENCES instrumenty(id))")

cursor.execute("""INSERT INTO instrumenty (nazwa, rodzaj, typ) VALUES("Epiphone", "gitara", "strunowe")""")
cursor.execute("""INSERT INTO instrumenty (nazwa, rodzaj, typ) VALUES("Gibson", "gitara", "strunowe")""")
cursor.execute("""INSERT INTO instrumenty (nazwa, rodzaj, typ) VALUES("Yamaha", "pianino", "klawiszowe")""")
cursor.execute("""INSERT INTO instrumenty (nazwa, rodzaj, typ) VALUES("Stradivarius", "skrzypce", "smyczkowe")""")

cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("A", "1")""")
cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("A", "1")""")
cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("A", "1")""")
cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("A", "2")""")
cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("A", "2")""")
cursor.execute("""INSERT INTO magazyn (sektor, instrumenty_id) VALUES("B", "3")""")


def showall():
    result = cursor.execute("SELECT * FROM instrumenty")
    db.commit()
    for i in result:
        print(i)

    print()

    result = cursor.execute("SELECT * FROM magazyn")
    db.commit()
    for i in result:
        print(i)

    print()


def stan_magazynu():
    result = cursor.execute("""SELECT instrumenty.id, nazwa, rodzaj, sektor FROM instrumenty, magazyn
                                WHERE instrumenty.id=magazyn.instrumenty_id""")
    db.commit()
    for i in result:
        print(i)
    print()


def ilosc_na_magazynie():
    result = cursor.execute("""SELECT COUNT(*) FROM instrumenty, magazyn 
                WHERE instrumenty.id=magazyn.instrumenty_id""")
    db.commit()
    for i in result:
        print(f"Ilość instrumentów na magazynie: {i[0]}")
    print()


def ilosc_poszczegolnych_instrumentow():
    cursor.execute("""SELECT COUNT(magazyn.id), instrumenty.rodzaj FROM instrumenty, magazyn
                        WHERE instrumenty.id=magazyn.instrumenty_id
                        GROUP BY rodzaj""")
    ilosc = cursor.fetchall()
    for rodzaj in ilosc:
        print(f"""Na magazynie jest {rodzaj[0]} instrumentów rodzaju {rodzaj[1]}""")
    print()


def delete_id():
    table = input("Z której tabeli chcesz coś usunąć?\n")
    if table == "instrumenty":
        to_be_deleted = input("Podaj id do usunięcia: ")
        ids_table = cursor.execute("SELECT id FROM instrumenty")
        ids = []
        for id in ids_table:
            ids.append(id[0])
        if int(to_be_deleted) in ids:
            cursor.execute(f"""DELETE FROM instrumenty WHERE id={to_be_deleted}""")
            print("Usunięto pomyślnie!")
            print()
        else:
            print("Nie ma takiego id!")
            print()
    elif table == "magazyn":
        to_be_deleted = input("Podaj id do usunięcia: ")
        ids_table = cursor.execute("SELECT id FROM magazyn")
        ids = []
        for id in ids_table:
            ids.append(id[0])
        if int(to_be_deleted) in ids:
            cursor.execute(f"""DELETE FROM magazyn WHERE id={to_be_deleted}""")
            print("Usunięto pomyślnie!")
            print()
        else:
            print("Nie ma takiego id!")
            print()
    else:
        print("Nie ma takiej tabeli")


showall()
stan_magazynu()
ilosc_na_magazynie()
ilosc_poszczegolnych_instrumentow()
delete_id()
showall()
