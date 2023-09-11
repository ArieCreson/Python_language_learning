# Python_language_learning
This program is meant to be used through your local shell. it's purpose is to serve as a language learning aid, this is done by utilising the dictionary 
data type and saving your target language words as keys and their meaning as keys.
some features use the alias : dict="cd && cd program_location && python3 dictionary.py" (ie, external use of the program for better accessabilty)
by intiating the program through the shell you will be prompted with the list of available functions.
in order to use the advanced AI features you need to set up an API key from open ai, do this by replace "your api key" in "ai.sh" to your API key (should start with sk).
the script "ai.sh" uses chatgpt in order answer any given prompt.


some examples of usage (by initiating the program you would get the following prompt):

1. "add" & "get":
Enter your choice: add guten morgen
Enter translation: good morning
The word: "guten morgen" has been added!
Enter your choice: get guten morgen
Translation: good morning

what ever comes after add goes to the key of a new entry in the diary.
the answer to the translation goes to the value of that key. 
by using get on a key in the diary we can extract the value.

2. another example of "add": 
Enter your choice: add Hallo:hello
The word: "Hallo" has been added!
Enter your choice: get Hallo 
Translation: hello
Enter your choice: 

in this example, "Hallo" is saved with the meaning hello (to a local file called words.json).
this alternative use of add has two arguments:
the first one is between the first space of add until the ":" and goes to the key of the variable.
the second argument is whatever comes after the ":" and goes to the value of that key. 

3."add" and "get" but from the shell enviorment:

after you have set up the appropriate aliases you can also add and get words outside of the program, like so:

arie@arie-H97-HD3:~$ dict add github:website
The word: "github" has been added!
arie@arie-H97-HD3:~/Desktop/Scripts/Language-Dictionary-$ dict get github
Translation: website

As simple as that. the word is saved in "words.json" where dictionary.py is at.

4. after you set up your API key you can finally use "ai" and "translate" example:


dict ai can you help me understand quantom physics?
Of course! I can provide a basic overview of quantum physics. Quantum physics, 
also known as quantum mechanics, is a branch of physics that deals with the 
behavior of particles at the smallest scales, such as atoms and subatomic 
particles. It provides a framework for understanding phenomena that classical 
physics cannot explain.

Here are some key concepts in quantum physics:

1. Wave-particle duality: According to quantum physics, particles such as 
electrons and photons can exist as both particles and waves, depending on how 
they are observed or measured.

2. Superposition: Quantum systems can exist in multiple states simultaneously. 
This means that until observed or measured, particles can exist in a state of 
superposition, where they possess all possible values of a property at the 
same time.

3. Uncertainty principle: The uncertainty principle, discovered by Werner 
Heisenberg, states that it is impossible to simultaneously know both the 
position and momentum of a particle with absolute precision. The more 
accurately you know one, the less accurately you can know the other.

4. Quantum entanglement: Entanglement occurs when two or more particles become 
correlated, so that the state of one particle is instantly linked to the state 
of the others, regardless of the distance between them. This phenomenon has 
been experimentally verified.

5. Quantum tunneling: Quantum tunneling refers to the phenomenon where 
particles can pass through energy barriers even when they do not possess 
enough energy to do so according to classical physics.

These concepts are just a starting point, and quantum physics involves many 
other fascinating principles and phenomena. It is a complex field that 
requires mathematical formalism to fully understand and describe physical 
phenomena accurately.

Remember, this is only a brief introduction, and delving into quantum physics 
can be a deeply intricate endeavor.





another example: 
dict translate stueckchen
"Stückchen" ist ein Substantiv auf Deutsch. Es bedeutet "ein kleines Teil" oder 
"eine kleine Menge" von etwas. Es wird oft verwendet, um kleine Portionen von 
Lebensmitteln oder anderen Gegenständen zu beschreiben.



this output is clear once you understand the python script, there is a matching place where this command (translate) takes an input (in this example stueckchen) and attaches another string to it
and then shooves it into ai.sh which gives back the output.





