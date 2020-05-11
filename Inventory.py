# Setting Config Options
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', False)


# Importing Resorces and Libraries
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, WipeTransition
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import subprocess
from kivy.uix.dropdown import DropDown
import datetime
import random
import sqlite3

# Establishing SQL Connection
global conn #Defines conn as a global variable for all class'
conn = sqlite3.connect('C:/Users/jarnold/Desktop/seinv.db')
c = conn.cursor()


#defines dropdown menu class
class DropDownMenu(DropDown):
	def test(self):
		subprocess.call([r'test.bat'])


#class to link screens to dropdown menu
class LeftMenu:
    def open_menu(self, anchor):
        DropDownMenu().open(anchor)

# Creates screen named MainScreen
class MainScreen(Screen, LeftMenu):
	pass #space holder as nothing in on this screen yet

# Class to define NewDVR screen
class NewDVR(Screen, LeftMenu):

	#variable for SQL query to allow variables without sql injection
	insert_dvr_query = "INSERT INTO DVRs(IventoryID, Notes, DateRecieved, DateSentOut, Property) VALUES (?,?,?,?,?)"

	#define action for submit button
	def submitdvr(self):
		c.execute("SELECT Count(IventoryID) FROM DVRs")
		num_len = 5
		count = c.fetchone()[0] + 1
		count = str(count)
		string_output = "0"*(num_len-len(count)) + count
		c.execute(NewDVR.insert_dvr_query, ('DVR'+str(string_output),str(self.dvrnotes.text),str(datetime.date.today()),'NA','NA'))
		conn.commit()




class NewRTR(Screen, LeftMenu):

	insert_rtr_query = "INSERT INTO Routers(IventoryID, ModelNumber, Notes, DateRecieved, DateSentOut, Property) VALUES (?,?,?,?,?,?)"

	def submitrtr(self):
		if self.rtrtog1.state == 'down':
			c.execute("SELECT Count(IventoryID) FROM routers")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewRTR.insert_rtr_query, ('RTR'+str(string_output),'1200b', str(self.rtrnotes.text),str(datetime.date.today()),'NA','NA'))
			conn.commit()
		
		elif self.rtrtog2.state == 'down':
			c.execute("SELECT Count(IventoryID) FROM routers")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewRTR.insert_rtr_query, ('RTR'+str(string_output),'1400', str(self.rtrnotes.text),str(datetime.date.today()),'NA','NA'))
			conn.commit()
		
		elif self.rtrtog3.state == 'down':
			c.execute("SELECT Count(IventoryID) FROM routers")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewRTR.insert_rtr_query, ('RTR'+str(string_output),'1650', str(self.rtrnotes.text),str(datetime.date.today()),'NA','NA'))
			conn.commit()
		else:
			print ('Form Not Complete')


class NewPHN(Screen, LeftMenu):

	insert_phn_query = "INSERT INTO Phones(IventoryID, ModelNumber, Condition, IMEI, Notes, DateRecieved, DateSentOut, PhoneNumber, AssignedUser ) VALUES (?,?,?,?,?,?,?,?,?)"
	
	def submitphn(self):
		if self.imei.text == '':
			print ("Form Not Complete")
		else:
			if self.phntog1.state == 'down':

				if self.phntog3.state == 'down':
					c.execute("SELECT Count(IventoryID) FROM Phones")
					num_len = 5
					count = c.fetchone()[0] + 1
					count = str(count)
					string_output = "0"*(num_len-len(count)) + count
					c.execute(NewPHN.insert_phn_query, ('PHN'+str(string_output),'S8+', 'Used', str(self.imei.text), str(self.phnnotes.text),str(datetime.date.today()),'NA','NA', 'NA'))
					conn.commit()

				elif self.phntog4.state == 'down':
					c.execute("SELECT Count(IventoryID) FROM Phones")
					num_len = 5
					count = c.fetchone()[0] + 1
					count = str(count)
					string_output = "0"*(num_len-len(count)) + count
					c.execute(NewPHN.insert_phn_query, ('PHN'+str(string_output),'S8+', 'New', str(self.imei.text), str(self.phnnotes.text),str(datetime.date.today()),'NA','NA', 'NA'))
					conn.commit()

				else:
					print ("Form Not Complete")
				
			
			elif self.phntog2.state == 'down':
				
				if self.phntog3.state == 'down':
					c.execute("SELECT Count(IventoryID) FROM Phones")
					num_len = 5
					count = c.fetchone()[0] + 1
					count = str(count)
					string_output = "0"*(num_len-len(count)) + count
					c.execute(NewPHN.insert_phn_query, ('PHN'+str(string_output),'S10', 'Used', str(self.imei.text), str(self.phnnotes.text),str(datetime.date.today()),'NA','NA', 'NA'))
					conn.commit()

				elif self.phntog4.state == 'down':
					c.execute("SELECT Count(IventoryID) FROM Phones")
					num_len = 5
					count = c.fetchone()[0] + 1
					count = str(count)
					string_output = "0"*(num_len-len(count)) + count
					c.execute(NewPHN.insert_phn_query, ('PHN'+str(string_output),'S10', 'New', str(self.imei.text), str(self.phnnotes.text),str(datetime.date.today()),'NA','NA', 'NA'))
					conn.commit()

				else:
					print ("Form Not Complete")
			else:
				print ("Form Not Complete")

