def user():
    return dict(form=auth())

def register():
	return dict(form=auth())

@auth.requires_login()
def create():
    form = SQLFORM(db.ads).process(next=URL('index'))
    return dict(form=form)

def show():
    ad = db.ads(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(ad=ad)

def download():
    return response.download(request, db)

def index():
    images = db().select(db.image.ALL, orderby=db.image.title)
    return dict(images=images)

def search():
    return dict(form=FORM(INPUT(_id='keyword',
                                _name='keyword',
                                _onkeyup="ajax('callback', ['keyword'], 'target');")),
                target_div=DIV(_id='target'))

def contactform():
	return dict(form=auth())