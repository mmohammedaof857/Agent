from flask import Blueprint , request , jsonify

youtube_bp = Blueprint(
  " youtube ",
  __name__
  )

@youtube_bp.route(
   "/play" ,
  methods = ["post"]

 )
 def play ():

  data = request.get_json(
      silent = True
      )or {}

   command = data.get(
     "command",
     ""
   ).strip()

if not command :

  return jsonify({
    "success":"false",
    "message":"There is no song name , mentioned " 
})400
