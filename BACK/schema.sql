DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS rehabilitation_categories;
DROP TABLE IF EXISTS rehabilitation_knowledge;
DROP TABLE IF EXISTS medicine_feedback;
DROP TABLE IF EXISTS diagnose_feedback;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE rehabilitation_categories (
    categoryId VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE rehabilitation_knowledge (
    knowledgeId VARCHAR(255) PRIMARY KEY,
    categoryId VARCHAR(255),
    title VARCHAR(255),
    content TEXT,
    image VARCHAR(255),
    video VARCHAR(255),
    source VARCHAR(255),
    timestamp TIMESTAMP,
    FOREIGN KEY (categoryId) REFERENCES rehabilitation_categories(categoryId)
);

CREATE TABLE medicine_feedback (
    feecbackId INTEGER PRIMARY KEY AUTOINCREMENT,
    patientId INTEGER,
    medicineID INTEGER,
    feedbackContent TEXT,
    feedbackDate TEXT,
    FOREIGN KEY(patientId) REFERENCES user(id)
);

CREATE TABLE diagnose_feedback (
    feecbackId INTEGER PRIMARY KEY AUTOINCREMENT,
    patientId INTEGER,
    doctor INTEGER,
    feedbackContent TEXT,
    feedbackDate TEXT,
    FOREIGN KEY(patientId) REFERENCES user(id)
);
