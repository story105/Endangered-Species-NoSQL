-- 5 tables, one main with FOREIGN keys pointing to strin representations
CREATE TABLE Main(
  PK int PRIMARY KEY,
  organism_id int,
  species_id int,
  federal_status_id int,
  unit_id int,
  state_id int
);

CREATE TABLE Organism(
  organism_id int PRIMARY KEY,
  organism varchar(50),
  FOREIGN KEY (organism_id) REFERENCES Main(organism_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Species(
  species_id int PRIMARY KEY,
  species varchar(50),
  FOREIGN KEY (species_id) REFERENCES Main(species_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Federal_Status(
  federal_status_id int PRIMARY KEY,
  federal_status varchar(50),
  FOREIGN KEY (federal_status_id) REFERENCES Main(federal_status_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Unit(
  unit_id int PRIMARY KEY,
  unit varchar(50),
  FOREIGN KEY (unit_id) REFERENCES Main(unit_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE USstate(
  USstate_id int PRIMARY KEY,
  USstate varchar(50),
  FOREIGN KEY (USstate_id) REFERENCES Main(state_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);
