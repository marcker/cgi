#!/usr/bin/env python
# encoding: utf-8

import cgi

def urlParameter():
    form = cgi.FieldStorage()
    
    if form.getvalue('username') != None:
        return str(form.getvalue('username') + '.')
    else:
        return 'Sem nome.'

def basicHtml(title, content):
    print "Content-type: text/html\n"
    print """
        <!doctype html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
            </head>
            <body>
                <div class="result">
                    <h1>Olá, %s</h1>
                </div>
            </body>
        </html>
    """ % (title, content)

basicHtml('Recuperar do formulário', urlParameter())