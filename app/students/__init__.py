

from flask.blueprints import  Blueprint  # collect urls of the application

student_blueprint= Blueprint('students',__name__, url_prefix='/students' )

from app.students import views