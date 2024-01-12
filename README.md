
# Tune Tracker

Tune Tracker is a web application developed with Django and styled using Semantic UI. This app serves as a comprehensive tool for managing and exploring a diverse collection of songs and artists. Users can effortlessly browse through their favorite tunes, add new artists, and associate multiple artists with each song. The sleek and modern interface, designed with Semantic UI, enhances the user experience.
## API Reference

#### Get all songs

```http
  GET /all_songs

  Description : Returns all the Songs along with its Description
```

#### Post song along with artist

```http
  POST /create_song
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Title`      | `string` |  Mention The Title of the song  **required field**|
| `Name`      | `string` |  Mention The name of the artist  **required field**|




## Run Locally

Clone the project

```bash
  git clone https://github.com/yomesh-yadav/FavoriteTunes
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Run Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
Start the server

```bash
python manage.py runserver

```
This will start the Django development server, and you can access your app at http://127.0.0.1:8000/ in your web browser.

