# Import your Wunderlist lists into Workflowy

## Why?

Wunderlist was great but is dead. Workflowy is great and alive.

Wunderlist has been part of Microsoft for a while and has been shut down since May 6, 2020. You can move your Wunderlist content to Microsoft To Do. If you want to transfer your data to Workflowy instead, use this script to create a Workflowy-readable version of your Wunderlist data that you can simply paste to Workflowy.

## How To

### Export from Wunderlist

Go to [wunderlist.com](https://www.wunderlist.com/). Under "Get Microsoft To Do" button, click "export" and download your data.

![Click the tiny "export" to get your data out of Wunderlist.](images/export_screenshot.png)

Unzip your downloaded data and note the JSON file. For me, it was called `Tasks.json`.

![This is how your exported JSON will look like.](images/json.png)

*NB: You must download your data by November 15, 2020.*

### Prepare import

Write all your Wunderlist content in Workflowy-readable format:

`python3 workflowy_importer.py ../Tasks.json` (or your differently-named JSON)

(Alternatively send it to a file and copy from there `python3 workflowy_importer.py ../Tasks.json > workflowy_import.txt`.)

![Output of this program](images/output.png)

### Import to Workflowy

Just copy the output of the previous command and paste it in Workflowy. If you already have other bullets in Workflowy I recommend to paste everything inside a bullet called "Wunderlist" and start sorting, moving, and deleting from there.

![Output pasted to Workflowy](images/pasted.png)
