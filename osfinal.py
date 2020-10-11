import os
a=[["NULL" for i in range(10)] for j in range(20)]
b="available"
c="not available"
dict={
	 "write": [100,3],
	 "read": [101,3],
	 "open": [102,3],
	 "close": [103,1],
	 "terminate": [104,1],
	 "end": [105,1],
	 "abort": [106,1],
	 "fork": [107,0],
	 "wait": [108,1],
	 "exit": [109,1],
	 "sleep": [110,1],
	 "alarm": [111,2],
	 "getppid": [112,0],
	 "pipe": [113,1],
	 "send": [114,2],
	 "receive": [115,2],
	 "cancel": [116,3],
	 "testcancel": [117,2],
	 "get_process_attribute":[118,4],
	"set_process_attribute": [119,4],
	"exec": [120,4]
}
t={
	 "write": [100,3],
	 "read": [101,3],
	 "open": [102,3],
	 "close": [103,1],
	 "terminate": [104,1],
	 "end": [105,1],
	 "abort": [106,1],
	 "fork": [107,0],
	 "wait": [108,1],
	 "exit": [109,1],
	 "sleep": [110,1],
	 "alarm": [111,2],
	 "getppid": [112,0],
	 "pipe": [113,1],
	 "send": [114,2],
	 "receive": [115,2],
	 "cancel": [116,3],
	 "testcancel": [117,2],
	 "get_process_attribute":[118,4],
	"set_process_attribute": [119,4],
	"exec": [120,4]
}
y={}
for key in dict.keys():
	y[key]=0
a[0]=dict["read"]
a[0].extend(["not available","unsigned int fd","char *buf","size_t count","NULL","NULL","NULL",1])
y["read"]=1
a[1]=dict["open"]
a[1].extend(["not available","unsigned int fd","const char *buf","size_t count","NULL","NULL","NULL",1])
y["open"]=1
a[2]=dict["wait"]
a[2].extend(["not available","int time","NULL","NULL","NULL","NULL","NULL",0])
y["wait"]=1
a[3]=dict["send"]
a[3].extend(["not available","char *msg","pid id","NULL","NULL","NULL","NULL",1])
y["send"]=1
a[4]=dict["receive"]
a[4].extend(["not available","char *msg","pid id","NULL","NULL","NULL","NULL",1])
y["receive"]=1
a[5]=dict["get_process_attribute"]
a[5].extend(["not available","char *per","char *mode","pid id","char *type", "NULL","NULL",1])
y["get_process_attribute"]=1
for i in range(6,20):
	a[i][2]=b

def isc(e):
	if((e>='a' and e<='z') or(e>='A' and e<='Z')):
		return 1
	elif(e==''):
		return 0
l=6
def exec(s):
	global l
	i=l
	for key in dict.keys():
		if(s==key):
			a[i][0]=dict[key][0]
			a[i][1]=dict[key][1]
			a[i][2]=c
			d=t[s][1]
			k=3
			y[s]+=1
			a[i][1]=d
			a[i][0]=t[key][0]
			if(s=="read" or s=="write" or s=="open" or s=="close"):
				w=input("Enter the File: ")
				while (not os.path.isfile(w)) or (not os.path.exists(w)):
					w= input("Whhoops! No such file! Please enter the name of the file you'd like to use: ")
				if(d>1):
					print("Enter the arguements: ")
					for j in range(d-1):
						z=str(input())
						a[i][k]=z
						k+=1
			else:	
				if(d>0):
					print("Enter the arguements: ")
					for j in range(d):
						z=str(input())
						a[i][k]=z
						k+=1
			for j in range(k,9):
				a[i][j]="NULL"
			x=str(input("enter the return value: "))
			a[i][9]=x
			i+=1
			print(s+" is added to the table ...!")
			for m in range(20):
				print(a[m],end="\n \n")
	if(i==20 and a[0][0]=="NULL"):
		l=0
	elif(i==20 and a[0][0]!="NULL"):
		comp()
	elif(a[i][0]!="NULL"):
		l=0
	else:
		l=i

def comp():
	global l
	j=0
	if(j<20):
		while(j<20 and a[j][2]=="available" ):
			j+=1
		if( j< 20 and a[j][2]=="not available"):
			for key in dict.keys():
				if(a[j][0]==t[key][0] and y[key]!=0):
					q=key
					print("after the completion of the execution of the "+q+" system call in the table: ",end="\n")
					for k in range(2):
						a[j][k]="NULL"
					for k in range(3,len(a[j])):
						a[j][k]="NULL"
					a[j][2]=b
					y[key]-=1
					for m in range(20):
						print(a[m],end="\n \n")
					print(q+" has completed its execution ",end="\n")

			if(a[0][0]=="NULL" and a[j+1][0]=="NULL"):
				l=0
		elif(j>=20):
			return

while(1):
	q=str(input())
	if(isc(q)==1):
		s=str(input("enter the command: "))
		if s in dict.keys():
			exec(s)
		else:
			print("Invalid System Call...")
	elif(isc(q)==0):
		e=1
		for i in range(len(a)):
			if(a[i][0]!="NULL"):
				e=0
				break
		if(e==0):
			print("During the execution of the system calls in the table: ")
			comp()
		else:
			print("All System Calls in the table are executed...")
			l=0
			i=0



