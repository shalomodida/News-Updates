from flask import  render_template,redirect,url_for,request
from . import main
from ..models import Sources,Articles
from ..request import get_sources, get_articles

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general_categories = get_sources('general')
    title = 'World News Highlights'
    return render_template('index.html',title = title, general = general_categories)

@main.route('/newsarticle/<id>')
def newsarticle(id):
    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(id)
    title = f'Welcome to {id} | Latest News Headlines'
    return render_template('newsarticle.html',title = title,articles = articles)