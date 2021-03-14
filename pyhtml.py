class HTML:

    def __init__(self, name, lang):
        self.name = name
        self.lang = lang
        self.html = open(self.name, "w+")

        self.html_open = "<html>\n"
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
            concat += elem

        self.bd = bd_open + concat + bd_close


    def write(self):
        doc = self.html_open + self.hd + self.bd + self.html_close
        self.html.writelines(doc)

    def p(self, text):
        text = "\t<p>{}</p>\n".format(text)
        return text
         
    def h(self, n, text):
        text = "\t<h{}>{}</h{}>\n".format(n, text, n)
        return text


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
        

    


