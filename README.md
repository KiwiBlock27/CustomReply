# TGFS CustomReply Patch

This repository is a patch for **TG-FileStream** that allows overriding default bot reply texts.

---

## 1. Clone and Setup TG-FileStream

First, clone and setup the base project:

https://github.com/SpringsFern/TG-FileStream

Follow the setup instructions provided in that repository's README.

Ensure TG-FileStream is fully working before continuing.

---

## 2. Fork This Repository

Fork this repository and modify:

```
CustomReply/__init__.py
```

You can override any message variable defined in:

https://github.com/SpringsFern/TG-FileStream/blob/main/tgfs/utils/translation.py

Example:

```python
from tgfs.utils.translation import registry, en

class CustomText(en):
    START_TEXT = "Welcome to my custom file server!"

registry["en"] = CustomText
```

---

## 3. Clone Into Patches Directory

Clone your fork inside the `patches` directory.

Your folder structure should look like:

```
<TG-FileStream base folder>/
│
├── tgfs/
│   ├── patches/
│   │   └── CustomReply
```

Example:

```sh
cd <TG-FileStream base folder>/tgfs/patches
git clone https://github.com/<your-username>/CustomReply
```

---

## 4. Restart TG-FileStream

After installation, restart the bot:

```
python -m tgfs
```

Or if running with systemd:

```
sudo systemctl restart tgfs
```

---

## Adding New Language Support

You can:

- Submit translations to:
  https://github.com/SpringsFern/tgfs_translation

OR

- Define a new language class inside your patch:

```python
class CustomSpanish(en):
    START_TEXT = "Hola!"

registry["es"] = CustomSpanish
```

---

## Done

Your custom reply text should now be active.

Always restart the bot after adding or modifying a patch.