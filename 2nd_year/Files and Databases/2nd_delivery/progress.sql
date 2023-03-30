---------------------------------------------------3rd exercise draft------------------------------------------------
select attendance.client, attendance.performer, count(attendance.client)
        from attendances
        join client on
                attendance.client = clients.e_mail
        group by attendance.performer, attendance.client
        having count(attendance.client) > 1
        order by attendance.client;
       
create or replace view fans (fan_e_mail, performer, full_name, age) as
select attendances.client, attendances.performer,
		concat(concat(concat(concat(clients.name, ' '), clients.surn1), ' '), clients.surn2) as full_name,
		extract(year from CURRENT_DATE) - extract(year from clients.birthdate) as age
    from attendances
    join clients on
        attendances.client = clients.e_mail
    group by attendances.performer, attendances.client, clients.birthdate, clients.name, clients.surn1, clients.surn2
    having count(attendances.client) > 1
    order by attendances.client;
	
select * from fans where fan_e_mail = 'bernal@clients.vinylinc.com';


select *
        from attendances
        join clients on
                attendances.client = clients.e_mail;
        group by attendances.performer, attendances.client
        having count(attendances.client) > 1
        order by attendances.client;


---------------------------------------------------2nd exercise draft------------------------------------------------
--subquery doesn't work
select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration),
        (select count(performances.when) from performances 
                where concerts.when = performances.when
                group by performances.when)
                as performances_
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);








--This works perfectly
select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration)
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);




perfect query that checks everything is working:
select * from concerts 
        join performances on
        concerts.when = performances.when and
        concerts.performer = performances.performer
        where 
        extract(year from concerts.when) = 2020 and
        extract(month from concerts.when) = 10;




select count(*) from performances 
        where 
        extract(year from performances.when) = 1996 and
        extract(month from performances.when) = 08;
		
select avg(duration) from concerts
  where
  extract(year from concerts.when) = 1996 and
  extract(month from concerts.when) = 08;
		
select * from events 
        where 
        year_ = 1996 and
        month_ = 08;
        
--subquery doesn't work
select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration),
        (select count(performances.when) from performances 
                where concerts.when = performances.when
                group by performances.when)
                as performances_
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);
                
--This works perfectly
select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration)
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);
                
--Frankenstein
select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration),
        (select count(performances.when) from concerts join performances on
        concerts.when = performances.when
        and concerts.performer = performances.performer
        group by extract(year from concerts.when), extract(month from concerts.when))
        as performances_
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);
                
create view events(year_, month_, concerts_num, attendance_total, duration_avg) as
        select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration)
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);












Executed:
create view events(year_, month_, concerts_num, attendance_total, duration_avg) as
        select extract(year from concerts.when) as year_,
        extract(month from concerts.when) as month_,
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration)
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when);
--258 filas




---------------------------------------------------1st exercise draft-------------------------------------------------
select * from albums
join tracks on
albums.pair = tracks.pair
order by albums.pair, albums.performer;




select performer, albums.title album, tracks.title track, tracks.duration duration from albums
join tracks on
albums.pair = tracks.pair
order by albums.pair, albums.performer;




select albums.performer, albums.title album, sum(tracks.duration) from albums
join tracks on
albums.pair = tracks.pair
group by albums.pair, tracks.pair
order by albums.pair, albums.performer;




select * from albums
join tracks on
albums.pair = tracks.pair
order by albums.pair, albums.performer;


select pair, duration from tracks where pair = 'R70587QT947803G';
PAIR              DURATION
--------------- ----------
R70587QT947803G        178
R70587QT947803G        215
R70587QT947803G        216
R70587QT947803G        400
R70587QT947803G        366
R70587QT947803G        204
R70587QT947803G        191
R70587QT947803G        262
R70587QT947803G        374
R70587QT947803G        335
R70587QT947803G        278

PAIR              DURATION
--------------- ----------
R70587QT947803G        249
R70587QT947803G        282
R70587QT947803G        183

select pair, performer from albums where pair = 'R70587QT947803G';

PAIR            PERFORMER
--------------- --------------------------------------------------
R70587QT947803G Rici

select * from my_albums where pair = 'R70587QT947803G';
PERFORMER                                          PAIR              DURATION
-------------------------------------------------- --------------- ----------
Rici                                               R70587QT947803G       3733

---------------------------------------------------FINAL-------------------------------------------------




Final 2nd query:
create or replace view events(year_, month_, concerts_num, attendance_total, concert_duration, performances_avg) as
        select extract(year from concerts.when),
        extract(month from concerts.when),
        count(concerts.when), sum(concerts.attendance), avg(concerts.duration),
        (select count(performances.when) from performances
                where extract(year from performances.when) = extract(year from         concerts.when)
                and extract(month from performances.when) = extract(month from concerts.when)
                group by extract(year from concerts.when), extract(month from concerts.when))
                / count(concerts.when)
        as performances_
        from concerts
        group by extract(year from concerts.when), extract(month from concerts.when)
        order by extract(year from concerts.when), extract(month from concerts.when)
        with read only;




Final 1st view:
create or replace view my_albums(performer, pair, duration) as 
        select albums.performer ,albums.pair, sum(tracks.duration) from albums
        join tracks on
        albums.pair = tracks.pair
        group by albums.pair, albums.performer
        --order by albums.performer, albums.pair
with read only;