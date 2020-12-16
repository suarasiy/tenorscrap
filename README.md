# tenorscrap
Tenor scrapping with BeautifulSoup4. Tested on python3.

| Version | Status   |
| ------- | :------: |
| `3.8.3` | Tested   |


## usage

**Import `tenorscrap`**

```python
from tenorscrap import Tenor

tenor = Tenor()
```

#### **Search for tenor:**

```python
search = tenor.search("spongebob squarepants", limit=3)
```

#### **Getting DICT (default)**

By default the output is `list` and with `dict` structure inside. The result is `src`, `width`, `height`, `alt`, `style`, `url` tag format which all is default attrs in Tenor element tag.

```python
result = search.result()
```

**or**

```python
result = search.result(mode="dict")
```

<details>
<summary>📃 Example Result</summary>

```json
[{'src': 'https://media.tenor.com/images/1995989c1b87f95e0b6889b6cb333e4a/tenor.gif',
  'width': '180',
  'height': '135',
  'alt': 'Spongebobsquarepants Chocolate GIF - Spongebobsquarepants Chocolate GIFs',
  'style': 'background-color:#3f3f3f;',
  'url': 'https://tenor.com/view/spongebobsquarepants-chocolate-gif-19415198'},
 {'src': 'https://media.tenor.com/images/7f45ef2933b0fc99d0fd35b519256b55/tenor.gif',
  'width': '180',
  'height': '101.45454545454547',
  'alt': 'Squidward Spongebobsquarepants GIF - Squidward Spongebobsquarepants SeeThat GIFs',
  'style': 'background-color:#3f3f3f;',
  'url': 'https://tenor.com/view/squidward-spongebobsquarepants-see-that-gif-19415199'},
 {'src': 'https://media.tenor.com/images/eec2b6aa655847da8900c5c8d4fbae52/tenor.gif',
  'width': '180',
  'height': '100.63636363636364',
  'alt': 'Clarinet Squidward GIF - Clarinet Squidward SpongebobSquarepants GIFs',
  'style': 'background-color:#3f3f3f;',
  'url': 'https://tenor.com/view/clarinet-squidward-spongebob-squarepants-dance-music-gif-19011171'}]
```
</details>

#### **Getting JSON**

You can get `json` output by adding parameter `mode="json"`.

```python
result_json = search.result(mode="json")
```

<details>
<summary>📃 Example Result</summary>

```json
[
  {
    "alt": "Spongebobsquarepants Chocolate GIF - Spongebobsquarepants Chocolate GIFs",
    "height": "135",
    "src": "https://media.tenor.com/images/1995989c1b87f95e0b6889b6cb333e4a/tenor.gif",
    "style": "background-color:#3f3f3f;",
    "url": "https://tenor.com/view/spongebobsquarepants-chocolate-gif-19415198",
    "width": "180"
  },
  {
    "alt": "Squidward Spongebobsquarepants GIF - Squidward Spongebobsquarepants SeeThat GIFs",
    "height": "101.45454545454547",
    "src": "https://media.tenor.com/images/7f45ef2933b0fc99d0fd35b519256b55/tenor.gif",
    "style": "background-color:#3f3f3f;",
    "url": "https://tenor.com/view/squidward-spongebobsquarepants-see-that-gif-19415199",
    "width": "180"
  },
  {
    "alt": "Clarinet Squidward GIF - Clarinet Squidward SpongebobSquarepants GIFs",
    "height": "100.63636363636364",
    "src": "https://media.tenor.com/images/eec2b6aa655847da8900c5c8d4fbae52/tenor.gif",
    "style": "background-color:#3f3f3f;",
    "url": "https://tenor.com/view/clarinet-squidward-spongebob-squarepants-dance-music-gif-19011171",
    "width": "180"
  }
]
```
</details>