class NewKSK(Screen, LeftMenu):
	
	insert_ksk_query = "INSERT INTO Insomniacs(IventoryID, Property, Notes, DateRecieved, DateSentOut, Property) VALUES (?,?,?,?,?)"

	def submitksk(self):
		if self.propnum.text == '':
			print ("Form Not Complete")

		else:
			c.execute("SELECT Count(IventoryID) FROM Insomniacs")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewKSK.insert_ksk_query, ('KSK'+str(string_output), str(self.propnum.text), str(self.ksknotes.text),str(datetime.date.today()),'NA'))
			conn.commit()

class NewCAM(Screen, LeftMenu):

	insert_cam_query = "INSERT INTO Cameras(IventoryID, TypeOfCamera, Notes, DateRecieved, DateSentOut, Property) VALUES (?,?,?,?,?,?)"
	
	def submitcam(self):
		if self.camtog1.state == 'down':
			c.execute("SELECT Count(IventoryID) FROM Cameras")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewCAM.insert_cam_query, ('CAM'+str(string_output), str(self.camtog1.text), str(self.camnotes.text),str(datetime.date.today()),'NA', 'NA'))
			conn.commit()
		elif self.camtog2.state == 'down':
			c.execute("SELECT Count(IventoryID) FROM Cameras")
			num_len = 5
			count = c.fetchone()[0] + 1
			count = str(count)
			string_output = "0"*(num_len-len(count)) + count
			c.execute(NewCAM.insert_cam_query, ('CAM'+str(string_output), str(self.camtog2.text), str(self.camnotes.text),str(datetime.date.today()),'NA', 'NA'))
			conn.commit()
		else:
			print ('Form Not Complete')


class NewSWC(Screen, LeftMenu):

	insert_swc_query = "INSERT INTO Switches(IventoryID, TypeOfSwitch, NumberOfPorts, Notes, DateRecieved, DateSentOut, Property) VALUES (?,?,?,?,?,?,?)"
	
	def submitswc(self):
		if self.swcports.text == '':
			print ('Form Not Complete')
		else:
			if self.swctog1.state == 'down':
				c.execute("SELECT Count(IventoryID) FROM Switches")
				num_len = 5
				count = c.fetchone()[0] + 1
				count = str(count)
				string_output = "0"*(num_len-len(count)) + count
				c.execute(NewSWC.insert_swc_query, ('SWC'+str(string_output), str(self.swctog1.text), str(self.swcports.text), str(self.swcnotes.text), str(datetime.date.today()),'NA', 'NA'))
				conn.commit()

			elif self.swctog2.state == 'down':
				c.execute("SELECT Count(IventoryID) FROM Switches")
				num_len = 5
				count = c.fetchone()[0] + 1
				count = str(count)
				string_output = "0"*(num_len-len(count)) + count
				c.execute(NewSWC.insert_swc_query, ('SWC'+str(string_output), str(self.swctog2.text), str(self.swcports.text), str(self.swcnotes.text), str(datetime.date.today()),'NA', 'NA'))
				conn.commit()

			else:
				print ('Form Not Complete')


class Sendfld(Screen, LeftMenu):
	pass

class SendSWC(Screen, LeftMenu):

	def fillsnswc(self):
		fsnswc = str(self.swcid.text)
		c.execute("SELECT Notes FROM Switches Where IventoryID ='%s'" % (fsnswc))
		result = c.fetchall()
		for row in result:
  			self.sendswcnotes.text = (row[0])

	def sendswc(self):
		datesent = str(datetime.date.today())
		swcprop = str(self.swcprop.text)
		swcid = str(self.swcid.text)
		snswc = str(self.sendswcnotes.text)
		c.execute("UPDATE Switches SET Property =%s, DateSentOut='%s', Notes='%s'  WHERE  IventoryID ='%s'" % (swcprop, datesent, snswc, swcid,))
		conn.commit()

