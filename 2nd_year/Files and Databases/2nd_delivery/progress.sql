select extract(year from concerts.when) year_, extract(month from concerts.when) month_,
	count(performances.when) from concerts join performances on
	concerts.when = performances.when
	and concerts.performer = performances.performer
	group by extract(year from concerts.when), extract(month from concerts.when)
	order by extract(year from concerts.when), extract(month from concerts.when);
	
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
