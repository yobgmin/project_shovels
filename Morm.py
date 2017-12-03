import sqlalchemy
import os
from sqlalchemy import types,create_engine,Column,Integer,String, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from datetime import timedelta
import re

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

class sec_evt_tbl(Base):
	__tablename__='sec_evt_tbl'
	idx=Column(types.Integer,primary_key=True)
	EventTime=Column(types.DateTime)
	Hostname=Column(types.String)
	EventID=Column(types.Integer)
	SourceName=Column(types.String)
	ProcessID=Column(types.Integer)
	ThreadID=Column(types.Integer)
	SubjectUserSid=Column(types.String)
	SubjectUserName=Column(types.String)
	SubjectDomainName=Column(types.String)
	SubjectLogonId=Column(types.String)
	TargetUserSid=Column(types.String)
	TargetUserName=Column(types.String)
	TargetDomainName=Column(types.String)
	TargetLogonId=Column(types.String)
	TargetServerName=Column(types.String)
	LogonType=Column(types.String)
	WorkstationName=Column(types.String)
	ProcessName=Column(types.String)
	IpAddress=Column(types.DateTime)
	IpPort=Column(types.String)
	EventReceivedTime=Column(types.DateTime)
	SourceModuleName=Column(types.String)
	SourceModuleType=Column(types.String)
	TargetLogonId=Column(types.String)
	EventReceviedTime=Column(types.String)

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

def findParent_Image(PrcImage, EvtTime):
	for i in session.query(proc_tbl).filter(proc_tbl.Image.like(PrcImage)).filter(proc_tbl.EventTime.like(EvtTime)).filter(~proc_tbl.ParentImage.like("NULL")):
		print "ParentImage : ", i.ParentImage, i.Image
		return i.ParentImage

def findChildren(PrcImage, EvtTime):
	for i in session.query(proc_tbl).filter(proc_tbl.ParentImage.like(PrcImage)).filter(proc_tbl.EventTime.between(EvtTime+timedelta(seconds=-1), EvtTime+timedelta(seconds=2))):
		print "ChildImage : ", i.Image, i.Hostname, i.CommandLine
		return i.Image


def network_connection(PrcImage, HstName, EvtTime):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like(PrcImage)).filter(network_connect_tbl.EventTime.between(EvtTime+timedelta(seconds=-3), EvtTime+timedelta(seconds=3))):
		print "Network Connection : ", i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp, i.Image
		return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)

def network_connection_EventTime(EvtTime, HstName, Img):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.EventTime.between(EvtTime+timedelta(seconds=-3), EvtTime+timedelta(seconds=3))).filter(network_connect_tbl.Image.like(Img)):
		print "Network Connection : ", i.EventTime, i.Image, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp
		return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)

def system_network_connection(EvtTime, HstName):
	for i in session.query(network_connect_tbl).filter(network_connect_tbl.EventTime.between(EvtTime+timedelta(seconds=-2), EvtTime+timedelta(seconds=2))).filter(network_connect_tbl.Image.like('System')):
		print "System Net connect  ", i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp
		return (i.EventTime, i.Hostname, i.DestinationHostname, i.SourceIp, i.DestinationIp)


def printLine():
	print "===================================================================================================="

def host_process_create(EvtTime, HstName):
	for i in session.query(proc_tbl).filter(~proc_tbl.Hostname.like(HstName)).filter(proc_tbl.EventTime.between(EvtTime+timedelta(seconds=-2), EvtTime+timedelta(seconds=2))):
		print "Host Process Create ", i.Image, i.EventTime, i.Hostname

for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%cmd.exe')).filter(~proc_tbl.ParentImage.like('%explorer.exe')).filter(~proc_tbl.ParentImage.like('%vmtoolsd.exe')).filter(~proc_tbl.ParentImage.like('%cmd.exe')):
	print i.EventTime, i.ProcessID,i.Image,i.ParentImage,i.Hostname
	
	HstName = system_network_connection(i.EventTime, i.Hostname) # plus minus 2 seconds
	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	HstName = None

	if u'winrshost.exe' in i.ParentImage:
		HstName = network_connection('%winrs.exe', i.Hostname, i.EventTime)
		if HstName is not None:
			host_process_create(i.EventTime, i.Hostname)
		print "\n"
		continue
	elif u'WmiPrvSE.exe' in i.ParentImage:
		HstName = network_connection('%wmic.exe', i.Hostname, i.EventTime)
		if HstName is not None:
			host_process_create(i.EventTime, i.Hostname)
		print "\n"
		continue

	PrcList = [i.Image, i.ParentImage]
	Img = findParent_Image('%'+i.ParentImage.split('\\')[-1], i.EventTime)
	if Img is not None:
		PrcList.append(Img)
	
	for Img in PrcList:
		HstName = network_connection_EventTime(i.EventTime, i.Hostname, '%'+Img.split('\\')[-1]) # plus minus 2 seconds

	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	print "\n"

printLine()
for i in session.query(file_create_tbl).filter(~file_create_tbl.TargetFilename.like('%System32%')).filter(file_create_tbl.Image.like('System')).filter(~file_create_tbl.TargetFilename.like('%System Volume Information%')):
	print "System File Create -", i.EventTime, i.TargetFilename, i.Hostname

	HstName = system_network_connection(i.EventTime, i.Hostname) # plus minus 2 seconds
	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	HstName = None

	Img = findParent_Image('%'+i.TargetFilename.split('\\')[-1], i.EventTime)
	if Img:
		Img = '%'+Img.split('\\')[-1]
		HstName = network_connection_EventTime(i.EventTime, i.Hostname, Img) # plus minus 2 seconds

	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	print "\n"

