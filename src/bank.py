#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Bank:
	costumer_name = ''
	costumer_cpf = ''
	costumer_number_account = ''

	# fake base
	BaseCostumers = ([('kaio','123123','0004','100000.00'),('bruna','321123','0005','9000.00')])

	def __init__(self, name=None, cpf=None, account_number=None):
		if (name != None and cpf != None and account_number != None):
			self.costumer_cpf = cpf
			self.costumer_name = name
			self.costumer_number_account = account_number


	def CreateAccount(self):
		Validate = self.ValidateData()
		if Validate ==True:
			#"You cannot create this user because it already exists in our database."
			return False
		elif Validate == False:
			datas = (self.costumer_name, self.costumer_cpf, self.costumer_number_account)
			self.BaseCostumers.append(datas)
			print(self.BaseCostumers)
		else:
			#"Set the values of the properties in the costructor"
			return None


	def ValidateData(self):
		if (not self.costumer_cpf):
			return None

		for Costumer in self.BaseCostumers:
			if Costumer[0] == self.costumer_cpf:
				return True

		return False


	def QueryValueAccount(self, cpf_number=None):
		if (not cpf_number):
			return False

		for Costumer in self.BaseCostumers:
			if Costumer[1] == cpf_number:
				return Costumer[3]

		return False




