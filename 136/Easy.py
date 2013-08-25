num_students, num_grades = map(float, raw_input().split())
avgs, students = [], []
for i in xrange(int(num_students)):
  line = raw_input().split()
  grades = map(int, line[1:])
  student_avg = sum(grades)/num_grades
  avgs.append(student_avg)
  students.append((line[0], student_avg))
print "%.2f" % (sum(avgs)/num_students)
print "\n".join(x[0] + " " + str("%.2f" % x[1]) for x in students)
