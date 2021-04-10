import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):

  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]
  return current_questions



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


  @app.route('/categories', methods=['GET'])
  def retrieve_categories():
    selection = Category.query.order_by(Category.id).all()
    current_categories = [category.format() for category in selection]

    return jsonify({
      'success': True,
      'categories': current_categories
    })





  @app.route('/questions', methods=['GET'])
  def retrieve_questions():
    try:

      selection = Question.query.all()

      categories = {}
      for category in Category.query.all():
        categories[category.id] = category.type

      pag_questions = paginate_questions(request, selection)



      return jsonify({
        'success': True,
        'questions': pag_questions,
        'total_questions': len(selection),
        'categories': categories,
        'current_category': None

        })
    except:
      abort(404)


  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def questions_by_category(category_id):
    try:

      selection = Question.query.filter(Question.category == category_id).all()
      if selection is None:
        abort(404)


      current_questions = paginate_questions(request, selection)
      current_category = Category.query.filter(Category.id == category_id).one_or_none()


      categories = [category.format() for category in Category.query.all()]

      if len(current_questions) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'current_category': current_category.type,
        'categories': categories
        })
    except:
      abort(404)


  '''


  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      if question is None:
        abort(404)

      question.delete()
      return jsonify({
        'success': True,
        'deleted': question_id
      })

    except:
      abort(422)


  @app.route('/questions', methods=['POST'])
  def post_question():
    try:
      body = request.get_json()

      new_question = body.get('question', None)
      new_answer = body.get('answer', None)
      new_difficulty = body.get('difficulty', None)
      new_category = body.get('category', None)
      search = body.get('searchTerm', None)

      if search is not None:
        selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search)))
        current_questions = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(selection.all()),
          'current_category': None

        })


      else:
        question = Question(question=new_question, answer=new_answer,
                              difficulty=new_difficulty, category=new_category)
        question.insert()

        return jsonify({
            'success': True,
            'created': question.id
        })
    except:
      abort(422)









  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    