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

select * from concerts 
	join performances on
	concerts.when = performances.when and
	concerts.performer = performances.performer
	where 
	extract(year from concerts.when) = 2020 and
	extract(month from concerts.when) = 10;
	
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






Final 2nd query:
create or replace view events(year_, month_, concerts_num, attendance_total, concert_duration, performances_avg) as
	select extract(year from concerts.when),
	extract(month from concerts.when),
	count(concerts.when), sum(concerts.attendance), avg(concerts.duration),
	(select count(performances.when) from performances
		where extract(year from performances.when) = extract(year from 	concerts.when)
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
	order by albums.performer, albums.pair
with read only;






























--Full usable table
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

