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

class change_createtime_tbl(Base):
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

class file_create_tbl(Base):
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

class image_loaded_tbl(Base):
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

class network_connect_tbl(Base):
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

class pipe_tbl(Base):
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

class proc_access_tbl(Base):
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

	def __init__(self):
		pass
	def __repr__(self):
		pass

class raw_access_read_tbl(Base):
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

class reg_tbl(Base):
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

def Upper(guid):
	for i in session.query(proc_tbl).filter(proc_tbl.ProcessGuid==guid).filter(proc_tbl.EventID=='1'):
		print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid


class result_tbl:
	idx=0
	gidex=0
	tbl_number=0
	tbl_idx=0

	def __init__(self,gi,tbl_n,tbl_i):
		self.gidex=gi
		self.tbl_number=tbl_n
		self_tbl_idx=tbl_i

def findParent(PrcImage, PrcId):
	for i in session.query(proc_tbl).filter(proc_tbl.Image.like(PrcImage)).filter(proc_tbl.ProcessID.like(PrcId)):
		if i is not None:
			print "ParentImage : ", i.ParentImage
			return i.ParentImage, i.ProcessID
		else:
			return None

def findParent_Image(PrcImage):
	for i in session.query(proc_tbl).filter(proc_tbl.Image.like(PrcImage)):
		if i is not None:
			print "ParentImage : ", i.ParentImage
			return i.ParentImage
		else:
			return None

def findChildren(PrcImage, PrcId):
	for i in session.query(proc_tbl).filter(proc_tbl.ParnetImage.like(PrcImage)).filter(proc_tbl.ProcessID.like(PrcId)):
		print "ChildImage : ", i. Image
		return (i.Image, i.ProcessID)


def network_connection(PrcImage, HstName):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like(PrcImage)).filter(~network_connect_tbl.Hostname.like(HstName)):
		print "Network Connection : ", i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp
		return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)

def network_connection_EventTime(EvtTime, HstName):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.EventTime.like(EvtTime)).filter(~network_connect_tbl.Hostname.like(HstName)):
		if i is not None:
			print "Network Connection : ", i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp
			return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)
		else:
			return None

def system_network_connection(EvtTime, HstName):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.EventTime.like(EvtTime)).filter(~network_connect_tbl.Hostname.like(HstName)).filter(network_connect_tbl.Image.like('System')):
		print "System Net connect  ", i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp
		return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)


def printLine():
	print "===================================================================================================="

def host_prcess_create(EvtTime, HstName):
	for i in session.query(proc_tbl).filter(proc_tbl.Hostname.like(HstName)).filter(proc_tbl.EventTime.like(EvtTime)):
		print "Host Process Create ", i.Image, i.EventTime, i.Hostname, i.CommandLine
		return (i.Image, i.EventTime, i.Hostname, i.CommandLine)


Intell1=[]
Intell1_Guid=[]
Intell1_PImage=[]
Intell1_PGuid=[]
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%cmd.exe')).filter(~proc_tbl.ParentImage.like('%explorer.exe')).filter(~proc_tbl.ParentImage.like('%vmtoolsd.exe')):
	Intell1_Guid.append(i.ProcessGuid)#create object
	Intell1.append(i.Image)
	Intell1_PImage.append(i.ParentImage)
	Intell1_PGuid.append(i.ParentProcessGuid)
	print i.ProcessID,i.Image,i.ParentImage,i.ProcessGuid,i.ParentProcessGuid
	if(i.ParentImage is '%cmd.exe'):
		upper(i.ParentProcessGuid)
"""
	PrcList=[]
	Img = i.Image
	Pid = i.ProcessID
	temp = findParent(Img, Pid)

	while temp is not None:
		temp = findParent(Img, Pid)
		Img = temp[0]
		Pid = temp[1]
	for prc in PrcList:
		net_con = network_connection((prc[0], prc[1]), i.Hostname[0])
		if net_con[0]:
			for i in session.query(proc_tbl).filter(proc_tbl.EventTime.like(net_con[0])).filter(proc_tbl.Hostname.like(net_con[1])):
				print "Process from Host", net_con[0], net_con[1], net_con[2], net_con[3], net_con[4]"""

print "Up 1"
x=0
for in1 in Intell1_PImage:
	for i in session.query(proc_tbl).filter(proc_tbl.Image==in1).filter(proc_tbl.ProcessGuid==Intell1_PGuid[x]).filter(proc_tbl.EventID=='1'):
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

