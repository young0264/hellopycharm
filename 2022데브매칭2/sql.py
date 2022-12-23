-- -- 코드를 입력하세요
SELECT t1.branch_id, t2.name as branch_name, (t3.car_id) as count from employees as t1

join (select id, name from branches ) t2
on t1.branch_id = t2.id

join (select employee_id,car_id, count(car_id=306) from sellings group by car_id  ) t3
on t1.id = t3.employee_id

group by t2.id
order by t1.branch_id

-- select employee_id, count(car_id=306) from sellings group by car_id

-- select * from employees
-- select * from branches
-- select * from sellings