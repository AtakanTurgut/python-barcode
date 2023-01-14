## Make a barcode generator.
For make a barcode, Barcode module must be installed first.
- Download the latest [Python installer](https://www.python.org/downloads/) for your OS.
I used [this website](https://www.alphr.com/pip-is-not-recognized-as-an-internal-or-external-command/#:~:text=Reinstall%20Python%20to%20Fix%20'Pip,components%20to%20fix%20the%20problem.) for help, you can have a look if you want.
-  Users who want to use pip for installing the Barcode module on Windows in the command prompt have to use the command:
```
pip install python_barcode
```
Whatever we want to print on the barcode, we write it in ' text0 = "example" '.

After the generate, we write the image name in ' save_img = image.save('lastNameBarcode') '.

![](/AtakanTurgutBarcode.png)