class SendCAM(Screen, LeftMenu):

	def fillsncam(self):
		fsncam = str(self.camid.text)
		c.execute("SELECT Notes FROM Cameras Where IventoryID ='%s'" % (fsncam))
		result = c.fetchall()
		for row in result:
  			self.sendcamnotes.text = (row[0])

	def sendcam(self):
		datesent = str(datetime.date.today())
		camprop = str(self.camprop.text)
		camid = str(self.camid.text)
		sncam = str(self.sendcamnotes.text)
		c.execute("UPDATE Cameras SET Property =%s, DateSentOut='%s', Notes='%s'  WHERE  IventoryID ='%s'" % (camprop, datesent, sncam, camid,))
		conn.commit()

class SendDVR(Screen, LeftMenu):

	def fillsndvr(self):
		fsndvr = str(self.dvrid.text)
		c.execute("SELECT Notes FROM DVRs Where IventoryID ='%s'" % (fsndvr))
		result = c.fetchall()
		for row in result:
  			self.senddvrnotes.text = (row[0])

	def senddvr(self):
		datesent = str(datetime.date.today())
		dvrprop = str(self.dvrprop.text)
		dvrid = str(self.dvrid.text)
		sndvr = str(self.senddvrnotes.text)
		c.execute("UPDATE DVRs SET Property =%s, DateSentOut='%s', Notes='%s'  WHERE  IventoryID ='%s'" % (dvrprop, datesent, sndvr, dvrid,))
		conn.commit()

class SendKSK(Screen, LeftMenu):

	def sendksk(self):
		datesent = str(datetime.date.today())
		swcprop = str(self.swcprop.text)
		swcid = str(self.swcid.text)
		print ("UPDATE Switches SET Property ="+swcprop+", DateSentOut='"+datesent+"'  WHERE  IventoryID ='"+swcid+"'")
		c.execute("UPDATE Switches SET Property =%s, DateSentOut='%s'  WHERE  IventoryID ='%s'" % (swcprop, datesent, swcid,))
		conn.commit()

class SendPHN(Screen, LeftMenu):

	def sendphn(self):
		datesent = str(datetime.date.today())
		swcprop = str(self.swcprop.text)
		swcid = str(self.swcid.text)
		print ("UPDATE Switches SET Property ="+swcprop+", DateSentOut='"+datesent+"'  WHERE  IventoryID ='"+swcid+"'")
		c.execute("UPDATE Switches SET Property =%s, DateSentOut='%s'  WHERE  IventoryID ='%s'" % (swcprop, datesent, swcid,))
		conn.commit()

class SendRTR(Screen, LeftMenu):

	def fillsnrtr(self):
		fsnrtr = str(self.rtrid.text)
		c.execute("SELECT Notes FROM Routers Where IventoryID ='%s'" % (fsnrtr))
		result = c.fetchall()
		for row in result:
  			self.sendrtrnotes.text = (row[0])

	def sendrtr(self):
		datesent = str(datetime.date.today())
		rtrprop = str(self.rtrprop.text)
		rtrid = str(self.rtrid.text)
		snrtr = str(self.sendrtrnotes.text)
		c.execute("UPDATE Routers SET Property =%s, DateSentOut='%s', Notes='%s'  WHERE  IventoryID ='%s'" % (rtrprop, datesent, snrtr, rtrid,))
		conn.commit()
		


class Invstat(Screen, LeftMenu):
	pass

class WindowManager(ScreenManager):
    pass

# Defines the name of the kv file for the project
kv = Builder.load_file("Inventory.kv")

# Defines "sm" Variable
sm = WindowManager(transition=NoTransition())

# Defining Screens
screens = [MainScreen(name="MainMenu"), NewDVR(name="newdvr"), NewRTR(name="newrtr"), NewCAM(name="newcam"), 
			NewKSK(name="newksk"), NewPHN(name="newphn"), NewSWC(name="newswc"), Sendfld(name="sendfld"), 
			Invstat(name="invstat"), SendSWC(name="sendswc"), SendRTR(name="sendrtr"), SendCAM(name="sendcam"),
			SendPHN(name="sendphn"), SendKSK(name="sendksk"), SendDVR(name="senddvr")]
for screen in screens:
    sm.add_widget(screen)

# Setting Main Screen
sm.current = "MainMenu"


#Defines and names the App
class SEinventoryApp(App):
    def build(self):
        self.sm = sm
        return sm


# Check if apps name matches and if so runs app
if __name__ == "__main__":
   SEinventoryApp().run()