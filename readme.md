# Project documentation

## Team
424974 Aarni Halinen
<Dev2>
<Dev3>

## Goal

Goal is to create online game store for Javascript games, with support for players and developers alike. Dev's Javascript game hosted on other server is rendered to an iframe of the project service. Service and game servers communicate with window.postMessage(), given in project desciption.



## Plan

### Libraries
- Bootstrap
- AngularJS
- jQuery

### Features
- Registeration
    - Player and developer
    - As a developer: add games to their inventory, see list of game sales
    - As a player: buy games, play games, see game high scores and record their score to it
- Authentication (mandatory, 100-200 points):
    - Email validation
    - Django Auth

- Basic player functionalities (mandatory, 100-300 points):
    - Shop
        - http://payments.webcourse.niksula.hut.fi/
        - Category (Steam-like), search functionality
        - Shopping cart!
    - Inventory
        - Catalog, play button(s, load/save functionality?) -> game window and starting game
    - Play
    - Save/Load (extra)

- Basic developer functionalities (mandatory 100-200 points):
    - Adding game
    - Statistics (sales)
    - User specific inventory (secure!)

- Game/service interaction (mandatory 100-200 points):
    - Messaging system
    - Should be made more secure?
- Mobile friendly (Bootstrap)
- 3rd party login?
- RESTful API?
 
### Frontend structure
- Catalog, inventory, gaming and developer sites
- 

### Backend structure
- One app
- urls
    - Catalog
    - Game info (/<gameid>), information about game, developer
    - Play (game url via views.py)
    - API
- models
    - Normal user
    - Developer
        - Name, email, inventory, password!
    - Games
        - Description
        - Link to developer
    - 

## Schedule and working plan

- Week 51
    - Dev environment setup and planning
- Week 52
    - Backend models, users and developers
    - Unit tests
- Week 1
    - Unit tests complete
    - Frontend:
        - Bootstrap grid system
        - Simple Catalog, gaming, inventory "pages"
    - Backend:
        - 
- Week 2
    - 
- Week 3
    - 
- Week 4
    - 
- Week 5
    - 
- Week 6
    - Final features, polishing
- Final submission 19.2

## Testing and security

- Backend unit tests should cover near 100%
- Otherwise manual testing
- Apart from message system and payment (http instead of https), software should be safe
    - Authentication
    - Other user items cannot be tampered
    - iframe safety (games cause insecurity?)


