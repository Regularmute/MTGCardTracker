CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users,
    guest_id INTEGER REFERENCES users,
    name TEXT
);

CREATE TABLE decks (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections,
    creator_id INTEGER REFERENCES users,
    name TEXT
);

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    collection_id INTEGER REFERENCES collections,
    name TEXT,
    wins INTEGER,
    losses INTEGER,
    colors TEXT
);