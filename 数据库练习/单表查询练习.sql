/*company数据库：
	|--dept:部门表
		|--`deptno` 部门编号
		|--`dname`  部门名称
		|--`loc`    部门所在地址
  

	|--employees:员工表
		|--`empno`	员工编号
		|--`ename`	员工姓名
		|--`job`	工作
		|--`MGR`	上级领导
		|--`hiredate`   入职日期
		|--`sal`	薪资
		|--`comm`       将金
		|--`deptno`     部门编号

/*
	1. 查询出部门编号为30的所有员工
	2. 所有经理的姓名、编号和部门编号。
	3. 找出奖金高于工资的员工。
	4. 找出奖金高于工资60%的员工。
	5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
	6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
	7. 无奖金或奖金低于1000的员工。
	8. 查询名字由三个字组成的员工。
	9. 查询2000年以及以后入职的员工。
	10. 查询所有员工详细信息，用编号升序排序
	11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
	12. 查询每个部门的平均工资
	13. 查询每个部门的雇员数量。
	14. 查询每种工作的最高工资、最低工资、人数
*/
-- 1
SELECT *
FROM t_employees
WHERE `deptno` = 30
-- 2
SELECT empno,ename,deptno
FROM t_employees
WHERE `job` = "经理"
-- 3
SELECT *
FROM t_employees
WHERE `comm` > `sal`
-- 4
SELECT *
FROM t_employees
WHERE `comm` > `sal`*0.6
-- 5
SELECT *
FROM t_employees
WHERE (`deptno` = 10 AND `job` = "经理") OR (`deptno` = 20 AND `job` = "分析员")
-- 6
SELECT *
FROM t_employees
WHERE (`deptno` = 10 AND `job` = "经理") OR (`deptno` = 20 AND `job` = "分析员") 
OR (`sal` > 3000 AND (`job` != "经理" AND `job` != "武装上将"))
-- 7
SELECT *
FROM t_employees
WHERE `comm` < 1000 OR `comm` IS NULL
-- 8
SELECT *
FROM t_employees
WHERE `ename` LIKE "___"
-- 9
SELECT *
FROM t_employees
WHERE `hiredate` > "2000-01-01"
-- 10
SELECT *
FROM t_employees
ORDER BY `empno` ASC
-- 11
SELECT *
FROM t_employees
ORDER BY `sal` DESC,`hiredate` ASC
-- 12
SELECT `deptno`,AVG(sal)
FROM t_employees
GROUP BY `deptno`
-- 13
SELECT `deptno`,COUNT(*)
FROM t_employees
GROUP BY `deptno`
-- 14
SELECT `job`,MAX(sal),MIN(sal),COUNT(*)
FROM t_employees
GROUP BY `job`
