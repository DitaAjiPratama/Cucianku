import  mysql.connector     as      mariadb
from    mako.template       import  Template
from    config              import  database

class select_sample:

    def __init__(self):
        pass
    #end def

    def html(self, params):

        html_page = params['html']

        cursor = database.main_db.cursor()
        cursor.execute("SELECT username FROM auth")
        listing = list(cursor)

        return Template(html_page).render(
            cursor=listing
        )
    # end def

#end class
