<div align="center">
  
<img src="https://ds-ja-eventa.herokuapp.com/static/images/ds.png">
  
</div>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

# Eventa✨

Personal Project - Eventa 

## Demo💻

[Demo](https://ds-ja-eventa.herokuapp.com/)

## Environment Variables⚙

To run this project, you will need to add the following environment variables to a .env file at the root of the project

- `EMAIL_HOST_USER` : Your smtp email servie provider

- `EMAIL_HOST_PASSWORD` : Password for your smtp email service provder

- `AWS_KEY` : Your aws key for S3

- `AWS_SECRET_KEY` : Your secret aws key for S3

- `AWS_CDN_URL` : Your static cdn url

- `CACHE_USERNAME` : Operator of cache username

- `CACHE_PASSWORD` : Password of cache service password

You can use smtp providers like gmail, sendgrid etc. Update the `EMAIL_HOST` in events/settings.py accordingly.

## Run Locally🚀

Clone the project

```bash
  git clone https://github.com/dineshssdn-867/Events.git
```

Go to the project directory

```bash
  cd events
```

Create Environement and install dependencies

```bash
python m venv env
env\Scripts\activate
pip install -r requirements.txt
```

Make migrations and start the server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

## Features🧾

You can register as a user, event organizer
<details>
  <summary>For Event organizers</summary>
 
  - Register as a event organizer
  - Post Events, Update Events, Delete Events
  - Advertise your events
  - Post a rating review
  - Post a blog
</details>

<details>
  <summary>For Users</summary>
  
  - Register for event
  - Rate Event
  - Post a rating review
  - Post a blog
</details>


## Tech Stack👨‍💻

**Frontend:** HTML, CSS, JS, Bootstrap, React

**Backend:** Django, Firebase, Nginx, Caching Services, AWS Cloudfront

[emoji key](https://allcontributors.org/docs/en/emoji-key)

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/dineshssdn-867"><img src="https://avatars.githubusercontent.com/u/66898317?v=4" width="100px;" alt=""/><br /><sub><b>Dinesh Nariani</b></sub></a><br /><a href="https://github.com/dineshssdn-867/DIM/commits?author=dineshssdn-867" title="Code">💻</a> <a href="https://github.com/dineshssdn-867/DIM/commits?author=dineshssdn-867" title="Documentation">📖</a> <a href="#design-dineshssdn-867" title="Design">🎨</a> <a href="#maintenance-dineshssdn-867" title="Maintenance">🚧</a> <a href="#projectManagement-dineshssdn-867" title="Project Management">📆</a></td>
    <td align="center"><a href="https://github.com/jaympatel481"><img src="https://avatars.githubusercontent.com/u/70288062?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jay Patel</b></sub></a><br /><a href="https://github.com/vinaykakkad/DIM/commits?author=jaympatel481" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
