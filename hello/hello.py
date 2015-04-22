
#print "plese enter your name:"
#name = raw_input()
#print "aha your name is " + name

#a = 'ABC'
#b = a + 'hehe'
#a = 'XYZ'
#print b

#import sys
#print sys.argc
#print $(notdir sys.argv[0])
#print sys.argv[1]

def calc_static_cycle_count(select_str):
	range_tuple=('0-99', '100-199', '200-299', '300-399', '400-499', '500-599', '600-699', '700-799', '800-899', '900-999', 
	'1000-1499', '1500-1999', '2000-2999', '3000-3999', '4000-4999', '5000-5999', '6000-6999', '7000-7999', '8000-8999', '9000-9999', 
	'10000-14999', '15000-19999', '20000',)

	fn = open(select_str,'r')
	input_list = fn.readlines()
	input_list = [int(x.strip()) for x in input_list]

	range_list = []
	range_inter= []
	range_num=len(range_tuple)
	
	for n in range(range_num):
		range_list.append([range_tuple[n],0])
	
	range_inter = [x.split('-') for x in range_tuple]
	range_inter.pop()
	range_inter = [[int(x[0]),int(x[1])] for x in range_inter]
		
	for cycle_count in input_list:
		if cycle_count >= int(range_tuple[-1]):
			range_list[-1][1] += 1
		else:
			for n in range(range_num-1):
				low = range_inter[n][0]
				high = range_inter[n][1]
				if cycle_count >= low and cycle_count <= high:
					range_list[n][1] += 1
					break
	
	for n in range(range_num):
		if len(range_tuple[n])<9:
			print range_list[n][0] +'\t\t' + str(range_list[n][1])
		else:
			print range_list[n][0] +'\t' + str(range_list[n][1])
	
	fn.close()
	
def main():
	calc_static_cycle_count('in.txt')
	
main()