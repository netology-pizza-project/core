CREATE DATABASE pizza;
CREATE TABLE IF NOT EXISTS products (
    product_id uuid PRIMARY KEY default uuid_generate_v4 (),
    product_title varchar(50) not null,
    product_description varchar(350),
    product_image varchar default '/pics/default.png' not null,
    product_is_new bool default false not null,
    product_price float8 not null,
    product_available bool default true not null,
    created_at timestamp not null,
    updated_at timestamp not null,
    constraint product_price_check check(product_price > 10 and product_price < 100000)
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id      uuid PRIMARY KEY,
    customer_pw_hash varchar,
    customer_phone   integer not null,
    created_at       timestamp not null,
    updated_at       timestamp not null
);

CREATE TABLE IF NOT EXISTS orders_listing (
    order_id integer,
    product_id uuid REFERENCES products(product_id),
    product_quantity integer not null,
    constraint product_quantity_check check(product_quantity > 0 AND product_quantity < 100)
);

CREATE TABLE IF NOT EXISTS cart (
    customer_id uuid REFERENCES customers(customer_id),
    cart_b64_hash varchar,
    created_at timestamp not null,
    updated_at timestamp not null
);

CREATE TABLE IF NOT EXISTS orders (
    order_id uuid PRIMARY KEY,
    customer_id uuid REFERENCES customers(customer_id),
    order_address varchar not null,
    order_status varchar not null,
    created_at timestamp not null,
    updated_at timestamp not null
);

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


