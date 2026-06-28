Blog CMS Django

A full-featured blog with a content management system built with Django. Includes a rich text editor, category filtering, pagination, and is deployed on Railway with PostgreSQL.

Live Demo: https://web-production-e65d0.up.railway.app



Features

CMS Admin Panel — create, edit, and manage posts through Django's customized admin interface
Rich Text Editor — format post content with CKEditor (bold, italics, lists, images)
Draft / Published System — write posts privately as drafts before publishing them publicly
Categories — organize posts by category with dedicated category pages and clean URLs
Pagination — post list is paginated with category filter preserved across pages
Auto-slug Generation — post slugs are automatically generated from the title in the admin
Reusable Templates — built with template inheritance and partials to keep code DRY


Tech Stack

Backend — Django 6, Python
Database — PostgreSQL (production), SQLite (development)
Rich Text — django-ckeditor
Static Files — Whitenoise
Web Server — Gunicorn
Deployment — Railway


Author

CJ Ilagan
GitHub: [@cjilagan](https://github.com/cjilagan)
