import sqlite3
db=sqlite3.connect("BDSAHD.db")

c=db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS cargo (ID_CARGO INTEGER(5) PRIMARY KEY,DES_CARGO VARCHAR(100) UNIQUE NOT NULL)")
c.execute("CREATE TABLE IF NOT EXISTS area (ID_AREA INTEGER(5) PRIMARY KEY, DESC_AREA VARCHAR(100) NOT NULL)")
c.execute("CREATE TABLE IF NOT EXISTS usuarios (ID_USU INTEGER(5) PRIMARY KEY NOT NULL,NOMBRE VARCHAR(50),AP_P VARCHAR(50), AP_M VARCHAR(50),PASS VARCHAR(50) NOT NULL,HUELLA VARCHAR(15), ID_AREA INT(5), ID_CARGO INT(5))")
c.execute("CREATE TABLE IF NOT EXISTS checar (ID_CHECAR INTEGER(5)PRIMARY KEY, HR_ENTRADA TIME, HR_SALIDA TIME, REGISTRO DATE,ID_AREA INTEGER(5), ID_USUARIO INTEGER(5))")
'''
#c.execute("INSERT INTO cargo VALUES (1, 'Root')")
#c.execute("INSERT INTO cargo VALUES (2, 'Admon')")

areas=[(10000,'Geología'),
(10001,'Minas'),
(10002,'Concentradora'),
(10003, 'Mantenimiento'),
(10004,'Mantenimiento'),
(10005,'Seguridad'),
(10006, 'Logística'),
(10007,'Médico'),
(10008,'Relaciones industriales'),
(10009,'Contabilidad'),
(10010, 'Ingeniería'),
(10011,'Entrenamiento')]
c.executemany("INSERT INTO area VALUES (?,?) ",areas)

c.execute("CREATE TABLE IF NOT EXISTS general (ID_USU INTEGER(5) PRIMARY KEY NOT NULL,NOMBRE VARCHAR(50),AP_P VARCHAR(50), AP_M VARCHAR(50),PASS VARCHAR(50) NOT NULL,HUELLA VARCHAR(15), ID_AREA VARCHAR(100),ID_CARGO VARCHAR(100))")
c.execute("INSERT INTO usuarios VALUES(00001,'Francisco','Hernandez','Rocha','123456',00001,1)")
'''
c.execute("INSERT INTO general VALUES(00001,'Francisco','Hernandez','Rocha','123456','10','Relaciones industriales','Root')")

db.commit()
