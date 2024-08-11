# Background Removal Tool

This Python script allows you to remove the background from an image using a specified model. The image is downloaded from a provided URL, and the processed image is saved locally.

## Requirements

Ensure that you have the following dependencies installed:

- Python 3.x
- `requests`
- `rembg`
- `Pillow`

You can install these dependencies using pip:

```bash
pip install requests rembg Pillow
pip install --upgrade rembg
```

## Cloning the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/sachinchaunal/Image_Background_Remover.git
cd Image_Background_Remover
```

## Configuration

Before running the script, you'll need to configure the following:

1. **Image URL:** The script requires an image URL to download and process. Modify the `image_url` variable in the script with the URL of the image you wish to process.

2. **Output Path:** You can set the output path where the processed image will be saved. Modify the `output_path` variable accordingly.

3. **Model Selection:** The script uses a model for background removal. You can specify the model by changing the `model_name` parameter in the `remove_background` function. The default model is `'u2net'`. Another option is `'u2net_human_seg'` for human segmentation.

## Usage

To run the script, simply execute the following command in your terminal:

```bash
python SachinChaunal.py
```

After running the script, the background of the image will be removed, and the processed image will be saved to the specified output path.

## Example

```python
if __name__ == "__main__":
    image_url = 'https://i.pinimg.com/originals/ba/15/c0/ba15c084715c971446588c57a8d14e46.jpg'
    output_path = 'output_image.png'
    input_image = download_image(image_url)
    remove_background(input_image, output_path, model_name='u2net_human_seg')
    print("Background removal complete. Check the output image.")
```
