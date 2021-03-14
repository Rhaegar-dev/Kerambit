from pyhtml import HTML, Table

doc = HTML("index.html", lang="en") 
doc.head(title="title")

doc.body(
    doc.p("some text"),
    doc.h(3,"h3 text"),
    doc.button('button')

)
doc.write()

