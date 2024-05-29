-- -- poste = [ gerant, reciptioniste, techniciten, medecein ]
CREATE TABLE IF NOT EXISTS utilisateur (
  id SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  username VARCHAR NOT NULL UNIQUE,
  password VARCHAR NOT NULL,
  phone VARCHAR NOT NULL,
  date_naissance TIMESTAMP NOT NULL,
  poste VARCHAR NOT NULL
);
CREATE TABLE IF NOT EXISTS employe (
  id SERIAL PRIMARY KEY,
  date_entree TIMESTAMP NOT NULL,
  date_sortie TIMESTAMP,
  salaire REAL NOT NULL,
  utilisateur_id INT NOT NULL,
  CONSTRAINT fk_utilisateur
      FOREIGN KEY(utilisateur_id) 
        REFERENCES utilisateur(id)
);
CREATE TABLE IF NOT EXISTS specialite (
  id SERIAL PRIMARY KEY,
  nom TEXT NOT NULL,
  utilisateur_id INT NOT NULL,
  CONSTRAINT fk_utilisateur
      FOREIGN KEY(utilisateur_id) 
        REFERENCES utilisateur(id)
);

CREATE TABLE IF NOT EXISTS analysis (
  id SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  abreviation VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  prix REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS patient (
  id SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  sexe VARCHAR NOT NULL,
  date_naissance TIMESTAMP NOT NULL,
  phone VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS stock (
  id SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  quantite INT NOT NULL DEFAULT 0,
  prix_unitaire REAL NOT NULL,
  date_peremption TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS bilan (
  id SERIAL PRIMARY KEY,
  payee BOOLEAN NOT NULL DEFAULT FALSE,
  patient_id INT NOT NULL,
  analysis_id INT NOT NULL,
  consultation_id INT,
  date_visite TIMESTAMP NOT NULL,
  CONSTRAINT fk_patient
      FOREIGN KEY(patient_id) 
        REFERENCES patient(id),
  CONSTRAINT fk_analysis
      FOREIGN KEY(analysis_id) 
        REFERENCES analysis(id)
  CONSTRAINT fk_consultation
      FOREIGN KEY(consultation_id) 
        REFERENCES consultation(id)
);
CREATE TABLE IF NOT EXISTS consultation (
  id SERIAL PRIMARY KEY,
  contenu TEXT NOT NULL,
  bilan_id INT NOT NULL,
  CONSTRAINT fk_bilan
      FOREIGN KEY(bilan_id) 
        REFERENCES bilan(id)
);
CREATE TABLE IF NOT EXISTS echantillon (
  id SERIAL PRIMARY KEY,
  code VARCHAR NOT NULL,
  date_prelevement TIMESTAMP NOT NULL DEFAULT now(),
  bilan_id INT NOT NULL,
  CONSTRAINT fk_bilan
      FOREIGN KEY(bilan_id) 
        REFERENCES bilan(id)
);
CREATE TABLE IF NOT EXISTS resultat (
  id SERIAL PRIMARY KEY,
  date TIMESTAMP DEFAULT now(),
  contenu TEXT NOT NULL,
  echantillon_id INT NOT NULL,
  CONSTRAINT fk_echantillon
      FOREIGN KEY(echantillon_id) 
        REFERENCES echantillon(id)
);

