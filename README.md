# The Typing of the Dead: Overkill - A coding dictionary

A Steam Workshop dictionary for the game The Typing of the Dead: Overkill, focused on coding language and concepts.

![DLC Dictionaries](https://steamuserimages-a.akamaihd.net/ugc/39744846856619940/0855CF42BF6BE8DE1D6F2ED39E38FDB2A4B115A4/)

## How to install

This custom dictionary is currently published on Steam Workshop as "On Conding", and you can install it by accessing the folling link and clicking in the `Subscribe` button: https://steamcommunity.com/sharedfiles/filedetails/?id=2454256588

![How to install](/docs/res/how-to-install.jpg)

## Dictionary format

This is the file containing all the words and phrases that players will have to type in the game when they play with your Workshop dictionary enabled.

This needs to be a simple text file (*.txt) with each word and phrase written on a separate line:

```
SOLID
DRY
Don't Repeat Yourself
YAGNI
You Ain't Gonna Need It
C# is cool!
...
```

In this repository, this is done in the file `/dictionary/On Coding.txt`.

You can create this file with your favourite text editor before saving it and selecting it here.
The only thing to keep in mind is that only the following characters are supported in-game:

`aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0)1!2\"3#4$5%6^7&8*9(-_=+ /?,<.>;:'@`

Any other characters will be replaced in-game with ones that it can display.

## Adding new terms to the dictionary

To add new terms to the dictionary, just add them to one of the **themes**, or create a new theme under the `/themes` directory.

Then, run the following command to build the new dictionary:

`python mixer/__main__.py`

## The Typing of the Dead: Workshop Tool

This dictionary is published to the community through the `The Typing of the Dead: Workshop Tool`.

![Workshop tool](https://steamuserimages-a.akamaihd.net/ugc/39744846856559359/1990CB2C54CF1F82D50948B258A6D109948157C6/)

Detailed instructions on how to publish a custom dictionary using this tool is found here: https://steamcommunity.com/sharedfiles/filedetails/?id=414808565

## Some ideas for the future

Following, some ideas for future implementations.

### Dinamic dictionary generation

Build a dictionary from dynamic sources, like web page scrappers. We could extract relevant terms from selected Wikipedia articles, for example.