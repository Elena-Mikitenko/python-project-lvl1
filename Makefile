install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-even:
	poetry run brain-even

make lint:
<<<<<<< Updated upstream
	poetry run flake8 brain_games
=======
	poetry run flake8 braingames

>>>>>>> Stashed changes
