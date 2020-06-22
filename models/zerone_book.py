from odoo import api, fields, models, _


class ZeroneBook(models.Model):
    _name = "zerone.book"
    _description = "Zerone Books"

    _inherit = ['image.mixin']

    image_1920 = fields.Image(string="図書写真")
    name = fields.Char(string="図書名称", required=True)
    code = fields.Char(string="図書番号", copy=False, help="図書の管理番号です")
    isbn = fields.Char(string="ISBN", copy=False)
    author = fields.Char(string="作者")
    pages = fields.Integer(string="ページ数")
    publish_date = fields.Date(string="出版时间")
    publisher = fields.Char(string="出版社")
    price = fields.Float(string="定価", digits=(7, 2))
    description = fields.Text(string="概要", help="""本図書の概要説明""")
    binding_type = fields.Selection(
        [("common", "普通"), ("hardcover", "ハードカバー")],
        string="図書形式", index=True, default='common'
    )
    e_link = fields.Html(string="電子版リンク")
    borrowed = fields.Boolean(string="貸出中", default=False)
    date_last_borrowed = fields.Datetime("最後の貸出時刻", index=True, readonly=True)

    shelf_id = fields.Many2one('zerone.shelf', string='書架')
    tags_ids = fields.Many2many("zerone.tags", string="タグ")

    @api.depends('isbn', 'name')
    def name_get(self):
        result = []
        for book in self:
            result.append((book.id, '%s(%s)' % (book.name, book.isbn)))
        return result

    def action_borrow(self):
        self.borrowed = True
        self.date_last_borrowed = fields.Datetime.now()

    def action_return(self):
        self.borrowed = False
        self.date_last_borrowed = None

