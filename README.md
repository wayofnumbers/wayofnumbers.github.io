## Theme Tweak##
Change /pelican-themes/elegant/static/css/elegant.css and elegant.prod.css
Change .page-header .h1 h2 h3 h4 h5 etc's font-family to 'PT Sans Narrow', Helvetica, sans-serif, etc. font-weight to bold. font-color to #EA4329

##Script for auto-deployment##
1. Get article URLs and put into article.txt
2. Script read the article.txt and use mediumexporter to convert each of them into MarkDown
3. Script to process the .md file
	- stript empty lines
	- from URL get Slug, from .md file get article title
	- Use the slug and title to construct Markdown file meta-data for Pelican to process
	- Run Pelican to generate site
	- Push to GitHub
	- Auto deploy to Netlify

## favicon
https://stackoverflow.com/questions/31270373/how-to-add-a-favicon-to-a-pelican-blog
