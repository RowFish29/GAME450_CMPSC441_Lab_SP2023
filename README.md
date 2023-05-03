# Final Report
## CMPSC 441 and GAME 450

----- Abstract -----

As Legolas travels from city to city, he faces not only dangerous bandits but also the challenge of limited resources. With little money to his name, he must be resourceful and frugal, living off the land and the occasional kindness of strangers. However, he quickly learns that even his meager possessions are not safe from the bandits who prey on unsuspecting travelers. He must use his wits and fighting skills to fend off these thieves and protect his hard-earned belongings. Despite the challenges, Legolas remains undaunted, determined to continue his journey, and fulfill his quest.

The paragraph above is a ChatGPT generated story that summarizes the story behind the final project for this course, AI, and Advanced Game Programming. When developing this project, various AI concepts and techniques were learned and scripted. AI was used to solve various difficult tasks that would make up this project. Along with AI, many algorithms were created to solve other tasks such as determining valid routes between cities, whether our warrior Legolas makes it to his destination based on his health and currency, and what skills he should use to defeat bandits along the way. 

This report will go over the key algorithms and AI used to program this project. This will cover the description of the problems that each AI method solves, which will contain the inputs and outputs of each algorithm as well as an overall description of it. 

----- List of AI Components in the Project -----
1.  AI Player Combat
2.  Unconnected Start and End City
3.  Path Traveling 
4.  AI Journaling with Open AI

----- Problems Solved-----
1.   AI Player Combat Class

The AI Combat Player is a cutting-edge artificial intelligence system designed to simulate a medieval combat experience. Unlike traditional games that use the rock-paper-scissors format, the AI Combat Player utilizes a unique system based on three different types of attacks: sword, fire, and arrow.

A sword attack is a quick and precise strike that can inflict serious damage if executed correctly. It is particularly effective against opponents who rely heavily on defensive maneuvers or who are caught off guard.

The fire attack is a powerful and destructive assault that can engulf opponents in flames, causing them to suffer damage over time. It is particularly effective against opponents who are not well-equipped to deal with fire-based attacks, such as those wearing heavy armor.

The arrow attack is a ranged attack that allows the AI Combat Player to strike opponents from a distance. It is particularly effective against opponents who are unable to close the distance quickly or who are caught in the open.

The AI Combat Player can analyze the tactics and movements of its opponents, using its weapon selecting strategy function. This function takes in the opponent’s last choice in weapon and bases its selected weapon on the opponent’s previous weapon choice. This is done by thinking of the weapon selections as you would for rock paper scissors, instead though: Arrow beats Sword, Fire beats Arrow, and Sword beats Fire. Depending on which was the opponent’s last selection, the AI player will choose the combination that will defeat it. 

2.  Unconnected Start and End City
One major, yet simple problem, is when 10 random routes are selected to be used during a run of project. Sometimes cities do not have routes leading to them, which is fine under the circumstances that this city is neither the end city, the way the game ends, or the starting city, the way the game begins. If the end city does not have a route, then the game cannot end, and will run forever until the program is ended. If the start city does not have a route, then the game cannot be played further than the map being initialized. Neither of these circumstances are well for this project, and sadly not the only way to break the game, as there needs to be a complete path from the start city to the end city. 

This algorithm only solves the end points not being routed in the map. The algorithm developed takes in the 10 routes that were randomly selected to be a part of the map. This algorithm will result in no routes being added, a route to the end city added, a route to the start city added, or both the end and start city being added. This algorithm is intended to lessen the occurrences of an unplayable map, where there could potentially be no start or end. 

3.  Path Traveling 
Another major component to the game is ensuring that the AI player follows along with the created routes, rather than travel between two unconnected cities. The algorithm for this took in all the valid paths between cities, which would be around 10 without the introduction to the algorithm mentioned above. The algorithm will then output the next destination city for the ai player to travel to. 

This algorithm works by checking to see what cities are connected to the current city that the player is located at. Whether it is in the first or second index of the routes. It then stores the available paths within an array. Afterwards, the length of the array, minus 1, is taken and used to randomly generate an index for the route and destination city that the player will travel to. 

As an extra component of the algorithm, that prevents repetitive actions, the player cannot choose to go back to the city they just visited unless there are no other routes available. While running the algorithm repeatedly, it more frequently than not chose to travel back to the same city, which slowed gameplay down incredibly. 

4.  AI Journaling with Open AI
As a piece to our final project, we had to integrate and use another AI component, and it was suggested that it be used for text generation based on a prompt. For this part of the project, I chose to use Open AI, which requires a key to use (which will be provided as a comment on the canvas submission). This AI algorithm intakes a string prompt and generates a text output based on the prompt. I used this algorithm after each battle between the player and the computer/bandit. The prompt varies on if the player won, lost, or ended up in a draw with the computer. There is a Journal.txt file under the lab14_final folder that displays the date and time the program was run, then the various text generations based on battle outputs. This file only gets appended to, so each run of the program can be seen, split by the date and time stamp. 


----- Appendix-----
1.	ChatGPT Abstract
Prompt: write 100 words about the warrior Legolas traveling city to city with limited money, and must fend off bandits from stealing it

Response: As Legolas travels from city to city, he faces not only dangerous bandits but also the challenge of limited resources. With little money to his name, he must be resourceful and frugal, living off the land and the occasional kindness of strangers. However, he quickly learns that even his meager possessions are not safe from the bandits who prey on unsuspecting travelers. He must use his wits and fighting skills to fend off these thieves and protect his hard-earned belongings. Despite the challenges, Legolas remains undaunted, determined to continue his journey, and fulfill his quest.

2.	ChatGPT AI Player Combat
Prompt: write a description for an AI Combat Player that uses 'sword, fire, arrow' instead of 'rock, paper, scissors'

Response: The AI Combat Player is a cutting-edge artificial intelligence system designed to simulate a medieval combat experience. Unlike traditional games that use the rock-paper-scissors format, the AI Combat Player utilizes a unique system based on three different types of attacks: sword, fire, and arrow.

The sword attack is a quick and precise strike that can inflict serious damage if executed correctly. It is particularly effective against opponents who rely heavily on defensive maneuvers or who are caught off guard.

The fire attack is a powerful and destructive assault that can engulf opponents in flames, causing them to suffer damage over time. It is particularly effective against opponents who are not well-equipped to deal with fire-based attacks, such as those wearing heavy armor.

The arrow attack is a ranged attack that allows the AI Combat Player to strike opponents from a distance. It is particularly effective against opponents who are unable to close the distance quickly or who are caught in the open.

The AI Combat Player is able to analyze the tactics and movements of its opponents, adapting its own strategies to counter their attacks. It is capable of predicting its opponents' next moves and adjusting its own tactics accordingly, making it a formidable opponent in any combat situation.

With its advanced algorithms and powerful processing capabilities, the AI Combat Player is the ultimate virtual sparring partner for anyone seeking to improve their combat skills or simply enjoy an immersive medieval combat experience.


