tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
        "name": "Authentication",
        "description": "Login logic is here.",
    },
    {
        "name": "Posts",
        "description": "Operations with posts.",
    },
    {
        "name": "Vote",
        "description": "Operations with votes.",
    },
]

description = """
**API for a social media application. 🚀**
* orm SQLAlchemy
* database migration tool Alembic

## Users

You will be able to:

* **Create users**.
* **Read users**.


## Authenticate

You will be able to:

* **Login and authenticate as a user**.
* **Cannot peform operations on post unless your are authenticated**.
* **Cannot peform operations on vote unless your are authenticated**.



## Posts

You will be able to:

* **Create posts**.
* **Read all posts**.
* **Read only one post**.
* **Read only your posts**.
* **Delete your posts**.
* **Update your posts**.

## Vote

You will be able to:

* **Upvote a posts**.
* **Remove your upvote from a posts**.

"""