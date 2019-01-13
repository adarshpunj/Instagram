# Instagram
A simple Instagram bot for analysis, and minimising human work.

#### Depedencies:
> [`selenium`](https://www.seleniumhq.org/)
> [`requests`](http://docs.python-requests.org/en/master/)

###### You would also need to have [pynotify](https://github.com/adarshpunj/pynotify).
(You could also choose to remove any usage of pynotify in the program)

#### How to run:
##### 1. Download the project.
##### 2. Open strings.py and make changes (chromium path, username, password, etc.).
##### 3. Run the main.py file

###### Here's a guide to use different functions defined in instagram.py file.

| Function | Description | Arguments |
| :---         |     :---:      |          ---: |
| `login()`   |Logs into instagram     |    |
| `scroll_following_list()`     |Scrolls the following dialog till the end      |      |
| `follow()`   | Follows an Instagram account     | Username (string)|
| `unfollow()`   | Unfollows an instagram account  |Username (string)  |
| `follow_fans_of()`   | Follows accounts who recently liked a page's post     |Page username (string) |
| `follow_users()`   | Picks up usernames from strings.py and calls `follow_fans_of()`|    |
