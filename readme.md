# Project documentation

## Team
424974 Aarni Halinen
529714 Nathan Marcalle
529837 Lassi Mölsä

https://guarded-wave-62136.herokuapp.com/

## Goal

Goal is to create online game store for Javascript games, with support for players and developers alike. Dev's Javascript game hosted on other server is rendered to an iframe of the project service. Service and game servers communicate with window.postMessage(), given in project desciption.



## Plan

### Libraries
- Bootstrap
- AngularJS Framework if needed for 
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
        - Catalog, play button(s, load/save functionality) -> game window and starting game
    - Play

- Basic developer functionalities (mandatory 100-200 points):
    - Adding game
    - Statistics (sales)
    - Security is priority

- Game/service interaction (mandatory 100-200 points):
    - Messaging system
    - By default not secure
- Mobile friendly (Bootstrap)
- 3rd party login to be added
- RESTful API as well
 
### Frontend structure
- Catalog, inventory, gaming and developer sites
- Filters and other minor features to be done, low priority

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
        - Login, basic functionality
- Week 2
    - Frontend features, also filters and extra, if all going well for project
- Week 3
    - Main feautres for backend done (inventory, catalogs etc.)
- Week 4
    - Security for backend
    - Final features for backend done
- Week 5
    - Focus on frontend and polishing backend
    - All features' frontend done
- Week 6
    - Polishing
- Final submission 19.2

## Testing and security

- Backend unit tests should cover near 100%
- Otherwise manual testing
- Apart from message system and payment (http instead of https), software should be safe
    - Authentication
    - Other user items cannot be tampered
    - iframe safety (games cause insecurity?)


