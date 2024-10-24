# © 2010-2013 OpenERP s.a. (<http://openerp.com>).
# © 2014 initOS GmbH & Co. KG (<http://www.initos.com>).
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Overview Dashboard (Tiles)",
    "summary": "Add Overview Dashboards with Tiles",
    "version": "12.0.2.0.0",
    "depends": ["web", "board", "mail", "web_widget_color"],
    "author": "initOS GmbH & Co. KG, "
    "GRAP, "
    "Iván Todorovich <ivan.todorovich@gmail.com>, "
    "Odoo Community Association (OCA)",
    "maintainers": ["legalsylvain"],
    "website": "https://github.com/OCA/web",
    "category": "web",
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "views/templates.xml",
        "views/menu.xml",
        "views/tile_tile.xml",
        "views/tile_category.xml",
    ],
    "demo": [
        "demo/tile_category.xml",
        "demo/tile_tile.xml",
    ],
}
