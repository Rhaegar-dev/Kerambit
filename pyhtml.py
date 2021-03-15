
class HTML:

    def __init__(self, name, lang):
        self.name = name
        self.lang = lang
        self.html = open(self.name, "w+")

        self.html_open = "<!DOCTYPE html>\n<html>\n"
        self.html_close = "</html>"

        self.hd = ""
        self.bd = ""
         
    def head(self, title, style=None, link=None, script=None):

        title = "\t<title>{}</title>\n".format(title)

        
        self.hd = "<head>\n" + title + "</head>\n"
        
    def body(self, *bd_elements:str):
        bd_open = "<body>\n"
        bd_close = "</body>\n"

        concat = ""
        for elem in bd_elements:
            elem = '  ' + elem 
            concat += elem

        self.bd = bd_open + concat + bd_close

    def button(self, text, autofocus=None, disabled=None, form=None,form_action=None):
        
        text = "<button>{}</button>\n".format(text)
        return text

    def p(self, text):
        text = "<p>{}</p>\n".format(text)
        return text

    def b(self, text):
        text = "<b>{}</b>\n".format(text)
        return text

    def a(self, href, text):
        a_start = "<a "
        a_end = "</a>\n"
        href = 'href="{}">'.format(href)
        text = a_start + href + text + a_end
        return text

    def br(self):
        return "<br>"

    def i(self, text):
        text = "<i>{}</i>\n".format(text)
        return text

    def script(self, text):
        text = "<script>{}</script>\n".format(text)
        return text
         
    def h(self, n, text):
        text = "<h{}>{}</h{}>\n".format(n, text, n)
        return text
    
    def update(self):
        doc = self.html_open + self.hd + self.bd + self.html_close
        self.html.writelines(doc)
    
    
class Table:
    def __init__(self, caption):
        self.table_start = "<table>\n"
        self.table_end = "</table>\n"
        self.caption = "<caption>" + caption + "<caption>\n"
        self.code ='' 

    def head(self, cell_head = []):
        self.tr = ''
        for cell in cell_head:
            self.tr += "<th>" + cell + "</th>\n"
        
        self.tr = "<tr>\n" + self.tr + "</tr>\n"
    
    def data(self, cell_data):
        self.td = ''
        for cell in cell_data:
            self.td += "<td>" + cell + "</td>\n"
        
        self.td = "<tr>\n" + self.td + "</tr>\n"

    
    def concat(self):
        self.code = self.table_start + self.caption + self.tr + self.td + self.table_end
        return self.code
        
global_attrs = {
    "accesskey": "",
    "class": "",
    "id": "",
    "style": "",
    "title": "",
    "tabindex":,
}
    


