use emp;
create table employee5 (emp_name char(30), location varchar(30));
desc employee5;
alter table employee5 add add_emp varchar(100);
desc employee5;
alter table employee5 add emp_id int first;
desc employee5;
alter table employee5 add email varchar(25) after location;
desc employee5;
alter table employee5 modify emp_name varchar(30);
desc employee5;
alter table employee5 add sid int, add department varchar(30);
desc employee5;
alter table employee5 change emp_name employeename varchar(30);
desc employee5;
alter table employee5 drop column sid;
desc employee5;

select version();
