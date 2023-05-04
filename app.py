from flask import Flask, render_template, request
import random

app = Flask(__name__)

my_list = ['Chameleons are a family of lizards.', 
           'Chameleons are well-known for their ability to change color.', 
           'Chameleons have a long sticky tongue that they use to catch insects.', 
           'Chameleons have independently moving eyes that can look in two directions at once.', 
           'Chameleons can move their eyes in all directions without moving their head.', 
           'Chameleons feet are adapted for grasping branches.', 
           'Chameleons have a prehensile tail that they can use to hold onto branches.', 
           'Chameleons are found in warm habitats such as rain forests, deserts, and savannas.', 
           'Some species of Chameleons can change color to blend in with their surroundings, while others change color to regulate their body temperature.', 
           'Most chameleons are arboreal, which means they spend most of their time in trees.', 
           'Chameleons are found primarily in Africa, Madagascar, and parts of Asia and Europe.', 
           'Chameleons have a unique tongue structure that allows them to shoot their tongues out at prey at high speeds.', 
           'Chameleons are cold-blooded reptiles and require a warm environment to regulate their body temperature.', 
           'Female chameleons are usually larger than males, and they lay eggs to reproduce.']

def get_random_element(lst):
    return random.choice(lst)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fact', methods=['POST'])
def get_fact():
    if request.form['submit_button'] == 'Yes':
        random_element = get_random_element(my_list)
        return render_template('get_fact.html', fact=random_element)
    else:
        return render_template('get_fact.html', fact='Text')

@app.route('/continue', methods=['POST'])
def continue_app():
    if request.form['submit_button'] == 'Yes':
        return render_template('index.html')
    else:
        return render_template('continue.html')

if __name__ == '__main__':
    app.run(debug=False)