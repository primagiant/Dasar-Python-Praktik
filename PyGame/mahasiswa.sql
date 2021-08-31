INSERT INTO dosen
VALUES 
("00001", "Nugraha Adisono", "L", "+6200000000"),
("00002", "Aduinin Din", "P", "+6200000001"),
("00003", "Jaka Tarub", "L", "+6200000002"),
("00004", "Geraldin Etok", "P", "+6200000033"),
("00005", "Govar Bahar", "L", "+6200000023"),
("00006", "Sonya Silimin", "P", "+6200000045"),
("00007", "Jimmy Nutron", "L", "+6200000032"),
("00008", "Toyota X", "L", "+6200000054"),
("00009", "Honda Salim", "L", "+6200000067"),
("00010", "Adi Sena Ayu", "P", "+6200345234");

INSERT INTO matkul
VALUES 
("MK001", "Interaksi Manusia dan Komputer", "3"),
("MK002", "Basis Data", "3"),
("MK003", "Web Programming", "5"),
("MK004", "Struktur Data dan Algoritma", "3"),
("MK005", "Struktur Bangunan", "2"),
("MK006", "Architecture Etnic", "3"),
("MK007", "Studio Perancangan", "4"),
("MK008", "Machine Learning", "3"),
("MK009", "Game Development", "4"),
("MK010", "Argonometri", "2");

INSERT INTO mhs
VALUES 
("2015101001", "Putu Kebog" , "Singaraja", "L", "081334000001", "2020"),
("1915101001", "Kadek Juki" , "Denpasar", "P", "081334000002", "2019"),
("1915101002", "Komang Sirna" , "Jembrana", "L", "081334000003", "2019"),
("1915101003", "Ketut Jali" , "Negara", "L", "081334000004", "2019"),
("1815101001", "Nyoman Sami" , "Tabanan", "P", "081334000005", "2019"),
("1815101002", "Made Pengkol" , "Singaraja", "L", "081334000006", "2018"),
("1815101003", "Ketut Semedi" , "Jembrana", "L", "081334000007", "2018"),
("1815101004", "Luh Dino" , "Denpasar", "P", "081334000008", "2018"),
("2015101002", "Luh De Funny" , "Singaraja", "P", "081334000009", "2020"),
("2015101003", "Alexsander Epoxi" , "Singaraja", "L", "081334000010", "2020");

INSERT INTO mk_mhs
VALUES
("MK001", "2015101001", "00001", "2021", "2"),
("MK002", "1915101001", "00002", "2021", "4"),
("MK003", "1915101002", "00003", "2021", "4"),
("MK004", "1915101003", "00004", "2021", "4"),
("MK005", "1815101001", "00005", "2021", "6"),
("MK006", "1815101002", "00006", "2021", "6"),
("MK007", "2015101002", "00007", "2021", "2"),
("MK008", "2015101003", "00008", "2021", "2"),
("MK009", "1815101001", "00009", "2021", "6"),
("MK010", "2015101003", "00010", "2021", "2");

-- Subquery
SELECT nama FROM mhs 
where nim IN (SELECT kd_mhs FROM mk_mhs);


-- Union
SELECT nama, no_tlp  FROM mhs
UNION SELECT nama, no_hp FROM dosen;

-- Intersect
SELECT kd_mhs FROM mk_mhs
INTERSECT SELECT nim FROM mhs;

-- Except
SELECT nim FROM mhs
SELECT kd_mhs FROM mk_mhs

-- Intersect V2
SELECT DISTINCT kd_mhs FROM mk_mhs  
WHERE kd_mhs IN (SELECT nim FROM mhs);

-- Except V2
SELECT DISTINCT nim FROM mhs  
WHERE nim NOT IN (SELECT kd_mhs FROM mk_mhs)
UNION
SELECT DISTINCT nim FROM mhs  
WHERE nim NOT IN (SELECT kd_mhs FROM mk_mhs); 
