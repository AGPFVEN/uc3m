insert into performer(stage_name, nationality) select distinct band, band_nation from fsdb.artists join fsdb.recordings on (bandw = performer);
insert into musician(passport, full_name, birth_date, performer, role_, incorporation_date, withdrawal_date) select distinct passport, musician, birthdate, band, role, start_date, end_date from fsdb.artists join fsdb.recordings on (band = performer) where passport is not null;
--ORA-00001: restriccion unica (FSDB261.PK_PASSPORT) violada
--I know what the error means but I don't have more time to correct it