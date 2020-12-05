from flask import Flask, render_template, request

app = Flask(__name__)

# function to determine the story, based on the inputed story type.
def get_story(story, username, protagonist, secondary, noun1, noun2, adjective1, adjective2, adjective3, adjective4, adjective5, place, emotion1, emotion2, emotion3, body_part1, body_part2, adverb1, adverb2, verb1, verb2, verb_past, objects): 
  g_story = ""
  if story == "Spooky": #When user selects 'A Spooky Story'
    g_story = f' It was a {adjective1} night. {protagonist} was a {adjective2} {noun1}. {protagonist} was waiting for {secondary}, a {adjective3} {noun2}. Suddenly something grabbed {protagonist} by the {body_part1}. {protagonist} felt very {emotion1} until {protagonist} turned around and realized it was {secondary}. They headed to the haunted {place}, they were going to {verb1} the {adjective4} ghost. When they had reached the {place}, {secondary} stopped and said “Wait, I’m feeling too {emotion2}”. {protagonist} grabbed {secondary} by the {body_part2} and started pulling. “There’s no reason to  feel {emotion2}” said {protagonist}. Right after {protagonist} had finished talking, they heard a {adjective5} noise behind them. They turned {adverb1}, it was the {adjective4} ghost. {protagonist} and {secondary} felt so {emotion3} they started to {verb2} {adverb2}. The ghost {verb_past} and that was it, {protagonist} and {secondary} ran away from the haunted {place} and never came back, even if they had left their {objects} behind.'

  elif story == "Christmas": #When user selects 'A Christmas Story'
    g_story = f" It was a {adjective1} Christmas eve. {protagonist} was restless while {secondary} was soundly asleep. {protagonist} had asked Santa for a {adjective2} {noun1} and couldn’t wait to open his present. Suddenly {protagonist} heard a noise downstairs. {protagonist} jumped off bed. As {protagonist} was walking through the pitch black hallway something grabbed {protagonist} by the {body_part1}. {protagonist} felt very {emotion1} until {protagonist} turned around and realized it was {secondary}. They headed downstairs, they were going to {verb1} Santa. They saw a {adjective3} silhouette  next to the christmas tree, puting things out of his bag {adverb1}. They jumped over Santa {adverb2}, grabbed him by the {body_part2} and wrestled over the floor. 'You should feel {emotion2}, you {adjective4} children' said Santa. 'I was going to give you the gifts you asked for, but now you’re only getting a {adjective5} {noun2}.' The children tried to {verb1}, they felt so {emotion3} but Santa just {verb_past} 'Now I need to go {verb2} at the {place}'. Santa disappeared so quickly he forgot his {objects}. " 
   
  elif story == "Love":  #When user selects 'A Love Story'
    g_story = f''
  
  return g_story
  
  
@app.route('/')
def home():
  return render_template("home.html")

@app.route('/form')
def form():
  return render_template("form.html")
  
@app.route('/story', methods=["POST"])
def story():
  story = request.form['story']
  username = request.form['username']
  protagonist = request.form['protagonist']
  secondary = request.form['secondary']
  noun1 = request.form['noun1']
  noun2 = request.form['noun2']
  adjective1 = request.form['adjective1']
  adjective2 = request.form['adjective2']
  adjective3 = request.form['adjective3']
  adjective4 = request.form['adjective4']
  adjective5 = request.form['adjective5']
  emotion1 = request.form['emotion1']
  emotion2 = request.form['emotion2']
  emotion3 = request.form['emotion3']
  place = request.form['place']
  body_part1 = request.form['body_part1']
  body_part2 = request.form['body_part2']
  adverb1 = request.form['adverb1']
  adverb2 = request.form['adverb2']
  verb1 = request.form['verb1']
  verb2 = request.form['verb2']
  verb_past = request.form['verb_past']
  objects = request.form['objects']

  g_story = get_story(story, username, protagonist, secondary, noun1, noun2, adjective1, adjective2, adjective3, adjective4, adjective5, place, emotion1, emotion2, emotion3, body_part1, body_part2, adverb1, adverb2, verb1, verb2, verb_past, objects)

  return render_template("story.html", story=story, username=username, protagonist=protagonist, secondary=secondary, noun1=noun1, noun2=noun2, adjective1=adjective1, adjective2=adjective2, adjective3=adjective3, adjective4=adjective4, adjective5=adjective5, place=place, emotion1=emotion1, emotion2=emotion2, emotion3=emotion3, body_part1=body_part1, body_part2=body_part2, adverb1=adverb1, adverb2=adverb2, verb1=verb1, verb2=verb2, verb_past=verb_past, objects=objects, g_story=g_story)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)