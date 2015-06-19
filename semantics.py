import web
render = web.template.render('templates/',base='layout')
from word_handler import word_handler
handler=word_handler()

class semantics_index:
    def GET(self):
        dates=[2005,2006,2007,2008]
        return render.semantics_index(dates=dates)

class semantics_show:
    def GET(self):
        return 'Semantics show'
    def POST(self):
        params = web.input()
        word=params['word']
        dates=[]
        for p in params:
            if params[p]=='on':
                dates.append(p)
        words=handler.get_closest_words(dates,word)
        words=zip(dates,words)
        dates=[2005,2006,2007,2008]
        return render.semantics_index(dates=dates,words=words)
