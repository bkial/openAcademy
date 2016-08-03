# -*- coding: utf-8 -*-
from openerp import models,fields


class Course(models.Model):
    _name="openacademy.course"

    name = fields.Char(required=True,string="Titre")
    titre = fields.Char(string="tit")
    description = fields.Text(string="Description")
    resp_id = fields.Many2one(comodel_name="res.users",string="Responsable")




