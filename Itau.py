#!/usr/bin/python
# -*- encoding: utf-8 -*-

from Bank import *

class Itau(Bank):
	pass

account = Itau(name="Miguel",account_number='00008', cpf='31212345')
account.CreateAccount()