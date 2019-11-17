#-*- coding: utf-8 -*-
from odoo import models,fields,api
class MiModulo(models.Model):
	_name = 'mi.modulo'
	_description = 'Mi Modulo :D'
	name = fields.Char('Description',required=True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?',default=True)
	@api.one 
	def do_toggle_done(self):
		for task in self:
			task.is_done = not task.is_done
		return True
	@api.multi
	def do_clear_done(self):
		dones = self.search([('is_done','=',True)])
		dones.write({'active':False})
		return True