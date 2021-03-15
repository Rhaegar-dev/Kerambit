from pyhtml import HTML, Table

doc = HTML("index.html", lang="en") 
doc.head(title="title")

doc.body(
    doc.p("some text"),
    doc.a(href="#p1", text="Summer"),
    doc.button('button')

)
doc.update()

