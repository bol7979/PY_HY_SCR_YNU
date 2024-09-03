from flask import Flask, render_template, request, redirect, send_file
from scr import search_incruit
from scr import search_jobkorea
from scr import search_saramin
from file import save_to_csv

app = Flask(__name__)

page = 1
db = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    keyword = request.args.get("kw")

    if keyword in db:
        jobs = db[keyword]
    else:
        jobs_incruit = search_incruit(keyword, page)
        jobs_jobkorea = search_jobkorea(keyword, page)
        jobs_saramin = search_saramin(keyword, page)
        jobs = jobs_incruit + jobs_jobkorea + jobs_saramin
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=enumerate(jobs), counts=len(jobs))

@app.route("/export")
def export():
    keyword = request.args.get("kw")

    if keyword == "":
        return redirect("/")
    
    if keyword not in db:
        return redirect("/")
    
    save_to_csv(db[keyword])

    return send_file("./to_save.csv", as_attachment=True)

if __name__ == '__main__':
    app.run()