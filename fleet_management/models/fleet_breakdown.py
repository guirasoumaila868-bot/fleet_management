# -*- coding: utf-8 -*-
from odoo import models, fields


class SmartFleetBreakdown(models.Model):
    _name = 'smart.fleet.breakdown'
    _description = 'Panne / Réparation'
    _inherit = ['mail.thread']
    _order = 'date desc'

    name = fields.Char(string="Objet", required=True)
    vehicle_id = fields.Many2one('smart.fleet.vehicle', string="Véhicule", required=True, ondelete='cascade')
    date = fields.Date(string="Date de la panne", default=fields.Date.context_today)
    description = fields.Text(string="Description")
    gravite = fields.Selection([
        ('legere', 'Légère'),
        ('moyenne', 'Moyenne'),
        ('grave', 'Grave / immobilisation'),
    ], default='moyenne', string="Gravité")
    cout_reparation = fields.Monetary(string="Coût de réparation")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    state = fields.Selection([
        ('signalee', 'Signalée'),
        ('en_reparation', 'En réparation'),
        ('resolue', 'Résolue'),
    ], default='signalee', tracking=True, string="Statut")
