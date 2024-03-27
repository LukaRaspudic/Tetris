# Tetris
This is the Tetris game using the Python library PyGame.

There are a lot of ways to display competence in programming and the one I chose was to create a game. My reasoning for this was to improve my understating of (OOP) object oriented programming. While I have experience with functional programming due to my previous employment, my understanting of OOP was not as extensive.

## 🚀 Quick Start

### Install pygame using pip install

```bash
pip install pygame
```

### Update filepaths

In score.py on line 10, you will have to change the filepath for the font to where you saved the images folder. See below examples.

```python
self.font = pygame.font.Font("ADD YOUR FILE PATH FOR THE FONT IN THE IMAGES FOLDER TITLED pixel-operator.ttf", 30)
```
The below example is what I use for the file path on my machine.

```python
self.font = pygame.font.Font("/workspace/github.com/Revan68/Tetris/images/pixel-operator.ttf", 30)
```
In preview.py on line 12, you will have to reapeat the steps above by updating the file path for images. See below examples.

```python
self.shape_surfaces = {shape: load(f'ADD YOUR FILE PATH HERE THAT LEADS TO IMAGES/images/{shape}.png').convert_alpha() for shape in tetrominos.keys()}
```
The below example is what I use for the file path on my machine.

```python
self.shape_surfaces = {shape: load(f'/workspace/github.com/Revan68/Tetris/images/{shape}.png').convert_alpha() for shape in tetrominos.keys()}
```

## Run main.py in terminal

```bash
python3 main.py
```
or
```bash
python main.py
```
The game should open in a new window and you can start playing.

![Screenshot](https://github.com/Revan68/Tetris/blob/main/images/Screenshot%202024-03-28%20072851.png?raw=true)

## 📖 Usage

Available keys:

* `←: Left Arrow` - Move tetromino left
* `→: Right Arrow` - Move tetromino right
* `↑: Up Arrow` - Rotate tetromino
* `↓: Down Arrow` - Increase rate of decent for tetromino

## 🤝 Contributing

### Clone the repo

```bash
git clone https://github.com/Revan68/Tetris
```

### Update filepaths

In score.py on line 10, you will have to change the filepath for the font to where you saved the images folder. See below examples.

```python
self.font = pygame.font.Font("ADD YOUR FILE PATH FOR THE FONT IN THE IMAGES FOLDER TITLED pixel-operator.ttf", 30)
```
The below example is what I use for the file path on my machine.

```python
self.font = pygame.font.Font("/workspace/github.com/Revan68/Tetris/images/pixel-operator.ttf", 30)
```
In preview.py on line 12, you will have to reapeat the steps above by updating the file path for images. See below examples.

```python
self.shape_surfaces = {shape: load(f'ADD YOUR FILE PATH HERE THAT LEADS TO IMAGES/images/{shape}.png').convert_alpha() for shape in tetrominos.keys()}
```
The below example is what I use for the file path on my machine.

```python
self.shape_surfaces = {shape: load(f'/workspace/github.com/Revan68/Tetris/images/{shape}.png').convert_alpha() for shape in tetrominos.keys()}
```

### Run the project

```bash
python3 main.py
```
or
```bash
python main.py
```

### Enyoy the game 😄

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
