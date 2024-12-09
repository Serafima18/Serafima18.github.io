CREATE TABLE USERS (
    user_id TEXT PRIMARY KEY,
    email TEXT,
    geo TEXT
);

CREATE TABLE LOG (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    time DATETIME,
    bet REAL,
    win REAL,
    FOREIGN KEY (user_id) REFERENCES USERS (user_id)
);