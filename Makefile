all: install

install:
	virtualenv .env --no-site-packages --python=python3.7
	.env/bin/python -m pip install -r requirements.txt

clean:
	rm -rf .env/
