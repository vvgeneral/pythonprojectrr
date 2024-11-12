# Russian Roulette


Aset Saylyavkhan
Github: vvgeneral
United States
2024/06/11

## Description:

This project is the final assignment for the CS50 Introduction to Programming with Python course. After looking through the gallery of final projects, I saw a game about gambling. I kept this in mind while deciding what my project would be about, and then I played a game called Buckshot Roulette. The premise of the game is that you are play Russian roulette with an ai where you need to kill the ai and survive to win. I liked the idea of Russian roulette and my previous thoughts of gambling combined into this project where you have to play Russian roulette to make a million dollars.

The file project.py contains the logic for the game. main() initializes the variables for play_game(starting_money, target_money, tries). play_game(starting_money, target_money, tries) runs all the other at most three times since there are only three tries per game. The first function called within it is the roulette() function which randomly selects a number and then lets the player choose a number 1-6. If the input matches the randomly selected number the player will die, but if it does not the player will live. After living, the player is prompted to continue with this or try or to reset the gun and start the next try. With each continue the amount of money gained is increased so as to encourage the player to take high risk high reward plays. Within roulette() is second_guess() which runs 33% of the time after a player selects a bullet. This function allows the player to change or stick with the bullet they chose.

After the roulette function exits, money is run to multiply the starting money of $10,000 with the amount of multipliers they got that try. The play_game() function also has logic to exit if the player has used up all their tries or to let the player know they won if they reached the $1,000,000 threshold. A function that shows up throughout the code is slow_print(text, char_delay, word_delay) which I used to replace the print() function. This is because the print() function prints out everything immediately, but that doesn't really look good visually for the game. Using the slow_print() function, I can dictate the speed each letter in a word prints and the speed each word in the string prints.

I was considering a design where there is also a dealer that talks to you throughout the game. My idea for him was that he would just be a character in the background that helps the player to immerse but doesn't really change anything for the chances of winning or losing. Because of this, I decided against it as it would be a lot of coding for little return. I was also thinking of implementing a last stand feature where after you reach the $1,000,000 threshold you had to play one more round. The player would only have to guess once to live and then the player could take the money and go home. Once again, I decided against it as I felt like it would not drastically improve or change the way the game plays out.


## License

This documentation is licensed under the [MIT License](LICENSE.md).
