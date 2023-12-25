# Hosts File editor

Just simple pet project for learning python and Qt6.

## Implemented functionality

### Release 0.1

1. Simple GUI with pyQt6
2. Adding new urls to hosts file (with 127.0.0.1)

### Release 0.2
1. URL validation
2. Manual adding custom IP address (if blank its add 127.0.0.1 by default)

### Release 0.3
1. Translation between en and ru locales. (Switcher will be on Settings page later)
2. Added info dialogbox
3. Added exit button functionality
4. Adding new urls to hosts file was purge temporary
5. Added config file 
6. Added manual IP address adding
7. App refactored to work with rules and comments as well

## Plans
~~- Refactor to OOP and MVC pattern (It's not necessary to use MVC and OOP here, but for learning purposes)~~
- ~~Add checkup for input text (must be url)~~
- ~~Translations~~
- ~~Add manual IP address adding~~
- ~~Work with comments (adding, reading)~~
- Linux and macOS builds.
- Need to do checks for hosts file's folder, not only in standard folders. (For all OS)
- Add functionality to read, modify and delete sites in hosts file
- Think about crontab and adding/deleting rules in workhours (manually adding rules)
- Tests-tests-tests
