# -*- coding: utf-8 -*-
from openerp import models,fields



class Partner(models.Model):
    _inherit="res.partner"

    instructor = fields.Boolean(string="Instructeur")
    session_ids = fields.Many2many(comodel_name="openacademy.session", relation="session_part_rel",
                                   column1="session_id", column2="part_id", string="session")




