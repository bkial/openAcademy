# -*- coding: utf-8 -*-
from openerp import models,fields


class Session(models.Model):
    _name="openacademy.session"

    name = fields.Char(string="Nom",required=True)
    date_debut = fields.Date(string="Date debut")
    duree = fields.Integer(string="Duree")
    nbr_place = fields.Integer(string="Nombre de place")
    course_id = fields.Many2one(comodel_name="openacademy.course", string="Course", ondelete="set null")
    instructeur_id=fields.Many2one(comodel_name="res.partner", string="Instructeur", ondelete="set null")
    participants = fields.Many2many(comodel_name="res.partner", relation="session_part_rel", column1="session_id",
                                    column2="part_id", string="Particpants")




