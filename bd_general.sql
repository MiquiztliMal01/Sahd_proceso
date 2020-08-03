
create table cargo (id_cargo int (5) primary key , desc_cargo varchar(100) unique not null);
create table area (id_area int(5) primary key, desc_araea varchar(100)unique not null);
create table usuarios (id_usu int(5) primary key, nom varchar(50)not null, ap_p varchar(50) not null, ap_m varchar(50) not null,contra varchar(50) not null, huella int(10),id_cargo int(5), foreign key (id_cargo) references cargo(id_cargo));
create table checar (id_checar int(5)primary key, hr_entrada time, hr_salida time,fecha date not null, id_area int(5), id_usuario int(5),foreign key (id_usuario) references usuarios(id_usu), foreign key (id_area) references area(id_area));

insert into cargo values (50000,'Root');
insert into cargo values (50001,'Admon');
insert into cargo values (50002,'Empleado');

insert into area values (60000,'Geología');
insert into area values (60001,'Minas');
insert into area values (60002,'Concentradora');
insert into area values (60003,'Mantenimiento');
insert into area values (60004,'Seguridad');
insert into area values (60005,'Logística');
insert into area values (60006,'Médico');
insert into area values (60007,'Relaciones Industriales');
insert into area values (60008,'Contabilidad');
insert into area values (60009,'Ingeniería');
insert into area values (60010,'Entrenamiento');

select*from usuarios where id_cargo='50000';

insert into usuarios values (00001,'Francisco','Hernandez','Rocha',123456,10,50000);
insert into usuarios values (00002,'Eder Ulises','Tovar','Beltran',654321,10,50001);