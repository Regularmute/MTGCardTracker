CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT
);

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users ON DELETE CASCADE,
    name TEXT NOT NULL
);

CREATE TABLE collection_invitations (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections,
    guest_id INTEGER REFERENCES users
);

CREATE TABLE decks (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections,
    creator_id INTEGER REFERENCES users,
    name TEXT NOT NULL
);

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections ON DELETE CASCADE,
    name TEXT NOT NULL,
    wins INTEGER,
    losses INTEGER
);
