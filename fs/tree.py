#!/usr/bin/python
import os
import sys
'''
HDFS tree util, linux shell tree
** HADOOP_HOME must be set before use it **
'''

HADOOP_HOME='/home/hadoop/hadoop-curent'

HADOOP=HADOOP_HOME+'/bin/hadoop'
LS=HADOOP+' fs -ls '

def tree(level, prefix, path):
  if level == 0:
    return
  cmd=LS+path
  output=os.popen(cmd)
  found=output.readline()
  if found[0] == 'F':
    num = int(found.split()[1])
    x=0
    while x<num:
      x = x+1
      line=output.readline()
      subpath=line.split()[7]
      print prefix+subpath.split('/')[-1]
      if line[0]=='d':
	tree(level-1, '|\t'+prefix,subpath)


def usage(){
  print "tree.py [-l level]"
  print "\t level: recurive level"
}

if __name__=='__main__':
  level = -1
  for i in range(0, len(sys.argv)) :
    if sys.argv[i]=='-l':
      level = int(sys.argv[i+1])
      if level <0:
	level = -1
      break;

  print sys.argv[1]
  tree(level, '|--',sys.argv[1])
