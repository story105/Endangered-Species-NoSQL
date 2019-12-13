-- 5 tables, one main with FOREIGN keys pointing to strin representations
CREATE TABLE Main(
  PK INTEGER PRIMARY KEY,
  organism_id int,
  species_id int,
  federal_status_id int,
  unit_id int,
  state_id int,
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Organism(
  organism_id INTEGER PRIMARY KEY,
  organism varchar(50),
  FOREIGN KEY (organism_id) REFERENCES Main(organism_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Species(
  species_id INTEGER PRIMARY KEY,
  species varchar(50),
  FOREIGN KEY (species_id) REFERENCES Main(species_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Federal_Status(
  federal_status_id INTEGER PRIMARY KEY,
  federal_status varchar(50),
  FOREIGN KEY (federal_status_id) REFERENCES Main(federal_status_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Region(
  unit_id INTEGER PRIMARY KEY,
  unit varchar(50),
  FOREIGN KEY (unit_id) REFERENCES Main(unit_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE USstate(
  USstate_id INTEGER PRIMARY KEY,
  USstate varchar(50),
  FOREIGN KEY (USstate_id) REFERENCES Main(state_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Extinct (
  extinct_id INTEGER PRIMARY KEY,
  main_id INT,
  FOREIGN KEY (main_id) REFERENCES Main(PK)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);
