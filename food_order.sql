create database mohitha;
use mohitha;
create table user_info(name varchar(50),password varchar(20) unique,phone varchar(10) unique,address varchar(100));
create table cost(f_name varchar(50),cost int not null);
create table order_detail(username varchar(20),food_ordered varchar(40),total_cost int);
insert into cost values ('briyani',210),('noodles',150),('meals',100),('dosa',50);

select * from user_info;
select * from cost_table;
alter table cost rename cost_table;
select * from order_detail;