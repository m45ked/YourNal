YourNal
=======

Preface
-------

Application for archive RPG sessions events. Users will be able to create tree-like
structure of [Campaign](#Campaign) - [Session](#Session) - [Events](#Event) (one to many).

# Users
User is a person, who participate in a meeting (session).
User can be a *Game master* for a *session*, a participant with his *character*.

Right now in the application you can **make** one, **delete** old and **edit** existing one.

You cannot *make a character* (yet) in the app.

# Campaign
**Campaign** is a structure, that contains a storyline.

Right now in the application you can **make** one, **delete** old and **edit** existing one.

# Session
Session is a whole adventure of characters. It can be a long journey of army of heroes
to save a world or just simple task from your Johnson.

Session is made of series of *events*.

# vvv Not implemented vvv #
yet

# Event
It's a base unit of the universe. It describes particular matter that has place in
the World.

Basically event contains two important information:
* participants,
* description.

Participants are characters, that *know* about the case, that says the description.

Event could alsa contains a GM note, that's allow GM to note important things for
him for the future events.