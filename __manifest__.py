{
    'name': "zerone_books",
    'summary': """
        图书管理
        """,
    'sequence': 1,
    'description': """
        图书管理：
            图书信息
            图书分类信息
    """,
    'author': "zerone",
    'website':'http://www.google.co.jp',
    'category': 'tools',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        'views\zerone_book.xml',
    ],
    'installable': True,
    'application': True,
}
