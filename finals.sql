create table users
(
    user_id        serial      not null
        constraint users_pk
            primary key,
    first_name     varchar(50) not null,
    last_name      varchar(50) not null,
    address        varchar(50) not null,
    contact_number integer     not null
);

alter table users
    owner to postgres;

create table packages
(
    package_id serial       not null
        constraint packages_pk
            primary key,
    location   varchar(255) not null,
    duration   integer      not null,
    head_rate  integer      not null,
    inclusion  varchar(255),
    event_name varchar(255) not null
);

alter table packages
    owner to postgres;

create table reservations
(
    booking_id     serial                                          not null
        constraint reservations_pk
            primary key,
    package_id     integer                                         not null
        constraint reservations_packages__fk
            references packages,
    guest_id       integer                                         not null
        constraint reservations_users__fk
            references users,
    head_count     integer                                         not null,
    amount_due     double precision                                not null,
    receipt_number integer,
    payment_status varchar(50) default 'unpaid'::character varying not null
);

alter table reservations
    owner to postgres;

create unique index reservations_packages__fk
    on reservations (package_id, guest_id);

