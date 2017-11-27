import sqlalchemy
import os
from sqlalchemy import types,create_engine,Column,Integer,String, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('mysql://root:12345@localhost/winlogs?charset=utf8',convert_unicode=False)
Session=sessionmaker(bind=engine)	#Create session object that can access query
session=Session()
Base=declarative_base()

class proc_tbl(Base):
	__tablename__='proc_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	CommandLine=Column(types.String)
	CurrentDirectory=Column(types.String)
	User=Column(types.String)
	LogonGuid=Column(types.String)
	LogonId=Column(types.String)
	TerminalSessionid=Column(types.String)
	IntegrityLevel=Column(types.String)
	Hashes=Column(types.String)
	ParentProcessGuid=Column(types.String)
	ParentProcessId=Column(types.String)
	ParentImage=Column(types.String)
	ParentCommandLine=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class change_createtime_tbl:
	__tablename__='change_createtime_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	TargetFilename=Column(types.String)
	CreationUtcTime=Column(types.DateTime)
	PreviousCreationUtcTime=Column(types.DateTime)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class file_create_tbl:
	__tablename__='file_create_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	TargetFilename=Column(types.String)
	CreationUtcTime=Column(types.DateTime)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class image_loaded_tbl:
	__tablename__='image_loaded_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ImageLoaded=Column(types.String)
	Hashes=Column(types.String)
	Signed=Column(types.String)
	Signature=Column(types.String)
	SignatureStatus=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	Image=Column(types.String)
	ProcessGuid=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class network_connect_tbl:
	__tablename__='network_connect_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	User=Column(types.String)
	Protocol=Column(types.String)
	Initiated=Column(types.String)
	SourceIsIpv6=Column(types.String)
	SourceIp=Column(types.String)
	SourcePort=Column(types.String)
	SourcePortName=Column(types.String)
	DestinationIsIpv6=Column(types.String)
	DestinationIp=Column(types.String)
	DestinationHostname=Column(types.String)
	DestinationPort=Column(types.String)
	DestinationPortName=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class pipe_tbl:
	__tablename__='pipe_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	PipeName=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	Image=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class proc_access_tbl:
	__tablename__='proc_access_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	SourceProcessGuid=Column(types.String)
	SourceProcessId=Column(types.String)
	SourceThreadId=Column(types.String)
	SourceImage=Column(types.String)
	TargetProcessGuid=Column(types.String)
	TargetProcessId=Column(types.String)
	TargetImage=Column(types.String)
	NewThreadId=Column(types.String)
	StartAddress=Column(types.String)
	StartModule=Column(types.String)
	StartFunction=Column(types.String)
	GrantedAccess=Column(types.String)
	CallTrace=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	TargeImage=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class raw_access_read_tbl:
	__tablename__='raw_access_read_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	Device=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass

class reg_tbl:
	__tablename__='reg_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	AccountName=Column(types.String)
	UserID=Column(types.String)
	AccountType=Column(types.String)
	UtcTime=Column(types.DateTime)
	ProcessGuid=Column(types.String)
	Image=Column(types.String)
	TargetObject=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	Details=Column(types.String)

	def __init__(self):
		pass
	def __repr__(self):
		pass


def whatgidex(guid):
	for ii in session.query(result_tbl).filter(result_tbl.ProcessGuid==guid):
		return ii.Gidex
class result_tbl:
	idx=0
	gidex=0
	tbl_number=0
	tbl_idx=0

	def __init__(self,gi,tbl_n,tbl_i):
		self.gidex=gi
		self.tbl_number=tbl_n
		self_tbl_idx=tbl_i

Intell1=[]
Intell1_Guid=[]
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%cmd.exe')).filter(~proc_tbl.ParentImage.like('%explorer.exe')).filter(~proc_tbl.ParentImage.like('%vmtoolsd.exe')):
	Intell1_Guid.append(i.ProcessGuid)#create object
	Intell1.append(i.Image)
	print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid,i.ParentProcessGuid
print "Start Straw"
x=0
for in1 in Intell1:
	for i in session.query(proc_tbl).filter(proc_tbl.Image==in1).filter(proc_tbl.ProcessGuid==Intell1_Guid[x]).filter(proc_tbl.EventID=='1'):
#		gid=whatgidx(i.ProcessGuid)
		print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid
		#create object
	x+=1
print "Low 1"
x=0
for in1 in Intell1:
	for i in session.query(proc_tbl).filter(proc_tbl.ParentImage==in1).filter(proc_tbl.ParentProcessGuid==Intell1_Guid[x]).filter(proc_tbl.EventID=='1'):
		print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid,i.ParentProcessGuid
	x+=1
#	print i.ProcessID,i.Image

for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%cmd.exe')).filter(~proc_tbl.ParentImage.like('%explorer.exe')).filter(~proc_tbl.ParentImage.like('%vmtoolsd.exe')):
	Intell1_Guid.append(i.ProcessGuid)#create object
	Intell1.append(i.Image)
	print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid,i.ParentProcessGuid

for i in session.query(proc_access_tbl):
	print i.EventTime