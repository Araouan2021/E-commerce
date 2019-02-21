def user():
    return dict(form=auth())

def register():
    return dict(form=auth())

@auth.requires_login()
def create():
    form = SQLFORM(db.ads).process(next=URL('index'))
    return dict(form=form)

def show():
    ads = db.ads(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(ads=ads)

def download():
    return response.download(request, db)

def index():
    ads = db().select(db.ads.ALL, orderby=db.ads.title)
    return dict(ads=ads)

def search():
    return dict(form=FORM(INPUT(_id='keyword',
                                _name='keyword',
                                _onkeyup="ajax('callback', ['keyword'], 'target');")),
                target_div=DIV(_id='target'))

def contact():
    return dict(form=auth())

@auth.requires_login()
def showseller():
    ads = db(db.ads.created_by == auth.user).select(orderby=db.ads.title)
    return dict(ads=ads)

@auth.requires_login()
def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.ads.id == submitted_id).select():
        db(db.ads.id == submitted_id).delete()
        return 'Ads Deleted Successfully'

    else:
        return 'No Ad With the ID found'
 
def showbuyer():
    ads = db(db.ads.created_by == auth.user).select(orderby=db.ads.title)
    return dict(ads=ads)

def callback():
    query = db.ads.title.contains(request.vars.keyword)
    pages = db(query).select(orderby=db.ads.title)
    links = [A(ads.title, _href=URL('show', args=ads.id)) for a in ads]
    return UL(*links)



    
