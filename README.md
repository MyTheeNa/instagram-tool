# Instagram Tool by thee0x91

This is a powerful Instagram tool developed by thee0x91. It provides functionalities for downloading Instagram stories, highlights, and posts, as well as checking if users you follow are following you back.

## Features

- **Storyloader:** Download Instagram stories, highlights, and posts of any user.
- **Check Following:** Check which users are not following you back.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/MyTheeNa/instagram-tool.git
    cd instagram-tool
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `config.json` file in the root directory with your Instagram credentials:

    ```json
    {
      "USERNAME": "your_instagram_username",
      "PASSWORD": "your_instagram_password"
    }
    ```

## Usage

1. Run the tool:

    ```sh
    python instagram_tool.py
    ```

2. Select an option from the menu:

    - `1. Storyloader`
    - `2. Check Following`

3. Follow the on-screen prompts to enter the target username and select the desired actions.

## Logging

The tool saves logs for each operation:

- **Storyloader Logs:** Saved in `log/Storyloader/` directory.
- **Check Following Logs:** Saved in `log/checkfollowing/` directory.

## Example

```sh
Please select an option (1 or 2): 1
Enter the target username: example_user
Download posts? (y/n): y
Download highlights? (y/n): y
Download stories? (y/n): y
