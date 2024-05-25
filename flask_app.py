from flask import Flask, url_for, current_app


app = Flask(__name__)


@app.route("/")
def hello_world():
    index_page_html = """
    <style>
        /* Apply padding to all paragraphs */
        p {
            padding: 10px; /* top, right, bottom, left */
            max-width: 400px; /* Set maximum width */
        }
        h1 {
            padding: 10px; /* top, right, bottom, left */
            max-width: 600px; /* Set maximum width */
        }
        h2 {
            padding: 10px; /* top, right, bottom, left */
            padding-top: 30px; /* Only top padding */
            max-width: 600px; /* Set maximum width */
        }

        ul {
            list-style-type: none; /* Remove bullets */
        }


        /* Apply padding to a specific element with class "box" */
        .box {
            padding: 30px; /* top, right, bottom, left */
        }

        /* Apply different padding to an element with id "header" */
        #header {
            padding-top: 10px; /* 10 pixels of padding on the top */
            padding-bottom: 20px; /* 20 pixels of padding on the bottom */
            padding-left: 15px; /* 15 pixels of padding on the left */
            padding-right: 15px; /* 15 pixels of padding on the right */
        }
    </style>
    <body>
        <h2>Learning Physics Differently</h2>
        <ul>
            <li><a href="/history_of_resistance">Do Physics, Learn History</a></li>
        </ul>
        <h2>Discussions on Classic Textbook Problems</h2>
        <ul>
            <li><a href="/ashcroft_and_mermin">Solid State Physics, Ashcroft and Mermin</a></li>
        </ul>
        <h2>Ideas in Condensed Matter Theory</h2>
        <ul>
            <li><a href="/history_of_resistance">The Mathematics of Lattices </a></li>
            <li><a href="/history_of_resistance">Surfaces of Minimal Energy, Fermi Surfaces</a></li>
        </ul>

        </ul>
    </body>
    """
    return index_page_html


@app.route("/history_of_resistance")
def history_of_metallic_resistance():
    return current_app.send_static_file('do_physics_but_learn_history.html')


@app.route("/ashcroft_and_mermin")
def ashcroft_mermin():
    with open('ashcroft_and_mermin.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