printLine()
for i in session.query(file_create_tbl).filter(~file_create_tbl.TargetFilename.like('%System32%')).filter(file_create_tbl.Image.like('System')).filter(~file_create_tbl.TargetFilename.like('%System Volume Information%')):
	print "System File Create -", i.EventTime, i.TargetFilename, i.Hostname

	HstName = system_network_connection(i.EventTime, i.Hostname)

	if HstName is not None:
		for i in session.query(proc_tbl).filter(proc_tbl.Hostname.like(HstName[0])).filter(proc_tbl.EventTime.like(i.EventTime)):
			print "Host Process Create - ", i.Image, i.EventTime, i.Hostname, i.CommandLine
	print '%'+i.TargetFilename.split('\\')[-1]
	Img = findParent_Image('%'+i.TargetFilename.split('\\')[-1])

	if Img is not None:
		HstName = network_connection_EventTime(i.EventTime, i.Hostname)

	if HstName is not None:
		for i in session.query(proc_tbl).filter(proc_tbl.Hostname.like(HstName[0])).filter(proc_tbl.EventTime.like(i.EventTime)):
			print "Host Process Create - ", i.Image, i.EventTime, i.Hostname, i.CommandLine

printLine()
for i in session.query(raw_access_read_tbl).filter(~raw_access_read_tbl.Image.like('%Everything.exe')).filter(~raw_access_read_tbl.Image.like('System')).filter(~raw_access_read_tbl.Image.like('%System32%')).filter(~raw_access_read_tbl.Image.like('%TrustedInstaller.exe')):
	print i.ProcessID, i.Image, i.EventTime, i.Hostname
# not permitted RawAccessRead
printLine()
for i in session.query(proc_access_tbl).filter(proc_access_tbl.TargetImage.like('%lsass.exe')).filter(~proc_access_tbl.SourceImage.like('%System32%')).filter(proc_access_tbl.EventID.like('8')):
	print "PwDump(Remote) or WCE", i.SourceImage, i.TargetImage, i.EventTime, i.GrantedAccess, i.Hostname


"""	
printLine()
for i in session.query(proc_access_tbl).filter(proc_access_tbl.TargetImage.like('%lsass.exe')).filter(proc_access_tbl.GrantedAccess.like('0x1010')).filter(proc_access_tbl.EventID.like('10')):
	print "Mimikatz - logonpasswords", i.SourceImage, i.TargetImage, i.EventTime, i.GrantedAccess, i.Hostname
	PrcList=[]
	PrcList.append((i.SourceImage, i.ProcessID)
	Img = i.SourceImage
	Pid = i.ProcessID
	while Img!=None:
		PrcList.append((Img, Pid))
		Img, Pid = findParent(Img, Pid)
	for prc in PrcList:
		net_con = network_connection((prc[0], prc[1]), i.Hostname[0])
		if net_con[0]:
			for i in session.query(proc_tbl).filter(proc_tbl.EventTime.like(net_con[0])).filter(proc_tbl.Hostname.like(net_con[1])):
				print "Process from Host", net_con[0], net_con[1], net_con[2], net_con[3], net_con[4]

printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%net1.exe')).filter(~proc_tbl.Image.like('%net.exe')).filter(proc_tbl.EventID.like('1')):
	print "net1.exe, net.exe", i.Image, i.EventTime, i.Hostname, i.CommandLine

for i in session.query(pipe_tbl).filter(pipe_tbl.Image.like('%net1.exe')).filter(pipe_tbl.PipeName.like('\browser')).filter(pipe_tbl.EventID.like('18')):
	print "net1.exe - net view", i.Image, i.EventTime, i.Hostname

for i in session.query(pipe_tbl).filter(pipe_tbl.Image.like('%net1.exe')).filter(pipe_tbl.PipeName.like('\wkssvc')).filter(pipe_tbl.EventID.like('18')):
	print "net1.exe - net use", i.Image, i.EventTime, i.Hostname

printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%WmiPrvSE.exe')).filter(proc_tbl.EventID.like('1')):
	print "wmic - Destination", i.Image, i.EventTime, i.Hostname, i.ParentImage

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%wmic.exe')).filter(network_connect_tbl.EventID.like('3')):
	print "wmic - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp

printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%WScript.exe')).filter(proc_tbl.EventID.like('1')):
	print "wmiexec.vbs", i.Image, i.EventTime, i.Hostname, i.CommandLine
	
printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%WinrsHost.exe')).filter(proc_tbl.EventID.like('1')):
	print "winrs - Destination", i.Image, i.EventTime, i.Hostname, i.ParentImage

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%winrs.exe')).filter(network_connect_tbl.EventID.like('3')):
	print "winrs - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%winrs.exe')).filter(network_connect_tbl.EventID.like('3')).filter(network_connect_tbl.SourcePort is 5985):
	print "winrs - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp
"""
