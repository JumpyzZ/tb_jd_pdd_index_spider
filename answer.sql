select name, id, class, age
from tb_student
where major = "应用统计"
order by age desc
limit 20 offset 0
