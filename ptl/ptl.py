################################################################################
#Filename    : ptl.py
#Version     : Ver 0.1
#Author      : Haven
#Date        : 2015.04.20
#Description : this python script is help for analysing performance trace log
#Usage       : ptl.py MCU_x "filter string"
#              eg ptl.py MCU_0 "Ahci task start"
#Modify      :
#20150420    Haven create file
################################################################################

import sys
import glob

def get_input_filename(mcux):
	filelist = glob.glob("*.txt")
	
	for filename in filelist:
		if mcux in filename:
			input_file_name = filename
			break

	if 'input_file_name' in dir():
		print "input file is " + input_file_name
		return input_file_name
	else:
		print "can not find *"+mcux+"*.txt, please check your input param and exist log files"
		exit()

def select_target_log(input_file_name, select_str):
	output_file_name = select_str.replace(' ','_') + '.txt'
	input_file = open(input_file_name, 'r')
	output_file = open(output_file_name, 'w')
	list = input_file.readlines()

	for line in list:
		if select_str in line:
			output_file.write(line)

	input_file.close()
	output_file.close()

def sort_cycle_count(select_str):
	input_file_name = select_str.replace(' ','_') + '.txt'
	output_file_name = select_str.replace(' ','_') + '_sorted' + '.txt'
	input_file = open(input_file_name, 'r')
	output_file = open(output_file_name, 'w')

	list = input_file.readlines()
	list = [x.split('ulDiffCycles = ') for x in list]
	list = [x[1] for x in list]
	list = [x.strip() for x in list]
	list = [int(x,16) for x in list]
	list.sort(reverse=True)
	list = [str(x) + '\n' for x in list]

	output_file.writelines(list)

	input_file.close()
	output_file.close()
	print "result saved to " + output_file_name

def calc_static_cycle_count(select_str):
	range_tuple=('0-99', '100-199', '200-299', '300-399', '400-499', '500-599', '600-699', '700-799', '800-899', '900-999', 
	'1000-1499', '1500-1999', '2000-2999', '3000-3999', '4000-4999', '5000-5999', '6000-6999', '7000-7999', '8000-8999', '9000-9999', 
	'10000-14999', '15000-19999', '20000',)

	input_filename = select_str.replace(' ','_') + '_sorted' + '.txt'
	
	fn = open(input_filename,'r')
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
	
	print '\nstatistical result:'
	for n in range(range_num):
		if len(range_tuple[n])<9:
			print range_list[n][0] +'\t\t' + str(range_list[n][1])
		else:
			print range_list[n][0] +'\t' + str(range_list[n][1])
	
	fn.close()


def main():
	mcux = sys.argv[1]
	select_str = sys.argv[2]
	
	#preparing input_filename
	input_filename = get_input_filename(mcux)
	
	#first step, select trace log strings for target trace location by the input filter string
	select_target_log(input_filename, select_str)

	#second step, filter cycle count and sorted them.
	sort_cycle_count(select_str)
	
	#3rd step, calc_static_cycle_count
	calc_static_cycle_count(select_str)

main()	