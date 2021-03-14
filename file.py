from pyhtml import HTML, Table

doc = HTML("base.html", lang="en") 
doc.head(title="title")

doc.body(
    doc.p("some text"),
    doc.h(3,"h3 text"),
    doc.h(5, "h5 text")

)
doc.write()

