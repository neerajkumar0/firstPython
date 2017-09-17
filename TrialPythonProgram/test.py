#!/usr/bin/python

print ("Hello, Python!");

class familyMember:
	'Details of family member'

	def __init__(self,name,age,sex,memberType):
		self.name = name
		self.age = age
		self.sex = sex
		self.memberType = memberType

	def DisplayMember(self):
		print ("\nName : ", self.name, " Age : ", self.age, " Sex : ", self.sex , "\n\n");

class family:
	'details of a family'
	familyCount =0

	def __init__(self, familyName, noOfMember):
		self.familyName = familyName
		self.noOfMember = noOfMember
		self.familyMembers = []
		count =0
		while(count < self.noOfMember):
			count += 1
			name = input("\nEnter Name:")
			age = input("\n age:")
			sex = input("\n sex:")
			memberType = input("\n member Type:")
			member = familyMember(name,age,sex,memberType)
			self.familyMembers.append(member)
		family.familyCount += 1

	def DisplayFamily(self):
		print ("\n This is the ", self.familyName, " family");
		print ("\n the family members are:");
		count =0
		father = False
		mother = False
		while(count < self.noOfMember):
			if(father ==False and self.familyMembers[count].memberType == 'F'):
				print ("\nFather :")
				self.familyMembers[count].DisplayMember()
				father = True
				count =0
			if(father == True and mother == False and self.familyMembers[count].memberType == 'M'):
				print ("\nMother :")
				self.familyMembers[count].DisplayMember()
				mother = True
				count =0
			if(mother == True and self.familyMembers[count].memberType == 'C'):
				print ("\nChild :")
				self.familyMembers[count].DisplayMember()
			count += 1


family1 = family("Kumar ", 4)
family1.DisplayFamily()


input("\n\nPress the enter key to exit.");
