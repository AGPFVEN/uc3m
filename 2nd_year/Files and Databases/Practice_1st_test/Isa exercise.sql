-- -----------------------------------------
-- 1st exercise
-- -----------------------------------------
--I took this approach because of the possibility of the future addition of new countries
--But this could be done with a check constraint in the store table
create table country(
    identifier varchar(50)
);

create table store(
    CIF varchar(50),
    store_name varchar(50),
    country varchar(50),
    constraint pk_store primary key (CIF),
    constraint fk_store_country foreign key(country) references country(IDENTIFIER)
);

create table customer(
    nif varchar(50),
    customer_name varchar(50),
    credit_card number(16),
    birth_date date,
    constraint pk_customer primary key(nif),
);

create table purcharse(
    store varchar(50),
    customer varchar(50),
    amount number(2),
    age number(3),
    constraint pk_purchase primary key(store, customer),
    constraint fk_purchase_store foreign key(store) references store(CIF),
    constraint fk_purchase_customer foreign key(customer) references customer(nif)
);