printLine()
for i in session.query(raw_access_read_tbl).filter(~raw_access_read_tbl.Image.like('%Everything.exe')).filter(~raw_access_read_tbl.Image.like('System')).filter(~raw_access_read_tbl.Image.like('%System32%')).filter(~raw_access_read_tbl.Image.like('%TrustedInstaller.exe')):
	print i.ProcessID, i.Image, i.EventTime, i.Hostname

	HstName = system_network_connection(i.EventTime, i.Hostname) # plus minus 2 seconds
	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	HstName = None

	Img = findParent_Image(i.Image, i.EventTime)
	if Img:
		Img = '%'+Img.split('\\')[-1]
		HstName = network_connection_EventTime(i.EventTime, i.Hostname, Img) # plus minus 2 seconds

	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	print "\n"
# not permitted RawAccessRead

printLine()
for i in session.query(proc_access_tbl).filter(proc_access_tbl.TargetImage.like('%lsass.exe')).filter(~proc_access_tbl.SourceImage.like('%System32%')).filter(proc_access_tbl.EventID.like('8')):
	print "PwDump(Remote) or WCE", i.SourceImage, i.TargetImage, i.EventTime, i.GrantedAccess, i.Hostname
	HstName = system_network_connection(i.EventTime, i.Hostname) # plus minus 2 seconds
	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	HstName = None

	Img = findParent_Image('%'+i.SourceImage.split('\\')[-1], i.EventTime)
	if Img:
		Img = '%'+Img.split('\\')[-1]
		HstName = network_connection_EventTime(i.EventTime, i.Hostname, Img) # plus minus 2 seconds

	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	print "\n"


	
printLine()
for i in session.query(proc_access_tbl).filter(proc_access_tbl.TargetImage.like('%lsass.exe')).filter(proc_access_tbl.GrantedAccess.like('0x1010')).filter(proc_access_tbl.EventID.like('10')):
	print "Mimikatz - logonpasswords", i.SourceImage, i.TargetImage, i.EventTime, i.GrantedAccess, i.Hostname

	HstName = system_network_connection(i.EventTime, i.Hostname) # plus minus 2 seconds
	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	HstName = None

	Img = findParent_Image('%'+i.SourceImage.split('\\')[-1], i.EventTime)
	if Img:
		Img = '%'+Img.split('\\')[-1]
		HstName = network_connection_EventTime(i.EventTime, i.Hostname, Img) # plus minus 2 seconds

	if HstName is not None:
		host_process_create(i.EventTime, i.Hostname)
	print "\n"


printLine()
netuse = re.compile("\s*net\s+use\s+\\\\.*$")
netshare=re.compile(".*net1\s+share\s+.*\\:.*")
for i in session.query(proc_tbl).filter(or_(proc_tbl.Image.like('%net1.exe'),proc_tbl.Image.like('%net.exe'))).filter(proc_tbl.EventID.like('1')):
	print "net1.exe, net.exe", i.Image, i.EventTime, i.Hostname, i.CommandLine
	if bool(netuse.match(i.CommandLine)):
		print "net use Detected"
		system_network_connection(i.EventTime, i.Hostname)
		print "\n"
	elif bool(netshare.match(i.CommandLine)):
		print "net share(shareFolder create) Detected"
		system_network_connection(i.EventTime, i.Hostname)
		print "\n"

for i in session.query(pipe_tbl).filter(pipe_tbl.Image.like('%net1.exe')).filter(pipe_tbl.PipeName.like('\browser')).filter(pipe_tbl.EventID.like('18')):
	print "net1.exe - net view", i.Image, i.EventTime, i.Hostname

for i in session.query(pipe_tbl).filter(pipe_tbl.Image.like('%net1.exe')).filter(pipe_tbl.PipeName.like('\wkssvc')).filter(pipe_tbl.EventID.like('18')):
	print "net1.exe - net use", i.Image, i.EventTime, i.Hostname

printLine()
for i in session.query(proc_tbl).filter(proc_tbl.ParentImage.like('%WmiPrvSE.exe')).filter(proc_tbl.EventID.like('1')):
	print "wmic - Destination", i.EventTime, i.Hostname, i.ParentImage, i.Image
	print "\n"

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%wmic.exe')).filter(network_connect_tbl.EventID.like('3')):
	print "wmic - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp

printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%WScript.exe')).filter(proc_tbl.EventID.like('1')):
	print "wmiexec.vbs", i.Image, i.EventTime, i.Hostname, i.CommandLine
	findChildren('%'+i.Image.split('\\')[-1], i.EventTime)
	print "\n"
	
printLine()
for i in session.query(proc_tbl).filter(proc_tbl.Image.like('%WinrsHost.exe')).filter(proc_tbl.EventID.like('1')):
	print "winrs - Destination", i.Image, i.EventTime, i.Hostname, i.ParentImage
	findChildren('%'+i.Image.split('\\')[-1], i.EventTime)
	print "\n"

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%winrs.exe')).filter(network_connect_tbl.EventID.like('3')):
	print "winrs - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp

for i in session.query(network_connect_tbl).filter(network_connect_tbl.Image.like('%winrs.exe')).filter(network_connect_tbl.EventID.like('3')).filter(network_connect_tbl.SourcePort is 5985):
	print "winrs - Source", i.Image, i.EventTime, i.Hostname, i.SourceIp, i.DestinationIp

printLine()
for i in session.query(sec_evt_tbl).filter(sec_evt_tbl.EventID.like('4624')).filter(sec_evt_tbl.SubjectDomainName.like('-')).filter(sec_evt_tbl.LogonType.like('3')):
	print "Security Log - Remote", i.EventTime, i.ProcessName, i.WorkstationName, i.TargetServerName
