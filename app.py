from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    banner_img = url_for('static', filename='images/banner.jpg')
    articles = [
        {
            'heading': 'My first post',
            'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, facilis? At odit repudiandae facere eligendi, officiis dolore tempora, possimus, ipsam beatae dicta mollitia dolor alias veritatis voluptates. Aspernatur, commodi deserunt. Nobis, minima! Quis, illum consectetur. Quasi eaque aspernatur quos corrupti numquam explicabo, adipisci atque, cumque quo, ut distinctio praesentium deserunt? Saepe explicabo facere molestias hic reprehenderit numquam, labore veritatis totam?',
            'link': '/'
        },
        {
            'heading': 'Second one',
            'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, facilis? At odit repudiandae facere eligendi, officiis dolore tempora, possimus, ipsam beatae dicta mollitia dolor alias veritatis voluptates. Aspernatur, commodi deserunt. Nobis, minima! Quis, illum consectetur. Quasi eaque aspernatur quos corrupti numquam explicabo, adipisci atque, cumque quo, ut distinctio praesentium deserunt? Saepe explicabo facere molestias hic reprehenderit numquam, labore veritatis totam?',
            'link': '/'
        },
        {
            'heading': 'Third one',
            'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, facilis? At odit repudiandae facere eligendi, officiis dolore tempora, possimus, ipsam beatae dicta mollitia dolor alias veritatis voluptates. Aspernatur, commodi deserunt. Nobis, minima! Quis, illum consectetur. Quasi eaque aspernatur quos corrupti numquam explicabo, adipisci atque, cumque quo, ut distinctio praesentium deserunt? Saepe explicabo facere molestias hic reprehenderit numquam, labore veritatis totam?',
            'link': '/'
        },
        {
            'heading': 'Fourth',
            'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, facilis? At odit repudiandae facere eligendi, officiis dolore tempora, possimus, ipsam beatae dicta mollitia dolor alias veritatis voluptates. Aspernatur, commodi deserunt. Nobis, minima! Quis, illum consectetur. Quasi eaque aspernatur quos corrupti numquam explicabo, adipisci atque, cumque quo, ut distinctio praesentium deserunt? Saepe explicabo facere molestias hic reprehenderit numquam, labore veritatis totam?',
            'link': '/'
        },
    ]
    return render_template("index.html", banner_img=banner_img, articles=articles, heading="Blog")

@app.route("/about")
@app.route("/archive")
def about():
    banner_img = url_for('static', filename="images/construction.jpg")
    return render_template("base.html", banner_img=banner_img, banner_full=True)

@app.errorhandler(404)
def page_not_found(e):
    banner_img = url_for('static', filename="images/404.jpg")
    return render_template("404.html", banner_img=banner_img, banner_full=True), 404

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)