/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
列：d.deptno, d.dname, d.loc, 部门人数
表：dept d, emp e
条件：e.deptno=d.deptno
*/
SELECT d.*,n.cnt
FROM t_dept d
JOIN (SELECT deptno,COUNT(*) cnt FROM t_employees GROUP BY deptno) n
ON d.deptno = n.deptno

/*
3. 列出所有员工的姓名及其直接上级的姓名。
列：员工姓名、上级姓名
表：emp e, emp m
条件：员工的mgr = 上级的empno
*/
SELECT t.ename,d.ename
FROM t_employees t
JOIN t_employees d
ON t.`MGR` = d.`empno`
ORDER BY d.`ename` ASC


/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
列：e.empno, e.ename, d.dname
表：emp e, emp m, dept d
条件：e.hiredate<m.hiredate
思路：
1. 先不查部门名称，只查部门编号!
列：e.empno, e.ename, e.deptno
表：emp e, emp m
条件：e.mgr=m.empno, e.hiredate<m.hireadate
*/
SELECT e.empno,e.ename,d.dname
FROM t_employees e
JOIN t_dept d ON e.`deptno` = d.`deptno`
JOIN t_employees m ON e.`MGR` = m.`empno`
WHERE e.`hiredate` < m.`hiredate` 


/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
列：* 
表：emp e, dept d
条件：e.deptno=d.deptno
*/
SELECT d.dname,e.*
FROM t_employees e RIGHT OUTER JOIN t_dept d
ON d.deptno = e.deptno


/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
列：job, count(*)
表：emp e
条件：min(sal) > 15000
分组：job
*/
SELECT job,COUNT(*)
FROM t_employees
GROUP BY job
HAVING MIN(sal) > 15000


/*
8. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。
列：e.ename
表：emp
条件：e.deptno=(select deptno from dept where dname='公关部')
*/
SELECT e.ename
FROM t_employees e
JOIN t_dept d ON e.deptno = d.deptno
WHERE d.dname = '公关部'


/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
列：* 
表：emp e
条件：sal>(查询出公司的平均工资)
*/
/*
create table `salgrade` (
	`grade`	VARCHAR(20),
	`losal`	int(10),
	`hisal`	int(10)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
insert into salgrade value ('一档',0,2000),('二档',2000,3000),('三档',3000,4000),('四档',4000,99999)
*/

SELECT e.*,d.dname,m.ename,s.grade
FROM t_employees e
JOIN t_dept d ON e.deptno=d.deptno
JOIN t_employees m ON e.MGR=m.empno
JOIN salgrade s ON e.sal BETWEEN losal AND hisal
WHERE e.sal > (SELECT AVG(sal) FROM t_employees)

/*
10.列出与张飞从事相同工作的所有员工及部门名称。
列：e.*, d.dname
表：emp e, dept d
条件：job=(查询出张飞的工作)
*/
SELECT e.ename,d.dname
FROM t_employees e
JOIN t_dept d ON e.deptno = d.deptno
WHERE e.job = (SELECT job FROM t_employees WHERE ename = "张飞")


/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
列：e.ename, e.sal, d.dname
表：emp e, dept d
条件；sal>all (30部门薪金)
*/
SELECT e.ename,e.sal,d.dname
FROM t_employees e
JOIN t_dept d ON e.deptno = d.deptno
HAVING sal > ALL (SELECT sal FROM t_employees WHERE deptno = 30)
