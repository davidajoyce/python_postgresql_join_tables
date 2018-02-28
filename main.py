#import csv_to_array as csv
import sys
import python_postgresql as pypsql
import csv


def load_file(filename):
    fp = open(filename, 'Ur')
    data_list = []
    count = 0
    for line in fp:
	if count > 0:
        	data_list.append(tuple(line.strip().split(',')))
	count = count+1
    fp.close()
    return data_list



def main():

	data = load_file('higher_than.csv')
	
	#print data
	pypsql.insert_news_list(data)


if __name__=='__main__':

	main()
