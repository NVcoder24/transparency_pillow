# transparency_pillow
Program that adds transparency to the image :/

## Libraries
```bash
pip install Pillow
```

## config
```python
cfg = {
    "input_file_name":"input.png",     # input file
    "output_file_name":"output.png",   # output file
    "opacity":0,                       # opacity (0 - 100%)
    "color":(0, 0, 0),                 # (r, g, b) | white (255, 255, 255) | black (0, 0, 0)
    "show_image":False                 # show image after saving it
}
```

## examples
###### input.png
![image](https://github.com/NVcoder24/transparency_pillow/blob/main/input.png)
###### output.png
![image](https://github.com/NVcoder24/transparency_pillow/blob/main/output.png)
###### everything based on default config!
