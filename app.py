from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    send_file
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

from database.models import (
    db,
    User,
    AnalysisReport
)

from modules.hashing_lab import HashingLab
from modules.strength_analyzer import StrengthAnalyzer
from modules.policy_analyzer import PolicyAnalyzer
from modules.risk_engine import RiskEngine
from modules.visualization import Visualization
from modules.reporting import ReportGenerator

import bcrypt
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "password-security-project"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"sqlite:///{os.path.join(BASE_DIR,'database','db.sqlite')}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing = User.query.filter_by(
            email=email
        ).first()

        if existing:
            flash("Email already exists")
            return redirect(url_for("register"))

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        ).decode()

        user = User(
            username=username,
            email=email,
            password_hash=hashed
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful")

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and bcrypt.checkpw(
            password.encode(),
            user.password_hash.encode()
        ):
            login_user(user)

            return redirect(
                url_for("dashboard")
            )

        flash("Invalid credentials")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():

    total_reports = AnalysisReport.query.filter_by(
        user_id=current_user.id
    ).count()

    return render_template(
        "dashboard.html",
        total_reports=total_reports
    )


@app.route("/strength", methods=["GET", "POST"])
@login_required
def strength():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        result = StrengthAnalyzer.analyze(
            password
        )

        risk = RiskEngine.calculate(
            result["score"]
        )

        report = AnalysisReport(
            password_length=len(password),
            strength_score=result["score"],
            risk_level=risk,
            hash_type="N/A",
            user_id=current_user.id
        )

        db.session.add(report)
        db.session.commit()

        Visualization.create_score_chart(
            result["score"]
        )

    return render_template(
        "strength.html",
        result=result
    )


@app.route("/policy", methods=["GET", "POST"])
@login_required
def policy():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        result = PolicyAnalyzer.evaluate(
            password
        )

    return render_template(
        "policy.html",
        result=result
    )


@app.route("/hashing", methods=["GET", "POST"])
@login_required
def hashing():

    hashes = None

    if request.method == "POST":

        password = request.form["password"]

        hashes = {
            "MD5":
            HashingLab.md5_hash(password),

            "SHA256":
            HashingLab.sha256_hash(password),

            "SHA512":
            HashingLab.sha512_hash(password),

            "BCRYPT":
            HashingLab.bcrypt_hash(password),

            "ARGON2":
            HashingLab.argon2_hash(password)
        }

    return render_template(
        "hashing_lab.html",
        hashes=hashes
    )


@app.route("/analytics")
@login_required
def analytics():

    reports = AnalysisReport.query.filter_by(
        user_id=current_user.id
    ).all()

    scores = [
        r.strength_score
        for r in reports
    ]

    avg_score = 0

    if scores:
        avg_score = round(
            sum(scores) / len(scores),
            2
        )

    return render_template(
        "analytics.html",
        reports=reports,
        avg_score=avg_score
    )


@app.route("/reports")
@login_required
def reports():

    reports = AnalysisReport.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "reports.html",
        reports=reports
    )


@app.route("/download_report/<int:score>")
@login_required
def download_report(score):

    reports_dir = os.path.join(
        BASE_DIR,
        "reports"
    )

    if os.path.exists(reports_dir) and not os.path.isdir(reports_dir):
        os.remove(reports_dir)

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    filename = os.path.join(
        reports_dir,
        f"report_{current_user.id}.pdf"
    )


    ReportGenerator.create_report(
        username=current_user.username,
        score=score,
        level="Generated",
        risk="Calculated",
        filename=filename
    )

    return send_file(
        filename,
        as_attachment=True,
        download_name=f"Security_Report_{current_user.id}.pdf",
        mimetype="application/pdf"
    )
if __name__ == "__main__":
    app.run(
        debug=True
    )