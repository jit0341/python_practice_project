#!/data/data/com.termux/files/usr/bin/bash

TODO_FILE="$HOME/storage/shared/python_practice_project/to-do.md"
TODAY="## 📅 $(date '+%A, %d %B %Y')"

# If today's heading is not present, add it at the top
if ! grep -q "$TODAY" "$TODO_FILE"; then
    echo -e "$TODAY\n\n$(cat "$TODO_FILE")" > "$TODO_FILE"
fi

# Open the file in Neovim
nvim "$TODO_FILE"
