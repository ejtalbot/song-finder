# Song finder app
CLI to query songs by artist in a db.

### Setup

Download repo an navigate into folder
```
git clone https://github.com/ejtalbot/song-finder.git
cd song-finder
```
Create virtual environment (Python >=3.6) and install requirements.
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Create sqlite db and populate with the dataset.
```
python db_setup.py
```
You should see the following output as confirmation:
```
sqlite db setup with schema
loaded artist file
loaded playlist file
```
### Using the CLI
Run the lookup_songs.py which takes one positional argument, the artist name.
See examples below:

Input:
```
python lookup_songs.py Nas
```
Output:
```
If I Ruled The World
```
Input:
```
python lookup_songs.py 'Mariah Carey'
```
Output:
```
Hark! The Herald Angels Sing
Reflections
I'll Be There
Silent Night
I Still Believe
I Want To Know What Love Is
Hero
Without You
Never Too Much
all i want for christmas is you
last night a d.j. saved my life
```