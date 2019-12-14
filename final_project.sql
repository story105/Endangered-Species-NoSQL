-- 5 tables, one main with FOREIGN keys pointing to strin representations
CREATE TABLE Temp(
  Torganism varchar(50),
  Tspecies varchar(50),
  Tfederal_status varchar(50),
  Tunit varchar(50),
  TUSstate varchar(50)
);

CREATE TABLE Main(
  PK INTEGER PRIMARY KEY,
  organism_id int,
  species_id int,
  federal_status_id int,
  unit_id int,
  state_id int,
  FOREIGN KEY (organism_id) REFERENCES Organism(organism_id)
  FOREIGN KEY (species_id) REFERENCES Species(species_id)
  FOREIGN KEY (federal_status_id) REFERENCES Federal_Status(federal_status_id)
  FOREIGN KEY (unit_id) REFERENCES Region(unit_id)
  FOREIGN KEY (state_id) REFERENCES USstate(USstate_id)
  ON UPDATE CASCADE
  ON DELETE SET NULL
);

CREATE TABLE Organism(
  organism_id INTEGER PRIMARY KEY,
  organism varchar(50)
);

CREATE TABLE Species(
  species_id INTEGER PRIMARY KEY,
  species varchar(50)
);

-- 1 or 2 = Threatened or Endangered
CREATE TABLE Federal_Status(
  federal_status_id INTEGER PRIMARY KEY,
  federal_status varchar(50)
);

CREATE TABLE Region(
  unit_id INTEGER PRIMARY KEY,
  unit varchar(50)
);

CREATE TABLE USstate(
  USstate_id INTEGER PRIMARY KEY,
  USstate varchar(50)
);

CREATE TABLE Extinct (
  extinct_id INTEGER PRIMARY KEY,
  extinct VARCHAR(50)
);
