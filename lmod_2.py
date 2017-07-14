from __future__ import print_function
#understanding modulo
#
my_bucket=[]

[my_bucket.append(i) for i in range(1, 100) if i % 4 == 3]
		
for i in range(1, 100):
	if i % 4 == 3:
		my_bucket.append(i)

print(my_bucket)
