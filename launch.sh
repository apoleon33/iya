echo "preprocessing the css..."
sass static/style.scss static/style.css
echo "done!"

python3 server.py